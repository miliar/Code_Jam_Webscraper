#include<cstdio>
long long a[10000],b[10000],sum[10000];
int main(){
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	long long i,j,r,k,time,n,s,t,tt=1;
	long long ans;
	scanf("%lld",&t);
	while(t--){
		scanf("%lld%lld%lld",&r,&k,&n);
		for(i=0;i<n;i++)scanf("%lld",&a[i]);
		i=0;
		b[0]=0;
		sum[0]=0;
		for(time=1;time<=2*n;time++){
			s=a[i];
			for(j=(i+1)%n;;j=(j+1)%n){
				s+=a[j];
				if(s>k)break;
				if(j==i)break;
			}
			s-=a[j];
			i=j;
			b[time]=i;
			sum[time]=sum[time-1]+s;
		}
		for(i=0;i<=2*n;i++){
			for(j=0;j<i;j++)
				if(b[j]==b[i])break;
			if(j!=i)break;
		}
		s=r%(i-j);
		if(s<i-j)s+=i-j;
		ans=((long long)sum[i]-sum[j])*(r-s)/(i-j)+sum[s];
		printf("Case #%lld: %lld\n",tt++,ans);
	}
	return 0;
}
