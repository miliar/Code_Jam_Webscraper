#include <stdio.h>
#include <string.h>

typedef __int64 int64;

const int maxn=1024 * 2;
int R,K,N;
int64 a[maxn];
int b[maxn];
int64 c[maxn];

int find(int sp, int64 count)
{
	int left=sp;
	int right=sp+N-1;
	int mid;
	while(left<right)
	{
		mid=(left+right+1)/2;
		if(a[mid]-a[sp-1]<=count){
			left=mid;
		}else{
			right=mid-1;
		}
	}
	if(left>N) return left-N;
	else return left;
}

int64 solve()
{
	int i,tmp,next;
	int sp=1;
	memset(b,-1,sizeof(b));
	b[1]=0;
	c[1]=0;
	int64 ret=0,count;
	
	for(i=1;i<=R;i++){
		next=find(sp,K);
		if(next<sp)count=a[next+N]-a[sp-1];
		else count=a[next]-a[sp-1];
		sp=next+1;
		if(sp>N) sp=1;
		ret+=count;
		if(b[sp]>=0){
			tmp=(R-i)/(i-b[sp]);
			ret+=(ret-c[sp])*tmp;
			i+=tmp*(i-b[sp]);
			memset(b,0,sizeof(b));
		}else{
			b[sp]=i;
			c[sp]=ret;
		}
	}
	return ret;
}

int main()
{
	freopen("C-large.in.txt","r",stdin);
	freopen("c.out","w",stdout);
	int i,j,T;
	scanf("%d",&T);
	for(i=1;i<=T;i++)
	{
		scanf("%d%d%d",&R,&K,&N);
		a[0]=0;
		for(j=1;j<=N;j++){
			scanf("%I64d",&a[j]);
			a[j]+=a[j-1];
		}
		for(;j<=N+N;j++){
			a[j]=a[j-1]+(a[j-N]-a[j-N-1]);
		}
		printf("Case #%d: ",i);
		printf("%I64d\n",solve());
	}
	return 0;
}