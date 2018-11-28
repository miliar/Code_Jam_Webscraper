#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <string>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <cstdio>
#include <cctype>
#include <cassert>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define REP(i,n) FOR(i,0,n)
#define sz size()
#define pb push_back
#define GI ({int t;scanf("%d",&t);t;})
#define INF int(1e9)

typedef long long LL;
typedef vector<int> VI;
typedef vector< vector<int> > VVI;
typedef vector<string> VS;
typedef pair<int,int> PII;

const int mn=42;
char mat[mn][mn];
int n;
int last[mn];

int main(){
	
	freopen("inp.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int Kase=GI;
	FOR(kase,1,Kase+1){
		
		n=GI;
		REP(i,n)	scanf("%s",mat[i]);
			
		REP(i,n)	last[i]=0;
		REP(i,n)	REP(j,n)	if(mat[i][j]=='1')	last[i]=j;
		int ans=0;
		/*REP(i,n){
			for(int j=0;j<n-i-1;j++){
				if(last[j]>last[j+1]){
					ans++;
					swap(last[j],last[j+1]);	
				}	
			}
		}*/
		REP(i,n){
			if(last[i]<=i)	continue;
			int j=i+1;
			for(;j<n;j++)	if(last[j]<=i){
				for(int k=j;k>i;k--)	last[k]=last[k-1],ans++;
				break;	
			}
		}
		printf("Case #%d: %d\n",kase,ans);
		
			
	}
	
	cerr<<"Finished Executing"<<endl;
	while(1);
	return 0;
}
