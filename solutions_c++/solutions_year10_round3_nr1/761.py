#include "stdio.h"
#include "stdlib.h" 
#include "math.h"
#include "string.h"

#define  nmax 1000+5

int node[2][nmax];
int nt[2][nmax];

int swap(int* x,int i,int j)
{
	int t;
	t=x[i];
	x[i]=x[j];
	x[j]=t;
	return 1;
}
int qsort(int* x,int low,int high)
{
	int t;
	int m;

	if(low<high)
	{
		//swap(x,low,randint(low,high));
		t=x[low];
		m=low;
		for(int i=low+1;i<=high;i++)
		{
			if(x[i]<t)swap(x,++m,i);
		}
		swap(x,low,m);
		qsort(x,low,m-1);
		qsort(x,m+1,high);
	}
	return 1;
}

int main()
{
	FILE* f;
	f=fopen("A-small-attempt0.in","r");
	//f=fopen("A-small.in","r");
	if(f==NULL)
	{
		printf("file read error£¡");
		exit(1); 
	}

	FILE *w;
	w=fopen("A-large.out","w");
	//w=fopen("A-small.out","w");
	if (w==NULL)
	{
		printf("file write error£¡");
		exit(1); 
	}
	int count=0;
	int n;
	int k;

	fscanf(f,"%d",&count);

// 	int temp=1;
// 	int num;
// 	int rsign;
// 	int bsign;
// 	char tem;
// 	int nowpos;

	for (int i=0;i<count;i++)
	{
		fscanf(f,"%d",&n);
		for (int j=0;j<n;j++)
		{
			fscanf(f,"%d",&node[0][j]);
			fscanf(f,"%d",&node[1][j]);

			//nt[0][j]=node[0][j];
			//nt[1][j]=node[1][j];
		}
		
		int sign=0;
		for (int j=0;j<n;j++)
		{
			for (int z=0;z<=j;z++)
		{
			nt[0][z]=node[0][z];
			nt[1][z]=node[1][z];
		}
			int k=0;
			int s=0;
			qsort(nt[0],0,j);
			qsort(nt[1],0,j);
			for (k=0;k<j;k++)
			{
				if (node[0][j]<=nt[0][k])break;
			}
			for (s=0;s<j;s++)
			{
				if (node[1][j]<=nt[1][s])break;
			}
			sign+=abs(k-s);
			
		}

		fprintf(w,"Case #%d: ",i+1);
		fprintf(w,"%d",sign);
		fprintf(w,"\n");
	}
	fclose(f);
	fclose(w);

}
