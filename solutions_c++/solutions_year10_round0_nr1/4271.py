#include <cstdio>
#include <sstream>
using namespace std;

int main()
{
	freopen("C:\\google\\2010QR\\Snapper Chain\\A-small-attempt4.in", "rt", stdin);
	freopen("C:\\google\\2010QR\\Snapper Chain\\A-small-attempt4.out", "wt", stdout);
    unsigned int T,N[10000],out[10000],i,i0,i1,i2,i3,i4,i5,c=0,c1=0;
    long K[10000],A[100][30];
	scanf("%d",&T);
	for(i=0;i<T;i++)
	{
	scanf("%d%ld",&N[i],&K[i]);
	out[i]=0;
	}
	for(i0=0;i0<T;i0++)
	{
		if(K[i0]==0)
			out[i0]=0;
		else 
		{
			A[0][0]=1;
			for(i3=1;i3<N[i0];i3++)
				A[0][i3]=0;
			for(i1=1;i1<K[i0];i1++)
			{
				if(A[i1-1][0]==1)
					A[i1][0]=0;
				else A[i1][0]=1;
				for(i2=1;i2<N[i0];i2++)
				{
					for(i4=0;i4<i2;i4++)
					{
						if(A[i1-1][i4]==1)
							c++;
					}
					if(c==i2)
					{
						if(A[i1-1][i2]==1)
					      A[i1][i2]=0;
				        else A[i1][i2]=1;
					}
					else A[i1][i2]=A[i1-1][i2];
					c=0;
				}
			}
			for(i5=0;i5<N[i0];i5++)
			{
				if(A[K[i0]-1][i5]==1)
					c1++;
			}
			if(c1==N[i0])
				out[i0]=1;
			else out[i0]=0;
			c1=0;
		}
			
	}
	for(i=0;i<T;i++)
	{
		printf("Case #%d:",i+1);
		if(out[i]==0)
	        printf(" OFF");
		else 
			printf(" ON");
        printf("\n"); 
	}
	return 0;
}