#include <iostream>
#include <fstream>
#include <cmath>
#include <queue>
#include <algorithm>

using namespace std;


int main(int argc, char *argv[])
{
    ifstream ifs("C-small-attempt1.in", ifstream::in);
    int T, i = 1;
    ifs >> T;

    while(i <= T)
    {
        int money = 0;
        unsigned long long R, k, N;
        queue<unsigned long long> g;

        ifs >> R; ifs >> k; ifs >> N;

        while(N > 0)
        {
           unsigned long long tmp;
           ifs >> tmp;
           g.push(tmp);
           N--;
        }

        queue<unsigned long long> tmp;

        while(R > 0)
        {
            while(!tmp.empty())
            {
                g.push(tmp.front());
                tmp.pop();
            }

            money += g.front();
            unsigned long long rest = k - g.front();
            tmp.push(g.front());
            g.pop();
            if(!g.empty())
            {
                while(g.front() <= rest)
                {
                    money += g.front();
                    rest -= g.front();
                    tmp.push(g.front());
                    g.pop();
                    if(g.empty()) break;
                }
            }
            else
            {
                g.push(tmp.front());
                tmp.pop();
            }

            R--;
        }
        cout << "Case #" << i << ": " << money << endl;
        i++;
    }
    ifs.close();
    return 0;
}
