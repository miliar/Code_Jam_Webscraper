#include "stdio.h"
#include "stdlib.h"
#include "string.h"

typedef __int64 int64;
typedef unsigned __int64 u_int64;
typedef unsigned int     u_int;
typedef u_int64  Type;
typedef unsigned char u_char;


int main(int argc,char* argv[])
{
	if( argc <= 1)
		return printf("need file name as a  parameter!"); 
	FILE* pf = fopen(argv[1],"r");
	if( pf == NULL)
		return printf("cann't open file");
	
	u_int C = 0;
	fscanf(pf,"%d\n",&C);
	
	int i=0,j=0,r=0,k=0;
	for(i=0;i<C;i++)
	{
		Type N,K,B,T;
		fscanf(pf,"%I64d %I64d %I64d %I64d\n",&N,&K,&B,&T);

		Type* pi = new Type[N];
		Type* vi = new Type[N];

		for(j=0;j<(N-1);j++)
			fscanf(pf,"%I64d ",&pi[j]);
		fscanf(pf,"%I64d\n",&pi[N-1]);

		for(j=0;j<(N-1);j++)
			fscanf(pf,"%I64d ",&vi[j]);
		fscanf(pf,"%I64d\n",&vi[N-1]);

		for(j=0;j<N;j++)
		{
			vi[j] = pi[j] + vi[j]*T;
		}

		int mark   = 0;
		Type sum_v = 0;
		Type sum_k = 0;

		for(j=N-1;j>=0;j--)
		{
			if( vi[j] >= B)
			{
				sum_k += 1;
				if( sum_k >= K)
				{
					mark = j;
					break;
				}
			}
		}
		for(j=N-1;j>=mark;j--)
		{
			if( vi[j] < B)
			{
				for(r=mark;r<j;r++)
					if(vi[r] >= B)
						sum_v++;
			}
		}

		if( sum_k >= K)
		{
			printf("Case #%d: %u\n",i+1,sum_v);
		}
		else
			printf("Case #%d: IMPOSSIBLE\n",i+1);

		delete vi;
		delete pi;
	}
	
	fclose(pf);
	return 0;
}
