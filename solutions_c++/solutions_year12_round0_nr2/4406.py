// =============================================================================
// 
//       Filename:  B.cpp
// 
//    Description:  Dancing With the Googlers
// 
//        Version:  1.0
//        Created:  04/14/2012 03:31:41 PM
//       Revision:  none
//       Compiler:  g++
// 
//         Author:  SphinX (Whisper), TopCoderSphinX@Gmail.com
//        Company:  HFUT
// 
// =============================================================================

#include <vector>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
using namespace std;

typedef vector<int> VI;

const int MAXN = 1004;

int stateJudge(int n, int m)
{
    int buf = n - m * 3;
    if (buf >= -2) 
    {
        return 1;
    }
    if (buf >= -4) 
    {
        if (m <= 1) 
        {
            return 0;
        }
        return 2;
    }
    return 0;
}
void ace()
{
    int test, n, s, p;
    int cas = 1;
    int res, data;
    VI arr;
    for (cin >> test; test--; ++cas) 
    {
        cin >> n >> s >> p;
        arr.clear();
        for (int i = 0; i < n; ++i) 
        {
            cin >> data;
            arr.push_back(data);
        }
        res = 0;
        for (int i = 0; i < n; ++i) 
        {
            int flag = stateJudge(arr[i], p);
            if (0 == flag) 
            {
                continue ;
            }
            if (1 == flag) 
            {
                ++res;
            }
            else
            {
                if (s != 0) 
                {
                    --s;
                    ++res;
                }
            }
        }
        cout << "Case #" << cas << ": " << res << endl;
    }
    return ;
}
int main(int argc, char *argv[]) 
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    ace();
    return EXIT_SUCCESS;
}
