#include<stdio.h>
#include<algorithm>
using std::sort;
typedef long long ll;
long T,TT,n,l,i,j,k,c,m;
long a[1001];
long count[1001];
long cc[1001];
ll ans,f1,f2,sum,t;
inline bool cmp(const long &x,const long &y){
	return a[y]<a[x];
}
int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	for(scanf("%ld",&T),TT=0;TT<T;){
		scanf("%ld%I64d%ld%ld",&l,&t,&n,&c),ans=0;
		for(i=0;i<c;++i)
			scanf("%ld",a+i),count[i]=n/c+(i<n%c),cc[i]=i,ans+=(ll)count[i]*a[i]*2;
		sort(cc,cc+c,cmp);
		printf("Case #%ld: ",++TT),sum=0;
		for(i=0;i<n;++i) if(t<=sum+2*a[i%c]) break; else sum+=2*a[i%c],--count[i%c];
		if(i==n||!l){printf("%I64d\n",ans);continue;}
		f1=a[i%c]-(t-sum)/2,--count[i%c];
		for(k=l-1,j=0;j<c;++j){
			if(count[cc[j]]<k) k-=count[cc[j]],f1+=(ll)count[cc[j]]*a[cc[j]];
			else{
				f1+=k*a[cc[j]];
				break;
				}
			}
		f2=0;
		for(k=l,j=0;j<c;++j){
			if(count[cc[j]]<k) k-=count[cc[j]],f2+=(ll)count[cc[j]]*a[cc[j]];
			else{
				f2+=k*a[cc[j]];
				break;
				}
			}
		if(f1<f2) ans-=f2;
		else ans-=f1;
		printf("%I64d\n",ans);
		}
	scanf("%ld",&T);
	return 0;
}
