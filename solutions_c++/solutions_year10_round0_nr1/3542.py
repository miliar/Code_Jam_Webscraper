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

long t,n,i,k,q,r,s,total;
bool con;
int main()
{
    #ifndef ONLINE_JUDGE
        freopen("A-large.in", "r", stdin);
        freopen("out.out", "w", stdout);
    #endif
    
    scanf("%ld",&t);
    total =t;
    long a[31];
    a[1]=1;
    for(i=2;i<=30;i++)
		a[i]=2*a[i-1];
    while(t--){
		con=true;
		scanf("%ld %ld",&n,&k);
		if(k==0){
			printf("Case #%ld: %s\n",total-t,"OFF");
			continue;
		}
		for(i=1;i<=n;i++){
			q=(k+1)/a[i];
			r=(k+1)%a[i];
			s=q%2;
			if((s==0 && r==0) || (s==1 && r!=0))
				continue;
			else{
				con = false;
				break;
			}
		}
		printf("Case #%ld: %s\n",total-t,con?"ON":"OFF");
       
    }
    return 0;
}

 

