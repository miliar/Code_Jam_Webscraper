#include	<cstdio>
#include	<cstdlib>
#include	<cstring>
#include	<string>
#include	<vector>
#include	<cmath>
#include	<algorithm>
#include	<cassert>
#include	<set>
#include	<map>
#include	<queue>
#include	<iostream>
#include <fstream>
using namespace std;
#define pb push_back
#define REP(i,n) for(int i=0;i<(n);i++ ) 

typedef long long LL;
typedef pair<int,int> piii;

int testCase;
int M,N;
char g[200][200];
int res[20][2000];
inline int countbit(int t)
{
        int sol=0;
        while (t)
        {
                sol+=t&1;
                t/=2;
        }
        return sol;
}
int main()
{
        cin>>testCase;
        REP(testIndex,testCase)
        {
                cin>>M>>N;
                REP(i,M)
                        REP(j,N)
                        {
                                char c;
                                while (1)
                                {
                                        c=getchar();
                                        if (c=='x' || c=='.')
                                                break;
                                }
                                g[i][j]=(c=='x');
                        }
                memset(res,0,sizeof res);
                REP(i,(1<<N))
                {
                        int suc=1;
                        REP(j,N)
                                if ( (i&(1<<j)))
                        {
                                if (g[0][j])
                                {
                                        suc=0;
                                        break;
                                }
                                if (j!=0)
                                        if (i&(1<<(j-1)))
                                        {
                                                suc=0;
                                                break;
                                        }
                                if (j!=N-1)
                                        if (i&(1<<(j+1)))
                                        {
                                                suc=0;
                                                break;
                                        }
                        }
                        if (suc)
                                res[0][i]=countbit(i);
                        //cout<<i<<' '<<res[0][i]<<' '<<suc<<endl;
                }
                REP(i,M-1)
                        REP(j,(1<<N))
                                REP(k,(1<<N))
                                {
                                        int suc=1;
                                        REP(t,N)
                                                if ((k&(1<<t)))
                                        {
                                                if (g[i+1][t]  )
                                                {
                                                        suc=0;
                                                        break;
                                                }
                                                if (t!=0)
                                                {
                                                        if (k&(1<<(t-1)))
                                                        {
                                                                suc=0;
                                                                break;
                                                        }
                                                        if (j&(1<<(t-1)))
                                                        {
                                                                suc=0;
                                                                break;
                                                        }
                                                }
                                                if (t!=N-1)
                                                {
                                                        if (k&(1<<(t+1)))
                                                        {
                                                                suc=0;
                                                                break;
                                                        }
                                                        if (j&(1<<(t+1)))
                                                        {
                                                                suc=0;
                                                                break;
                                                        }
                                                }
                                        }
                                        if (suc)
                                                res[i+1][k]=max(res[i+1][k],countbit(k)+res[i][j]);
                                }
                int sol=0;
                REP(i,(1<<N))
                        sol=max(sol,res[M-1][i]);
                printf("Case #%d: %d\n",testIndex+1,sol);
        }
}
