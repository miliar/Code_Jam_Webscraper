#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;
#define M 1000
long long num[M+10];
int next[M+5];
long long sum[M+5];
int used[M+5];

int main(){
	freopen("C-large.in","rb",stdin);
	freopen("C-large.out","wb",stdout);
	int ca,c=0;
	int i,j;
	int n,r,k;
	scanf("%d",&ca);
	while(ca--){
		c++;
		scanf("%d%d%d",&r,&k,&n);
		for(i=0;i<n;i++)
			scanf("%lld",&num[i]);

		memset(sum,0,sizeof(sum));
		for(i=0;i<n;i++){
			int d;
			for(j=0;j<n;j++){
				d=(i+j)%n;
				sum[i]+=num[d];
				if(sum[i]>k){
					sum[i]-=num[d];
					break;
				}
			}
			next[i]=(d%n);
		}

		int len=0;
		int klen=0;
		memset(used,0,sizeof(used));

		int d=0;
		while(!used[d]){
			used[d]=1;
			d=next[d];
		}

		int begin=d;
		long long rsum=0;
		memset(used,0,sizeof(used));
		while(!used[d]){
			len++;
			used[d]=1;
			rsum+=sum[d];
			d=next[d];
		}

		memset(used,0,sizeof(used));
		d=0;
		while(d!=begin){
			klen++;
			used[d]=1;
			d=next[d];
		}

		long long res=0;
		i=0;
		d=0;
		while(r!=0&&i<klen){
			r--;
			res+=sum[d];
			i++;
			d=next[d];
		}
		if(r==0){
			printf("Case #%d: %lld\n",c,res);
			continue;
		}

		long long p=(r/len);
		res+=p*rsum;
		r=r%len;
		d=begin;
		while(r!=0){
			res+=sum[d];
			r--;
			d=next[d];
		}
		printf("Case #%d: %lld\n",c,res);
	}
	return 0;
}