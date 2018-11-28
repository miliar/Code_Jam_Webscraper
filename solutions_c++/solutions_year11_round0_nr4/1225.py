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
        string delim = " ";
        size_t test_case_num = 0;
        cin >> test_case_num;

        for(size_t i = 0; i < test_case_num; i++)
        {
            cout << "Case #" << (i+1) << ": ";
            int N = 0;
            vector<int> array1;
            cin >> N;
            for (int j = 0; j < N; j++)
            {
                int k = 0;
                cin >> k;
                array1.push_back(k);
            }

            vector<int> array2 = array1;
            sort(array2.begin(), array2.end());

            float hits = 0.0;
            for(int j = 0; j < N; j++)
            {
                if (array1[j] != array2[j]) hits++;
            }

            cout.setf(ios::fixed);
            cout << setprecision(6) << hits;
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
    freopen("D-small-attempt0.in","rt",stdin);
    freopen("D-small-attempt0.out","wt",stdout);
#endif
#ifdef LARGE
    freopen("D-large.in","rt",stdin);
    freopen("D-large.out","wt",stdout);
#endif

    codejam_runner runner;
    runner.run();

    return 0;
}

