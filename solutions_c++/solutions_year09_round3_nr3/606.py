#include <iostream>
#include <cstdio>
#include <cctype>
#include <string>
#include <cmath>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <sstream>
#include <ctime>
#include <cassert>
#include <string.h>

using namespace std;

#define GI ({int t;scanf("%d",&t);t;})
#define GI64 ({int64 t;scanf("%lld",&t);t;})
#define GD ({double t;scanf("%lf",&t);t;})
#define GS ({string s;cin>>s;s;})
#define f(i,a,b) for(int i=a;i<b;i++)
#define rf(i,a,b) for(int i=a;i>b;i--)
#define SET(x,a) memset(x,a,sizeof(x));
#define all(a) a.begin(),a.end()
#define rall(a) a.rbegin(),a.rend()
#define tr(i,a) for( typeof(a.begin()) i=a.begin();i!=a.end();i++)
#define pb push_back
#define sz(a) (int)(a.size())
#define INF (int)1e9
#define EPS (double)1e-9

typedef long long int64;
typedef pair< int,int > ii;
typedef vector< ii > vii;
typedef vector < vii > vvii;
typedef vector< long long > vi;
typedef vector< vi > vvi;

#define is istringstream
#define os ostringstream

//char ch;
int N;

int go(vi order){
	int ans=0;
	bool seen[N+1];
	f(i,1,N+1)seen[i]=0;
	f(i,0,sz(order)){
		seen[order[i]]=1;
		int lft=0,rgt=0;
		for(int k=order[i]-1;k>0;k--){
			if(seen[k])break;
			lft++;
		}
		for(int k=order[i]+1;k<=N;k++){
			if(seen[k])break;
			rgt++;
		}
		ans+=lft+rgt;
	}
	return ans;
}

int main(){
	int t=GI;
	int cnt=0;
	while(t--){
		cnt++;
		int Q;
		vi order;
		N=GI,Q=GI;
		order.resize(Q);
		f(i,0,Q)order[i]=GI;
		sort(all(order));
		int answer=INF;
		do{
			answer=min(answer,go(order));
		}while(next_permutation(all(order)));
		cout<<"Case #"<<cnt<<": "<<answer<<endl;
	}
	return 0;	
}
