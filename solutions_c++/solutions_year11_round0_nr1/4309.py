#include<iostream>
#include<sstream>
#include<algorithm>
#include<numeric>
#include<vector>
#include<string>
#include<map>
#include<set>
#include<list>
#include<stack>
#include<queue>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<cctype>
#include<climits>
#include<cfloat>
#include<cassert>
#define dbge( x ) cout << #x << " : " <<  x << endl;
using namespace std;


int main()
{
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++)
    {
        int N;
        cin  >> N;
        long long int seconds = 0;
        int gO = 0, gB = 0; //Extra seconds provided to each robot to make the next move
        int pO = 1, pB = 1; //Current positions of the robots
        for(int i = 0; i < N; i++)
        {
            char a;
            int x;
            cin >> a;
            cin >> x;
            if(a == 'O')
            {
                int need = abs(x - pO) + 1;
                int taken;
                if(need > gO)
                    taken = need - gO;
                else 
                    taken = 1;
                gO = 0;
                gB += taken;
                seconds += taken;
                pO = x;
            }
            else
            {
                int need = abs(x - pB) + 1;
                int taken;
                if(need > gB)
                    taken = need - gB;
                else 
                    taken = 1;
                gB = 0;
                gO += taken;
                seconds += taken;
                pB = x;
            }
        }
        printf("Case #%d: ", t);
        cout << seconds << endl;
    }
    return 0;
}

