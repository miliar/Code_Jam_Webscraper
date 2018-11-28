#include <iostream>
using namespace std;
#define MAXN 1000

int main()
{
	freopen("C-large.in","rb",stdin);
	freopen("C-large.out","wb",stdout);

	int T,R,k,N,g[MAXN],next[MAXN],sum[MAXN],mark[MAXN];
	int i,j,tmp,round,r_first;
	long long ans,sum_tmp[MAXN+2],r_sum;

	scanf("%d",&T);
	for (int p=1;p<=T;p++)
	{
		scanf("%d%d%d",&R,&k,&N);
		for (i=0;i<N;i++)
			scanf("%d",g+i);
		
		tmp=0;
		for (j=0;j<N;j++)
		{
			if (tmp<=k-g[j])
				tmp+=g[j];
			else
				break;
		}
		next[0]=j%N;
		sum[0]=tmp;

		for (i=1;i<N;i++)
		{

			j=next[i-1];
			tmp=sum[i-1]-g[i-1];
			if (tmp==0)
			{
				tmp=g[j%N];
				j++;
			}
			for (;j!=i;j++)
			{
				if (tmp<=k-g[j%N])
					tmp+=g[j%N];
				else
					break;
			}
			next[i]=j%N;
			sum[i]=tmp;
		}

		memset(mark,-1,sizeof(mark));
		memset(sum_tmp,0,sizeof(sum_tmp));
		i=1;
		j=0;
		sum_tmp[1]=sum[0];
		while (mark[j]==-1)
		{
			mark[j]=i++;
			j=next[j];
			sum_tmp[i]=sum_tmp[i-1]+sum[j];
		}
		r_first=mark[j];
		round=i-r_first;
		r_sum=sum_tmp[i]-sum_tmp[r_first];

		if (R>r_first)
		{
			ans=(R-r_first)/round;
			ans=ans*r_sum+sum_tmp[r_first];
			R=(R-r_first)%round;
			ans+=sum_tmp[r_first+R]-sum_tmp[r_first];
		}
		else
			ans=sum_tmp[R];

		printf("Case #%d: %lld\n",p,ans);

	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}