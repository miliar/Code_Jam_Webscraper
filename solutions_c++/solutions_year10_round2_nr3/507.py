#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int seat(int mask, int n)
{
    int res = 0;
    for (int i=0; i<n; i++)
        if ((mask&(1<<i))>0)
            res++;
    return res+1;
}

int main()
{
    int T; 
    cin >> T;
    for (int testCase=1; testCase<=T; testCase++) {
        int N;
        cin >> N;
        int res = 0;
        N -= 2;
        for (int i=0; i<(1<<N); i++)
        {
            bool isOk = true;
            int count = seat(i, N);
            while (count!=1) {
                if ((i&(1<<(count-2)))==0) {
                    isOk = false;
                    break;
                }
                count = seat(i, count-2);  
            }
            if (isOk)
                res++;
        }
        cout << "Case #" << testCase << ": " << res%100003 << endl;
    }

    return 0;
}
