
#include <cstdio>
#include <iostream>
#include <cmath>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <sstream>
#include <iterator>
#include <cstdlib>
#include <cstring>
#include <utility>
#include <cctype>
#include <limits>
#include<ctime>

using namespace std;

const double EPS = 1e-9;
//const long long  INF = 1000000000000000000;


typedef pair<double,double> PDD;
typedef vector<long long> VLL;
typedef vector<int> VI;

#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define REP(i,n) FOR(i,0,n)

#define UNIQUE(v) SORT(v), v.erase(unique(v.begin(),v.end()),v.end())
#define SORT(c) sort((c).begin(),(c).end())
#define ll long long
typedef pair<ll, ll> PII;

int n,m;
vector<PII> x,y;


unsigned long long  a[111], b[111];
int A[111], B[111];
unsigned long long  dp[111][111];
int N,M;

unsigned long long  solve_1(unsigned long long  rem, int id, int f, int e)
{
    unsigned long long  ans = 0;

    FOR(i,f,e) if(B[i] == id)
    {
        ans += min(rem, b[i]);
        rem -= min(rem, b[i]);
    }

    return ans;
}

unsigned long long  solve_2(unsigned long long  *aa, int *id, int f, int e)
{
    if(id[0] == id[1])
    {
        return solve_1(aa[0]+aa[1], id[0], f, e);
    }

    unsigned long long  ans = 0;

    REP(ni,M)
    {
        unsigned long long  tmp = 0;
        unsigned long long  c[2] = {aa[0], aa[1]};

        REP(i,ni) if(B[i]==id[0])
        {
            tmp += min(c[0],b[i]);
            c[0] -= min(c[0],b[i]);
        }

        FOR(i,ni,M) if(B[i]==id[1])
        {
            tmp += min(c[1],b[i]);
            c[1] -= min(c[1],b[i]);
        }

        ans = max(ans, tmp);
    }

    return ans;
}

unsigned long long  solve_3(unsigned long long  *aa, int *id, int f, int e)
{
    if(id[0] == id[1] && id[0] == id[2])
    {
        return solve_1(aa[0]+aa[1]+aa[2], id[0], 0, M);
    }

    if(id[0]==id[1])
    {
        unsigned long long  na[2] = {aa[0]+aa[1], aa[2]};
        int nid[2] = {id[0], id[2]};

        return solve_2(na,nid,0,M);
    }

    if(id[2]==id[1])
    {
        unsigned long long  na[2] = {aa[0],aa[1]+aa[2]};
        int nid[2] = {id[0], id[2]};

        return solve_2(na,nid,0,M);
    }

    unsigned long long  ans = 0;

    REP(ni,M) FOR(nj,ni+1,M-1)
    {
        unsigned long long  tmp = 0;
        unsigned long long  aa[3] = {a[0], a[1], a[2]};

        REP(i,ni) if(B[i]==A[0])
        {
            tmp += min(aa[0],b[i]);
            aa[0] -= min(aa[0],b[i]);
        }

        FOR(i,ni,nj) if(B[i]==A[1])
        {
            tmp += min(aa[1],b[i]);
            aa[1] -= min(aa[1],b[i]);
        }

        FOR(i,nj,M) if(B[i]==A[2])
        {
            tmp += min(aa[2],b[i]);
            aa[2] -= min(aa[2],b[i]);
        }

        ans = max(ans, tmp);
    }

    return ans;
}

unsigned long long  solve_easy()
{
    if(N==1)
    {
        return solve_1(a[0],A[0],0,M);
    }

    if(N==2)
    {
        return solve_2(a,A,0,M);
    }

    unsigned long long  ans = 0;

    if(N==3)
    {
        FOR(s,1,1<<3)
        {
            int sz =0 ;
			int ff=1;
			REP(i,5)
			{
				if (s&ff) sz++;
				ff*=2;
			}

            if(sz==1)
            {
                int id = -1;
                for(; id < 3; ++id) if((1<<id)&s) break;

                ans = max(ans, solve_1(a[id],A[id],0,M));
            }

            if(sz==2)
            {
                unsigned long long  aa[2] = {0,0};
                int id[2] = {-1,-1};
                int cnt = 0;

                REP(i,3) if((1<<i)&s)
                {
                    id[cnt] = A[i];
                    aa[cnt] = a[i];
                    cnt ++;
                }

                ans = max(ans,solve_2(aa,id,0,M));
            }

            if(sz==3)
            {
                ans = max(ans, solve_3(a,A,0,M));
            }
        }
    }

    return ans;
}


int main()
{
#ifdef LocalHost
	freopen("input.txt","r",stdin);
	freopen("output_c_easy.txt","w",stdout);
#endif

	int T;
	cin>>T;

	REP(t,T)
	{
        cin >> N >> M;
        REP(i,N) cin >> a[i] >> A[i];
        REP(i,M) cin >> b[i] >> B[i];

        unsigned long long  ans = solve_easy();

        printf("Case #%d: ",t+1);
        cout << ans << endl;
	}

#ifdef LocalHost
	//cout<<endl<<endl<<"TIME: "<<clock()<<endl;
#endif

}