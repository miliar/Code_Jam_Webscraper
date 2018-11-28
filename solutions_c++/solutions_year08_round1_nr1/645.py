#include<iostream>
using namespace std;
#include<stdlib.h>
int cmp(const void *a,const void *b)
{
	return *(int *) a - *(int *)b;
}
int cmp1(const void *a,const void *b)
{
	return *(int *) b - *(int *)a;
}
int A[10001];
int B[10001];
int main()
{
    int i,t,j,w = 0,n;
	__int64 res;
	FILE *fp,*fout;
	fp = fopen("t.in","r");
	fout = fopen("out.in","w");
	fscanf(fp,"%d",&t);
//	scanf("%d",&t);
	while(t--)
	{
		w ++;
		res = 0;
		fscanf(fp,"%d",&n);
	//	scanf("%d",&n);
		for(i = 0; i < n; i++)
		{
			fscanf(fp,"%d",&A[i]);
		//	scanf("%d",&A[i]);
		}
		for(i = 0; i < n; i++)
		{
			fscanf(fp,"%d",&B[i]);
		//	scanf("%d",&B[i]);
		}
		qsort(A,n,sizeof(A[0]),cmp1);
		qsort(B,n,sizeof(B[0]),cmp);
		for(i = 0; i< n; i++)
			res += A[i]*B[i];
	//	printf("Case #%d: ",w);
	//	printf("%I64d\n",res);
		fprintf(fout,"Case #%d: ",w);
		fprintf(fout,"%I64d\n",res);
	}

}