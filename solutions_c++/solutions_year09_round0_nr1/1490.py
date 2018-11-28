#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cmath>

using namespace std;

#define GI ({int t;scanf("%d",&t);t;})
#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define REP(i,n) FOR(i,0,n)
#define pb push_back
#define sz size()
#define INF (int)1e9

typedef long long LL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<vector<int> > VVI;

const int ml=17,md=5003;
int l,d,Kase;
string a[md];

int main(){
	
	cin>>l>>d>>Kase;
	REP(i,d)	cin>>a[i];
	FOR(kase,1,Kase+1){
		string s;
		cin>>s;
		int ans=0;
		REP(i,d){
			int last=0;
			REP(j,l){
				bool present[28];	
				REP(r,28)	present[r]=0;
				if(s[last]!='('){
					present[ s[last]-'a']=1;
					last++;
				}
				else{
					for(last=last+1;s[last]!=')';last++)	present[ s[last]-'a' ]=1;
					last++;
				}
				if(!present[ a[i][j]-'a' ])	break;
				if(j==l-1)	ans++;
			}
		}
		printf("Case #%d: %d\n",kase,ans);
	}
	
	
	
	return 0;
}
