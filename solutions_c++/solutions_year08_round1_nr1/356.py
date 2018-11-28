#include <vector>
#include <string>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <algorithm>

using namespace std;

int main(int argc, char **argv)
{
    int NNNNN;
    cin >> NNNNN;
    for (int cccccc=1;cccccc<=NNNNN;++cccccc)
    {
        cout << "Case #" << cccccc << ": ";
        
        // CODE
        int n;
        cin >> n;
        vector<long long> x, y;
        for (int i=0;i<n;++i)
        {
            long long xx;
            cin >> xx;
            x.push_back(xx);
        }
        for (int i=0;i<n;++i)
        {
            long long xx;
            cin >> xx;
            y.push_back(xx);
        }
        sort(y.begin(), y.end());
        long long min = 10000000000000000LL;
        do
        {
            long long now = 0;
            for (int i=0;i<n;++i)
            {
                now += x[i] * y[i];
            }
            if (now < min) min = now;
        } while(next_permutation(y.begin(), y.end()));
        cout << min << endl;
        // END OF CODE
    }
    return 0;
}