#include<iostream>
#include<vector>
#include<algorithm>
#include<cstdio>
#include<map>
#include<set>
#include<cstring>
#include<string>
#include<queue>
#include<cctype>
#include<functional>
#include<fstream>
#include<sstream>
#include<complex>
#include<cmath>
#include<cstdlib>

using namespace std;

#define EPS 1.0e-10
#define REP(i,n) for(int i=0;i<n;i++)
#define ALL(t) t.begin(),t.end()
#define FOR(it,c) for(__typeof((c).begin()) it = (c).begin();it != (c).end();++it)
#define ll long long
#define mp make_pair
#define pb push_back
#define F first
#define S second
inline int signum(double x) { return (abs(x) < EPS ? 0 : x > 0 ? 1 : -1); }
const int SIZE=100;
int main(){
	int n,m;
	while(cin>>n>>m){
		string name[SIZE];
		map<string,int>id;
		REP(i,n){
			cin>>name[i];
			id[name[i]]=i;
		}
		bool ok[SIZE][SIZE]={0};
		REP(i,m){
			string a,b;
			cin>>a>>b;
			ok[id[a]][id[b]]=true;
			ok[id[b]][id[a]]=true;
		}
		int ans=0;
		vector<string> vec;
		REP(i,1<<n){
			int ct=0;
			bool no=false;
			vector<string>v;
			REP(j,n){
				if(!(i&(1<<j))) continue;
				ct++; v.pb(name[j]);
				for(int k=j+1;k<n;k++){
					if(!(i&(1<<k))) continue;
					if(ok[j][k]) no=true;
				}
			}
			if(!no){
				sort(ALL(v));
				if(ans<ct){
					ans=ct; vec=v;
				}
			}
		}
		cout<<ans<<endl;
		REP(i,vec.size()) cout<<vec[i]<<endl;
	}
	return 0;
}
