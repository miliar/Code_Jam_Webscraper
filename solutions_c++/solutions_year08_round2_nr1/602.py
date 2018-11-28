#include <iostream>
using namespace  std;
typedef struct  
{
	__int64 x,y;
}Info;

Info hash[100001];

FILE *fp1,*fp2;

int main()
{
	fp1=fopen("A.in","r");
	fp2=fopen("A.out","w");
	long T;
	fscanf(fp1,"%ld",&T);
	long f=1;
	while (T--)
	{
		__int64 n,A,B,C,D,x,y,M;
		fscanf(fp1,"%I64d %I64d %I64d %I64d %I64d %I64d %I64d %I64d",&n,&A,&B,&C,&D,&x,&y,&M);
		long i,j,k;
		__int64 X=x,Y=y;
		hash[0].x=X;
		hash[0].y=Y;
		for (i=1;i<n;++i)
		{
			X=( ( (A%M) * (X%M) ) % M + B%M )%M ;
			Y=( ( (C%M) * (Y%M) ) % M + D%M )%M  ;
			hash[i].x=X;
			hash[i].y=Y;
		}

		long count=0;

		for (i=0;i<n;++i)
		{
			for (j=i+1;j<n;++j)
			{
				for (k=j+1;k<n;++k)
				{
					if (
						  ((hash[i].x+hash[j].x+hash[k].x)%3==0)
					                        &&
						  ((hash[i].y+hash[j].y+hash[k].y)%3==0)
						)
					{
						++count;
					}
				}
			}
		}
		fprintf(fp2,"Case #%ld: %ld\n",f,count);
		++f;
	}
	fclose(fp1);
	fclose(fp2);
	return 0;
}