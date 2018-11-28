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

        for(size_t i = 0; i < test_case_num; i++)
        {
            cout << "Case #" << (i+1) << ": ";

            vector<size_t> v0;
            vector<size_t> v1;
            vector<vector<size_t>> v;
            vector<size_t> token;
            v.push_back(v0);
            v.push_back(v1);

            size_t N = 0;
            cin >> N;
            for (size_t i = 0; i < N; i++)
            {
                char c = 0;
                size_t p = 0;
                cin >> c;
                cin >> p;
                if ('O' == c)
                {
                    v[0].push_back(p);
                    token.push_back(0);
                }
                else
                {
                    v[1].push_back(p);
                    token.push_back(1);
                }
            }

            size_t scond = 0;
            size_t k = 0;
            size_t p[2] = {1, 1};
            size_t q[2] = {0, 0};
            size_t r[2] = {v[0].size(), v[1].size()};
            size_t token_size = token.size();

            while (k < token_size)
            {
                bool press_button = false;
                for(size_t i = 0; i < 2; i++)
                {
                    if (0 == r[i]) continue;
                    if (p[i] == v[i][q[i]])
                    {
                        if (i == token[k])
                        {
                            press_button = true;
                           q[i] = min((q[i])+1, (r[i])-1);
                        }
                    }
                    else
                    {
                        (p[i] < v[i][q[i]])?((p[i])++):(((p[i])--));
                    }
                }
                if (press_button) k++;
                scond++;
            }
            cout << scond << endl;
        }
        return 0;
    }
};

//#define SMALL
#define LARGE
int main(int argc, char* argv[])
{
#ifdef SMALL
    freopen("A-small-attempt0.in","rt",stdin);
    freopen("A-small-attempt0,out","wt",stdout);
#endif
#ifdef LARGE
    freopen("A-large.in","rt",stdin);
    freopen("A-large.out","wt",stdout);
#endif

    codejam_runner runner;
    runner.run();

    return 0;
}

