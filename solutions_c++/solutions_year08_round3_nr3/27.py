#include<iostream>
#include<algorithm>
#include<set>
#include<map>
#define MD 1000000007
using namespace std;
long long a[10001],b[1000001],c[1000001],manow[1000001],sum,n;
set<long long> s;
map<long long,long long> mp;
void add(long long p,long long v){
	while(p<=n){
		manow[p]+=v;
		manow[p]%=MD;
		p += p&(-p);
	}
}
long long query(long long p){
	long long v=0ll;
	while(p>0){
		v+=manow[p];
		v%=MD;
		p -= p&(-p);
	}
	return v;
}
main(){
	long long m,tt,t,x,y,z,i,j;
	scanf("%lld",&t);
	for(tt=1;tt<=t;tt++){
		scanf("%lld",&n);
		scanf("%lld",&m);
		scanf("%lld",&x);
		scanf("%lld",&y);
		scanf("%lld",&z);
		sum = 0ll;
		for(i=0;i<m;i++){
			scanf("%lld",&a[i]);
		}
		for(i=0;i<n;i++){
			manow[i]=0ll;
		}
		s.clear();
		mp.clear();
		for(i=0;i<n;i++){
			b[i] = a[i % m];
			s.insert(b[i]);
			a[i % m] = (x * a[i % m] + y * (i + 1)) % z;
		}
		i=1;
		for(set<long long>::iterator u=s.begin();u!=s.end();u++){
			mp[*u]=i;
			i++;
		}
		for(i=0;i<n;i++){
			c[i]=1+query(mp[b[i]]-1);
			c[i]%=MD;
			add(mp[b[i]],c[i]);
			sum += c[i];
			sum %= MD;
		}
		printf("Case #%lld: %lld\n",tt,sum);
	}
	return 0;
}
