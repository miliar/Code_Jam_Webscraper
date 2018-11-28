#include <vector>
#include <string>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cstring>
#include <ctype.h>
#include <bitset>
#include <assert.h>
using namespace std;

#define REP(i, n) for(int i=0; i<(n); i++)
#define FOR(i, a, b) for(int i=(a); i<(b); i++)
#define IFOR(i, a, b) for(int i=(a); i>=(b); i--)
#define FORD(i, a, b, c) for(int i=(a); i<(b); i+=(c))

#define SS ({int x;scanf("%d", &x);x;})
#define SI(x) ((int)x.size())
#define PB(x) push_back(x)
#define MP(a,b) make_pair(a, b)
#define SORT(a) sort(a.begin(),a.end())
#define ITER(it,a) for(typeof(a.begin()) it = a.begin(); it!=a.end(); it++)
#define ALL(a) a.begin(),a.end()
#define INF 1000000000
#define V vector
#define S string
#define FST first
#define SEC second
#define MAX 1000

typedef V<int> VI;
typedef V<S> VS;
typedef long long LL;
typedef pair<int, int> PII;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("jam.txt", "w", stdout);
    int t=SS,cas=0;
    while(t--)
    {
        cas++;
        int n=SS;
        V < VI > tab(n,VI(n));
        V <double> win(n,0),lose(n,0);
        lose=win;
        V <double> owp(n);
        REP(i,n)
        REP(j,n)
        {
            char ch;
            cin>>ch;
            if(ch=='.')
                tab[i][j]=-1;
            else if(ch=='1')
            {
                tab[i][j]=1;
                win[i]+=1;
            }
            else
            {
                tab[i][j]=0;
                lose[i]+=1;
            }
        }
        vector <double> ans(n,0);
        REP(i,n)
        {
            ans[i]=0.25*(win[i]/(win[i]+lose[i]));
            
        }
        REP(i,n)
        {
            double ow=0;
            REP(j,n)
            {
                if(i==j)
                    continue;
                if(tab[i][j]==1)
                {
                    ow+=(win[j]/(win[j]+lose[j]-1));
                }
                else if(tab[i][j]==0)
                {
                    ow+=((win[j]-1)/(win[j]+lose[j]-1));
                }
                
            }
            ow/=(win[i]+lose[i]);
            owp[i]=ow;
            ans[i]+=(0.5*owp[i]);
        }
        REP(i,n)
        {
            double temp=0;
            REP(j,n)
            {
                if(tab[i][j]>=0)
                {
                    temp+=owp[j];
                }
            }
            temp/=(win[i]+lose[i]);
            ans[i]+=(0.25*temp);
        }
        cout<<"Case #"<<cas<<":\n";
        REP(i,n)
        printf("%.12lf\n",ans[i]);
    }
    return 0;
}
