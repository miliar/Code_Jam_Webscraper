//BISMILLAHIRRAHMANIRRAHIM


#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <set>
using namespace std;
#define pii pair < long long , long long >

map < pii , long long > dp;
map < pii , long long > ::iterator it;

long long dfs(const long long l,const long long p,long long c) {
	if((l*c)>=p) return 0;
	it=dp.find( pii ( l,p));
	if(it!=dp.end()) return it->second;
	long long i=c,q=p-l,t;
	while((p/i+((p%i)?1:0))>l) {
		//tm=dfs(l,(p/i+((p%i)?1:0)),c);
		//t=max(tm,j)+1;
		t=max(dfs(l,(p/i+((p%i)?1:0)),c),dfs((p/i+((p%i)?1:0)),p,c))+1;
		if(t<q) q=t;
		i*=c;
		//cout<<i<<' '<<j<<' '<<(p/i+((p%i)?1:0))<<'\n';
	}
	//if(q>=1000000000) return 0;
	return dp[pii(l,p)]=q;
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T,I,l,p,c;
	//cout<<dfs(1,1000,2)<<'\n';
	cin>>T;
	for(I=1;I<=T;I++) {
		cin>>l>>p>>c;
		dp.clear();
		printf("Case #%d: %Ld\n",I,dfs(l,p,c));
	}
	return 0;
}
