#include <cstdio>
#include <cstring>
#include <iostream>

using namespace std;

struct bigint{
	int a[60],len;
	bigint(int x=0):len(1){
		memset(a,0,sizeof(a));
		a[len]=x;
	}
	bigint(const bigint &b){
		memcpy(a,b.a,sizeof(a));
		len=b.len;
	}
	bool iszero() const{
		return len==1&&a[1]==0;
	}
	void input(){
		char s[60];
		scanf(" %s",s);
		int i,l=strlen(s);
		memset(a,0,sizeof(a));
		for (i=0;i<l;i++)
			a[l-i]=s[i]-'0';
		len=l;
	}
	void output() const{
		for (int i=len;i>=1;i--)
			printf("%d",a[i]);
		puts("");
	}
};
bool operator<(const bigint &a,const bigint &b){
	if (a.len!=b.len) return a.len<b.len;
	for (int i=a.len;i>=1;i--)
		if (a.a[i]!=b.a[i]) return a.a[i]<b.a[i];
	return false;
}
bigint operator-(const bigint &a,const bigint &b){
	bigint ret(a);
	for (int i=1;i<=ret.len;i++){
		ret.a[i]-=b.a[i];
		if (ret.a[i]<0){
			ret.a[i]+=10;
			ret.a[i+1]--;
		}
	}
	while (ret.len>1&&ret.a[ret.len]==0)
		ret.len--;
	return ret;
}
bigint operator%(const bigint &a,const bigint &b){
	bigint ret(a);
	int i,l=a.len-b.len;
	for (;l>=0;){
		for (i=b.len+1;i>=1;i--)
			if (ret.a[i+l]!=b.a[i]) break;
		if (ret.a[i+l]>=b.a[i])
			for (i=1;i<=b.len;i++){
				ret.a[i+l]-=b.a[i];
				if (ret.a[i+l]<0){
					ret.a[i+l]+=10;
					ret.a[i+l+1]--;
				}
			}
		else l--;
	}
	while (ret.len>1&&ret.a[ret.len]==0)
		ret.len--;
	return ret;
}

bigint ans,a[1010],b[1010],g;

bigint gcd(bigint a,bigint b){
	bigint t;
	while (!b.iszero()){
		t=a%b;
		a=b;
		b=t;
	}
	return a;
}

int main(){
	int T,cas,i,n;
	scanf("%d",&T);
	for (cas=1;cas<=T;cas++){
		scanf("%d",&n);
		for (i=1;i<=n;i++)
			a[i].input();
		for (i=1;i<n;i++)
			if (a[i]<a[i+1])
				b[i]=a[i+1]-a[i];
			else b[i]=a[i]-a[i+1];
		g=b[1];
		for (i=2;i<n;i++)
			g=gcd(g,b[i]);
		if (g.iszero())
			ans=0;
		else{
			ans=a[1]%g;
			if (!ans.iszero())
				ans=g-ans;
		}
		printf("Case #%d: ",cas);
		ans.output();
	}
	return 0;
}
