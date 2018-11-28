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
    char m[33]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
    char line[101];
    S(cases);
    getchar();
    int c=1;
    while(cases--){
		cin.getline( line, 101);
		int l = strlen(line);
		for(int i=0 ; i<l ; i++){
			if(line[i]!=' '){
				line[i]=m[line[i]-97];
			}			
		}
		printf("Case #%d: %s\n",c++,line);
    }
    return 0;
}
