/* Song Qiang
 */ 

#include <cmath>

#include <string>
#include <vector>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <limits>

using namespace std;

int
main(int argc, const char **argv)
{
    ifstream in(argv[1]);
    ofstream out(argv[2]);
    
    int T;
    in >> T;

    for (size_t t = 0; t < T; ++t)
    {
        int N;
        in >> N;

        vector<int> button(N + 1, 1);
        vector<char> bots(N + 1, 'O');
        vector<int> prev(N + 1, 0);
        int po = 0, pb = 0;
        char ch;
        for (size_t i = 1; i < N+1; ++i)
        {
            in >> bots[i] >> button[i];
            if (bots[i] == 'O')
            {
                prev[i] = po;
                po = i;
            }
            else  if (bots[i] == 'B')
            {
                prev[i] = pb;
                pb = i;
            }
            else
            {
                cerr << "error" << endl;
            }
//            cout << prev[i] << "\t";
        }
        
//        cout <<  endl;
        

        vector<int> time(N + 1, 0);
        for (size_t i = 1; i < N + 1; ++i)
        {
            int need_waiting = time[i - 1] + 1;
            int no_waiting =
                time[prev[i]] + abs(button[i] - button[prev[i]]) + 1;
            time[i] = max(need_waiting, no_waiting);
//            cout << time[i] << "\t";
        }
        
        cout << "Case #" << t+1 << ": " << time.back() << endl;
    }
  
    return EXIT_SUCCESS;
}
