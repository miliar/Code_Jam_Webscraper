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
#include<complex>
using namespace std;
#define pb push_back
#define pf push_front
typedef long long lint;
typedef complex<double> pt;
#define mp make_pair
#define fi first
#define se second
typedef pair<int,int> pint;
#define All(s) s.begin(),s.end()
#define rAll(s) s.rbegin(),s.rend()
#define REP(i,a,b) for(i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)
int de[40],in[40],out[40];
bool gr[40][40];
int main()
{
	int i,n,j,k,l,t;string s;
	memset(de,0,sizeof(de));
	cin>>t;
	de[14]=26;de[8]=27;de[4]=29;de[0]=30;de[18]=31;de[19]=33;de[1]=34;de[6]=35;
	rep(i,t){
		cin>>n;cin>>s;int ret=0,rest=0;
		memset(gr,false,sizeof(gr));
		memset(in,0,sizeof(in));memset(out,0,sizeof(out));
		rep(j,s.size()-1){
			int a=s[j]-'a',b=s[j+1]-'a';
			vector <int> c,d;c.pb(a);d.pb(b);
			if(de[a]>0) c.pb(de[a]);if(de[b]>0) d.pb(de[b]);
			rep(k,c.size()) rep(l,d.size()){
				gr[c[k]][d[l]]=true;
				//cout<<c[k]<<' '<<d[l]<<endl;
			}
		}
		rep(j,36) rep(k,36){
			if(gr[k][j]){in[k]++;out[j]++;}
		}
		rep(j,36){
			ret+=in[j];rest+=max(0,in[j]-out[j]);
		}
		if(rest>1) ret+=rest-1;
		printf("Case #%d: %d\n",i+1,ret+1);
	}
	return 0;
}
