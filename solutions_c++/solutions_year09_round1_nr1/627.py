#include <iostream>
#include <cstdio>
#include <cctype>
#include <algorithm>
#include <stack>
#include <queue>
#include <vector>
#include <string>
#include <cmath>
#include <map>
#include <set>
#include <ctime>
#include <sstream>
#include <string.h>

using namespace std;

#define GI ({int t;scanf("%d",&t);t;})
#define GD ({double d;scanf("%lf",&d);d;})
#define GS ({string s;cin>>s;s;})
#define f(i,a,b) for(int i=a;i<b;i++)
#define tr(i,a) for( typeof(a.begin()) i=a.begin();i!=a.end();i++)
#define SET(x,a) memset(x,a,sizeof(x))
#define all(a) a.begin(),a.end()
#define rall(a) a.rbegin(),a.rend()
#define pb push_back 
#define sz(a) (int)(a.size())
#define INF (int)1e9
#define EPS (double)1e-9

typedef long long in64;
typedef vector<int> vi;
typedef vector< vi > vvi;
typedef pair<int,int> ii;
typedef vector< ii > vii;
typedef vector< vii > vvii;

#define is istringstream
#define os ostringstream

int ok(int x,int base){
	bool seen[1000005];
	SET(seen,0);
	while(1){
		int ans=0;
		while(x){
			ans+=(x%base)*(x%base);
			x/=base;
		}
		if(seen[ans])break;
		seen[ans]=1;
		x=ans;
	}
	if(seen[1])return 1;
	return 0;
}

int main(){
	int t=GI;
	cin.get();
	int p=0;
	while(t--){
		p++;
		string s;
		getline(cin,s);
		istringstream sin(s);
		int a=-1,b=-1,c=-1;
		bool flag=0;
		sin>>a>>b>>c;
		if(c==-1){
			int val=2;
			while(1){
				if(ok(val,a) && ok(val,b)){cout<<"Case #"<<p<<": "<<val<<endl;break;}
				val++;
			}
		}
		else{
			int val=2;
			while(1){
				if(ok(val,a) && ok(val,b) && ok(val,c)){cout<<"Case #"<<p<<": "<<val<<endl;break;}
				val++;
			}
		}
	}
	return 0;
}





