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

class codejam_runner
{
public:
    unsigned long run()
    {
        size_t test_case_num = 0;
        cin >> test_case_num;

        for(size_t j = 0; j < test_case_num; j++)
        {
            cout << "Case #" << (j+1) << ":" << endl;

            size_t team = 0;
            cin >> team;

            vector<vector<double>> vv;
            for(size_t i = 0; i < team; i++)
            {
                vector<double> v;
                string str;
                cin >> str;
                for(size_t k = 0; k < team; k++)
                {
                    if ('.' == str[k])
                    {
                        v.push_back(2.0);
                        continue;
                    }
                    if ('1' == str[k])
                    {
                        v.push_back(1.0);
                        continue;
                    }
                    if ('0' == str[k])
                    {
                        v.push_back(0.0);
                        continue;
                    }
                }
                vv.push_back(v);
            }

            vector<double> ww;
            vector<double> wp;
            vector<double> op;
            for(size_t i = 0; i < team; i++)
            {
                double w = 0.0;
                size_t o = 0;
                for (size_t k = 0; k < vv[i].size(); k++)
                {
                    if (2.0 != vv[i][k])
                    {
                        w += vv[i][k];
                        o++;
                    }
                }
                ww.push_back(w);
                if (0 < o) w = w/o;
                wp.push_back(w);
                op.push_back(o);
            }

            vector<double> owp;
            for(size_t i = 0; i < team; i++)
            {
                double w = 0.0;
                if (0 == op[i])
                {
                    owp.push_back(w);
                    continue;
                }
                for (size_t k = 0; k < vv[i].size(); k++)
                {
                    if (2.0 != vv[i][k])
                    {
                        if (1 < op[k]) w += ((ww[k]-vv[k][i])/(op[k]-1));
                    }
                }
                w = w/(op[i]);
                owp.push_back(w);
            }

            vector<double> oowp;
            for(size_t i = 0; i < team; i++)
            {
                double w = 0.0;
                if (0 == op[i])
                {
                    oowp.push_back(w);
                    continue;
                }
                for (size_t k = 0; k < vv[i].size(); k++)
                {
                    if (2.0 != vv[i][k])
                    {
                        w += owp[k];
                    }
                }
                w = w/op[i];
                oowp.push_back(w);
            }

            for(size_t i = 0; i < team; i++)
            {
                cout.setf(ios::fixed);
                cout << setprecision(12) <<  (0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i]) << endl;
            }

        }

        return 0;
    }
};

//#define SMALL
#define LARGE
int main(int argc, char* argv[])
{
    freopen("a.txt","rt",stdin);
#ifdef SMALL
    freopen("A-small-attempt0.in","rt",stdin);
    freopen("A-small-attempt0.out.txt","wt",stdout);
#endif
#ifdef LARGE
    freopen("A-large.in","rt",stdin);
    freopen("A-large.out.txt","wt",stdout);
#endif

    codejam_runner runner;
    runner.run();

    return 0;
}

