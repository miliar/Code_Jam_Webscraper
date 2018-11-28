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
            cout << "Case #" << (j+1) << ": ";

            int icombine = 0;
            int iopposed = 0;
            map<string,string> mcombine;
            map<string,string> mopposed;

            cin >> icombine;
            for (int i = 0; i < icombine; i++)
            {
                string str;
                cin >> str;
                string base_pair = str.substr(0,2);
                string non_base = str.substr(2,1);
                mcombine.insert(map<string,string>::value_type(base_pair, non_base));
                reverse(base_pair.begin(), base_pair.end());
                mcombine.insert(map<string,string>::value_type(base_pair, non_base));
            }

            cin >> iopposed;
            for (int i = 0; i < iopposed; i++)
            {
                string str;
                cin >> str;
                string base_pair = str.substr(0,2);
                string non_base = str.substr(2,1);
                mopposed.insert(map<string,string>::value_type(str.substr(0,1), str.substr(1,1)));
                mopposed.insert(map<string,string>::value_type(str.substr(1,1), str.substr(0,1)));
            }

            size_t invoked = 0;
            string tmp_str;
            string out_str = "";
            cin >> invoked;
            cin >> tmp_str;
            for (size_t i = 0; i < invoked; i++)
            {
                out_str += (tmp_str.at(i));
                size_t z = out_str.size();
                if (2 > z) continue;

                if (0 < icombine)
                {
                    string last2 = out_str.substr(z-2, 2);
                    map<string,string>::iterator it;
                    if (mcombine.end()!= (it = mcombine.find(last2)))
                    {
                        out_str = out_str.substr(0, z-2) + it->second;
                    }
                }

                if (0 < iopposed)
                {
                    string last1 = out_str.substr(z-1, 1);
                    map<string,string>::iterator it;
                    if (mopposed.end()!= (it = mopposed.find(last1)))
                    {
                        if (out_str.npos != out_str.find(it->second)) out_str = "";
                    }
                }
            }

            size_t z = out_str.size();
            cout << "[";
            for (size_t i = 0; i < z; i++)
            {
                if (0 != i) cout << ", ";
                cout << out_str.at(i);
            }
            cout << "]";
            cout << endl;
        }
        return 0;
    }
};

#define SMALL
//#define LARGE
int main(int argc, char* argv[])
{
#ifdef SMALL
    freopen("B-small-attempt0.in","rt",stdin);
    freopen("B-small-attempt0.out","wt",stdout);
#endif
#ifdef LARGE
    freopen("B-large.in","rt",stdin);
    freopen("B-large.out","wt",stdout);
#endif

    codejam_runner runner;
    runner.run();

    return 0;
}

