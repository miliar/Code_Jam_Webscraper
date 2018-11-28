#include<vector>
#include<cmath>
#include<map>
#include<cstdlib>
#include<iostream>
#include<sstream>
#include<string>
#include<algorithm>
#include<cstring>
#include<cstdio>
#include<set>
#include<stack>
#include<bitset>
#include<functional>
#include<cstdlib>
#include<ctime>
#include<queue>
#include<deque>
using namespace std;
#define pb push_back
typedef long long lint;
#define mp make_pair
#define fi first
#define se second
typedef pair<int,int> pint;
vector <pint> ka,cl;
int main()
{
	int i,t,k,j,a,b,n;vector <int> out;
	cin>>t;
	for(i=0;i<t;i++){
		cin>>n;ka=cl;
		for(j=0;j<n;j++){
			cin>>a>>b;ka.pb(mp(b,a));
		}
		for(j=0;;j++){
			sort(ka.begin(),ka.end());reverse(ka.begin(),ka.end());
//			cout<<ka[0].fi<<' '<<ka[0].se<<endl;
			if(ka[0].fi<2){out.pb(j);break;}
			ka[0].fi-=2;
			int f=0,t=ka[0].se;
			for(k=1;k<ka.size();k++){
				if(ka[k].se==t-1){ka[k].fi+=1;f=1;}
			}
			if(f==0) ka.pb(mp(1,t-1));
			f=0;
			for(k=1;k<ka.size();k++){
				if(ka[k].se==t+1){ka[k].fi+=1;f=1;}
			}
			if(f==0) ka.pb(mp(1,t+1));
		}
	}
	for(i=0;i<t;i++) cout<<"Case #"<<i+1<<": "<<out[i]<<endl;
	return 0;
}
