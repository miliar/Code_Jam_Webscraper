#include<iostream>
using namespace std;
#define N 1005
int arr[N][2];
int main(void)
{
	FILE*in=fopen("D:\\in.txt","r");
	FILE*out=fopen("D:\\out.txt","w");
	int test;
	fscanf(in,"%d",&test);
	for(int i=1;i<=test;i++)
	{
		int n; fscanf(in,"%d",&n);
		int j,k;
		for(j=0;j<n;j++)
		{
			fscanf(in,"%d%d",&arr[j][0],&arr[j][1]);
		}
		int ret=0;
		for(j=0;j<n;j++)
		{
			for(k=j+1;k<n;k++)
			{
				if((arr[j][0]>arr[k][0]&&arr[j][1]<arr[k][1])
					||(arr[j][0]<arr[k][0]&&arr[j][1]>arr[k][1]))
					ret++;
			}
		}
		fprintf(out,"Case #%d: %d\n",i,ret);
	}
	return 0;
}