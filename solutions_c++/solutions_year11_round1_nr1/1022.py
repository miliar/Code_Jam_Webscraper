#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <cmath>
#include <sstream>
#include <map>
#include <set>
#include <numeric>
#include <memory.h>
#include <cstdio>

using namespace std;

#define pb push_back
#define INF 101111111
#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define rep(i,n) FOR(i,0,n)
#define ford(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define CL(a,v) memset((a),(v),sizeof(a))
#define mp make_pair
#define X first
#define Y second
#define all(c) (c).begin(), (c).end()
#define SORT(c) sort(all(c))

typedef long long ll;
typedef vector<int> VI;
typedef pair<int,int> pii;

int GCD(int x, int y)
{
    return x==0 ? y : GCD(y%x,x);
}


int main()
{
	#ifndef ONLINE_JUDGE
        freopen("A-large.in","r",stdin);
        //freopen("input.txt","r",stdin);
        freopen("output.txt","w",stdout);
	#endif

    int T;
    cin >> T;

    FOR(cs,1,T+1)
    {
        ll N;
        int pg,pd;

        cin >> N >> pd >> pg;

        cout << "Case #" << cs <<": ";

        if(pg == 0)
        {
            if(pd==0)
                cout << "Possible" << endl;
            else
                cout << "Broken" << endl;
        }
        else if(pg == 100)
        {
            if(pd == 100)
                cout << "Possible" << endl;
            else
                cout << "Broken" << endl;
        }
        else
        {
//            int a = GCD(pd, 100);
//            int b = GCD(100-pd, 100);
//            int pd1 = pd/a;
//            int pd2 = (100-pd)/b;
//            int gcd = GCD(pd1,pd2);
//            int lcm = pd1*pd2/gcd;
//
//            if(N >= lcm)
//                cout << "Possible" << endl;
//            else
//                cout << "Broken" << endl;

            if(N >= 100LL)
                cout << "Possible" << endl;
            else
            {
                bool possible = false;

                FOR(n,1,N+1)
                {
                    int pd1 = n*pd/100;
                    int pd2 = n*(100-pd)/100;

                    if(pd1 + pd2 == n)
                    {
                        possible = true;
                    }
                }

                if(possible)
                    cout << "Possible" << endl;
                else
                    cout << "Broken" << endl;

            }

        }

    }


	return 0;
}
