#include "stdio.h"
#include "stdlib.h"
#include "string.h"

typedef __int64 iint64;
typedef unsigned __int64 u_int64;
typedef unsigned int     u_int;
typedef u_int64  Type;

int main(int argc,char* argv[])
{
	if( argc <= 1)
		return printf("need file name as a  parameter!"); 
	FILE* pf = fopen(argv[1],"r");
	if( pf == NULL)
		return printf("cann't open file");
	
	u_int T = 0;
	u_int i=0,j=0;
	fscanf(pf,"%d\n",&T);

	for(i=0;i<T;i++)
	{
		Type R=0,k=0,N=0;
		fscanf(pf,"%I64d %I64d %I64d\n",&R,&k,&N);

		Type* groups = new Type[(u_int)N];
		for(j=0;j<(N-1);j++)
			fscanf(pf,"%I64d ",&groups[j]);
		fscanf(pf,"%I64d\n",&groups[N-1]);

		Type gsum  = 0;
		Type  sum  = 0;
		for(j=0;j<N;j++)
			gsum += groups[j];
		if( gsum <= k )
		{
			sum = gsum*R;
		}
		else
		{
			Type index  = 0;
			for(j=0;j<R;j++)
			{
				Type temp = 0;
				while( (temp+groups[index%N]) <= k )
				{
					temp += groups[index%N];
					index++;
				}
				sum += temp;
			}
		}
		printf("Case #%d: %I64d\n",i+1,sum);
		delete groups;
	}
	fclose(pf);
	return 0;
}