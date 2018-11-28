#include "stdio.h"
#include "stdlib.h"
#include "string.h"

typedef __int64 int64;
typedef unsigned __int64 u_int64;
typedef unsigned int     u_int;
typedef u_int64  Type;
typedef unsigned char u_char;

typedef struct
{
	int Ai;
	int Bi;
}Point;

u_int getIntranet(Point* points,int len);

int main(int argc,char* argv[])
{
	if( argc <= 1)
		return printf("need file name as a  parameter!"); 
	FILE* pf = fopen(argv[1],"r");
	if( pf == NULL)
		return printf("cann't open file");
	
	u_int T = 0;
	fscanf(pf,"%d\n",&T);
	
	int i=0,j=0,r=0,k=0;
	for(i=0;i<T;i++)
	{
		u_int N;
		fscanf(pf,"%d\n",&N);

		Point* points = new Point[N];
		for(j=0;j<N;j++)
			fscanf(pf,"%d %d\n",&(points[j].Ai),&(points[j].Bi));

		u_int intranets = 0;
		if( N>=2 )
			intranets = getIntranet(points,N);

		printf("Case #%d: %u\n",i+1,intranets);

		delete points;
	}
	
	fclose(pf);
	return 0;
}


u_int getIntranet(Point* points,int len)
{
	u_int sum = 0;
	for(int j=0;j<len;j++)
		for(int i=j+1;i<len;i++)
			if( ((points[j].Ai-points[i].Ai)>0) ^ ((points[j].Bi-points[i].Bi)>0 ) )
				sum++;
	return sum;
}