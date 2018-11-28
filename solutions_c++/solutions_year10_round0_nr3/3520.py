#include <cstdio>
#include <sstream>
using namespace std;

int main()
{
	freopen("C:\\google\\2010QR\\Theme Park\\C-small-attempt1.in", "rt", stdin);
	freopen("C:\\google\\2010QR\\Theme Park\\C-small-attempt1.out", "wt", stdout);
	int i,j,i0,i1,i2,i3,i4,i5,R[50],K[50],N[50],G[50][10],G1[10],T;
	long out[50],sum;
    scanf("%d",&T);
	for(i=0;i<T;i++)
	{
	scanf("%d%d%d",&R[i],&K[i],&N[i]);
	for(j=0;j<N[i];j++)
	scanf("%d",&G[i][j]);
	out[i]=0;
	}
	for(i0=0;i0<T;i0++)
	{
		for(i1=0;i1<R[i0];i1++)
		{
			sum=G[i0][0];
			for(i2=1;i2<N[i0];i2++)
			{
			  if((sum+G[i0][i2])<=K[i0])
			  {
				  sum+=G[i0][i2];
				  if(i2==N[i0]-1)
				  {
					out[i0]+=sum;
					break;
				  }
			  }
			  else 
			  {
				  out[i0]+=sum;
				  for(i3=0;i3<i2;i3++)
					  G1[i3]=G[i0][i3];
				  for(i4=i2,i5=0;i4<N[i0];i4++,i5++)
					  G[i0][i5]=G[i0][i4];
				  for(i3=0;i3<i2;i3++,i5++)
					  G[i0][i5]=G1[i3];
				  break;
			  }
			}
			if(N[i0]==1)
				out[i0]+=sum;
			sum=0;
		}
	}

	for(i=0;i<T;i++)
	{
		printf("Case #%d: %ld\n",i+1,out[i]);
	}
	return 0;
}