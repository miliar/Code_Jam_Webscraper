#include<iostream>
#include<cstdio>
#include<queue>
#include<cstring>
#include<map>
#include<algorithm>
#include<cmath>
#include<set>
#include<sstream>
#include<map>
#include<utility>
#include<cstdlib>
#include<vector>
#include<numeric>

#define REP(i,n) for(i=0; i<n; i++)
#define REPA(i,a,n) for(i=a; i<n; i++)
#define SOR(x) sort(x.begin(), x.end())
#define REV(x) reverse(x.begin(), x.end())
#define FOREACH(iter,var) for(__typeof((var).begin()) iter=(var).begin(); iter!=(var).end(); iter++)
#define PB push_back
#define VI vector<int>
#define SZ size()
#define VS vector<string>

#define MP make_pair
#define VVI vector< vector<int> >
#define INF 2000000000

#define CLR(var,val) memset(var,val,sizeof((var)))
#define S(n) scanf("%d",&n)
#define LL long long
#define LD long double
#define triple pair<int, pair<int,int> >
#define OFF 0
#define MAX(a,b) (a>b?a:b)

using namespace std;

int cases,n,s,p,x;


int main()
{
    #ifndef ONLINE_JUDGE
        freopen("inp.in", "r", stdin);
        freopen("out.out", "w", stdout);
    #endif
    int t[31]={0,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,9,9,9,10,10,10};
    int u[31]={0,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,9,9,9,10,10,10,10,10};    
    S(cases);
    int c=1;
    while(cases--){
		cin>> n >> s >> p;
		int r = 0;
		for(int i=0 ; i<n ; i++){
			cin >>x;
			if(t[x]>=p){
				r++;
			}else if(s>0 && u[x]>=p){
				r++;
				s--;
			}			
		}
		printf("Case #%d: %d\n",c++,r);
    }
    return 0;
}

 
