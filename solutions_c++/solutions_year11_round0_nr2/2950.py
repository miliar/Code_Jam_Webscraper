#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <cstdio>
#include <string>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <string.h>
#include <cassert>

using namespace std;

#define GI ({int t;scanf("%d",&t);t;})
#define FOR(i,a,b) for(int i=a;i<b;i++)
#define REP(i,n) FOR(i,0,n)
#define pb push_back
#define sz size()
#define INF (int)1e9
#define EPS LD(1e-9)
#define DINF LD(1e50)

typedef long long LL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<vector<int> > VVI;
typedef pair<int,int> PII;
typedef double LD;

const int mc=37, md=29, mn=103;
int c,d,n;
char combine[26][26], buf[20];
bool destroy[26][26];

int main(){
	
	freopen("inp.txt","r",stdin);
	freopen("out.txt","w",stdout);
	
	int Kase=GI;
	FOR(kase,1,Kase+1){
		REP(i,26)	REP(j,26)	combine[i][j]='0', destroy[i][j]=0;
		c=GI;
		REP(i,c){
			scanf("%s",buf);
			combine[ buf[0]-'A' ][ buf[1]-'A' ]=combine[ buf[1]-'A' ][ buf[0]-'A' ]=buf[2];
		}
		d=GI;
		REP(i,d){
			scanf("%s",buf);
			destroy[ buf[0]-'A' ][ buf[1]-'A' ]=destroy[ buf[1]-'A' ][ buf[0]-'A' ]=1;
		}
		n=GI;
		scanf("%s",buf);
		vector<char> ans;
		REP(i,n){
			if(ans.sz>0){
				char v=ans[ ans.sz-1 ];
				if(combine[ v-'A' ][ buf[i]-'A' ]!='0'){
					ans[ ans.sz-1 ]=combine[ v-'A' ][ buf[i]-'A' ];
					continue;
				}
			}	
			bool toclear=0;
			REP(j,ans.sz)	if(destroy[ ans[j]-'A' ][ buf[i]-'A' ])	toclear=1;
			if(toclear){
				ans.clear();
				continue;	
			}
			ans.pb(buf[i]);
		}
		printf("Case #%d: ",kase);
		printf("[");
		REP(i,ans.sz){
			if(i)	printf(", ");	
			printf("%c",ans[i]);
		}
		printf("]\n");
		cerr<<"Completed "<<kase<<endl;
	}
	
	cerr<<"Completed all"<<endl;
	while(1);
	return 0;
}
