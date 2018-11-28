#include "stdio.h"
#include "stdlib.h"

typedef __int64 int64;
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
	Type T = 0;
	fscanf(pf,"%d\n",&T);
	for(Type i=0;i<T;i++)
	{
		Type N=0,K=0;
		Type P=1;
		fscanf(pf,"%d %d\n",&N,&K);
		
		P    = P<<N;
		K    = K%P;
		if( K == P-1 )
			printf("Case #%d: ON\n",i+1);
		else
			printf("Case #%d: OFF\n",i+1);
	}
	fclose(pf);
	return 0;
}