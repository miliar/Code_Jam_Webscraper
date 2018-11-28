// codejam.cpp : Defines the entry point for the console application.
//

#include <algorithm>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <deque>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;

unsigned __int64 sum(unsigned __int64 a, unsigned __int64 b)
{
    return (a^b);
}

class codejam_runner
{
public:
    unsigned long run()
    {
        string delim = " ";
        size_t test_case_num = 0;
        cin >> test_case_num;

        for(size_t i = 0; i < test_case_num; i++)
        {
            cout << "Case #" << (i+1) << ": ";

            size_t num = 0;
            vector<unsigned __int64> v;
            cin >> num;
            for (size_t j = 0; j < num; j++)
            {
                unsigned __int64 a = 0;
                cin >> a;
                v.push_back(a);
            }

            sort(v.begin(), v.end());
            size_t n = 0;
            for (n = 0; n < num-1; n++)
            {
                unsigned __int64 sum1 = 0;
                unsigned __int64 sum2 = 0;

                for (size_t j = 0; j < n+1; j++)
                {
                    sum1 = sum(sum1, v[j]);
                }

                for (size_t j = n+1; j < num; j++)
                {
                    sum2 = sum(sum2, v[j]);
                }

                if (sum1 == sum2) break;
            }

            if (n == num-1)
            {
                cout << "NO";
            }
            else
            {
                unsigned __int64 sum2 = 0;
                for (size_t j = n+1; j < num; j++)
                {
                    sum2 = sum2 + v[j];
                }
                cout << sum2;
            }

            cout << endl;
        }
        return 0;
    }
};

//#define SMALL
#define LARGE
int main(int argc, char* argv[])
{
#ifdef SMALL
    freopen("C-small-attempt0.in","rt",stdin);
    freopen("C-small-attempt0,out","wt",stdout);
#endif
#ifdef LARGE
    freopen("C-large.in","rt",stdin);
    freopen("C-large.out","wt",stdout);
#endif

    codejam_runner runner;
    runner.run();

    return 0;
}

