#include <iostream>
#include <string>
#include <sstream>

using namespace std;

int main()
{
    int inputs;
    cin >> inputs;




    string str;
    getline(cin, str);

    for (int i = 0; i < inputs; ++i) {

        getline(cin, str);

        istringstream isstr(str);

        int R, k, N;
        isstr >> R >> k >> N;

/*
        cout << R << " " << k << " " << N << endl;
*/

        getline(cin, str);

        int group[10000];
        isstr.clear();
        isstr.str(str);

        int x;
        int j = 0;
        while (!(isstr >> x).eof()) {
              group[j++] = x;
        }
        group[j++] = x;

        int begin = 0;
        int earning = 0;

        for (int m = 0; m < R; ++m) {

            int filled = 0;
            int start = begin;

            do {
               int x = filled+group[begin];
               if (x > k)
                  break;
               filled = x;
               begin = (begin+1)%N;
            } while (begin != start);

            earning += filled;
/*
            cout << filled << " " << begin << " " << group[begin] << endl;
*/
        }

        cout << "Case #" << (i+1) << ": " << earning << endl;
    }

}
