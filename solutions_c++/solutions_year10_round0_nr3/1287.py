#include<iostream>
#include<cmath>
#include<string>
#include<cstring>
#include<algorithm>
#include<cstdio>
using namespace std;

int gcd(int a,int b){
	if(b==0)return a;
	return gcd(b,a%b);
}
typedef long long LL;
const int MAXN=1005;
struct da{
	LL beg,end,sum;
};
da pm[MAXN];
int main(){

	LL y,n,i,j,m,r,k,t,num[MAXN],s;
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	scanf("%lld",&t);
	for(s=1;s<=t;s++){
		scanf("%lld%lld%lld",&r,&k,&n);
		for(j=0;j<n;j++)
			scanf("%lld",&num[j]);		
		for(i=0;i<n;i++){
			pm[i].sum=0;
			pm[i].beg=i;
			for(j=i;j-i<n;j++){
				if(pm[i].sum+num[j%n]>k)break;
				pm[i].sum+=num[j%n];
			}
			pm[i].end=j%n;
		}
		LL p=0;
		LL sum=0;
		bool v=0;
		for(i=0;i<r;i++){
			if(p==0&&v)
				break;	
			sum+=pm[p].sum;
			if(p==0)
				v=1;
			p=pm[p].end;
		}
		sum=(r/i)*sum;
		for(j=0;j<r%i;j++)
		{
			sum+=pm[p].sum;
			p=pm[p].end;
		}
		printf("Case #%lld: %lld\n",s,sum);
	}
	return 0;
}