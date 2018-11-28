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

#define GI ({int t;cin>>t;t;})
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

const int mn=103;
int n;
PII inp[mn];

int main(){
	
	freopen("inp.txt","r",stdin);
	freopen("out.txt","w",stdout);
	
	int Kase=GI;
	FOR(kase,1,Kase+1){
		int ans=0;
		n=GI;
		REP(i,n){
			char c;cin>>c;
			inp[i].second=GI;
			inp[i].first=(c=='B');	
		}
		int cur[2]={1,1}, tot=0, prev=-1;
		REP(i,n){
			if(prev==1-inp[i].first){
				int tosub=max(0,abs(inp[i].second-cur[ inp[i].first ])-tot)+1;
				tot=tosub;
				prev=inp[i].first;
				cur[ inp[i].first ]=inp[i].second;
				ans+=tosub;	
			}
			else{
				prev=inp[i].first;
				int tosub=abs(inp[i].second-cur[inp[i].first])+1;
				tot+=tosub;
				cur[ inp[i].first]=inp[i].second;
				ans+=tosub;
			}
		}
		printf("Case #%d: %d\n",kase,ans);
		cerr<<"Completed "<<kase<<endl;
	}
	
	cerr<<"Completed all"<<endl;
	while(1);
	return 0;
}
