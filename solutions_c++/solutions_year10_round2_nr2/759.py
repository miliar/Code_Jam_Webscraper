#include<vector>
#include<algorithm>
#include<string>
#include<set>
#include <stdio.h>
#include <iostream.h>
using namespace std;

#define FOR(i,n) for (int i=0; i<(int)(n); i++)
#define D "%d"


void main()
{
	FILE *fp = fopen("B-large.in.txt","r");
	FILE *fp2 = fopen("B-large.out.txt","w");

	if(!fp)
	{
		printf("cannot open file\n");
		exit(0);
	}
	int testNum;
	fscanf(fp,"%d",&testNum);
	for(int testID=1;testID<=testNum;testID++)
	{
		int N,K,B,T;
		int x[50]={0},v[50]={0};
		double t[50]={0};
		int gotNum=0,notgotNum=0,swapNum=0;
		fscanf(fp,"%d",&N);
		fscanf(fp,"%d",&K);
		fscanf(fp,"%d",&B);
		fscanf(fp,"%d",&T);
		for(int i=0;i<N;i++)
		{
			fscanf(fp,"%d",&x[i]);
//			printf("%d ",x[i]);
		}
//		printf("\n");
		for(i=0;i<N;i++)
		{
			fscanf(fp,"%d",&v[i]);
//			printf("%d ",v[i]);
		}
//		printf("\n");
		for(i=0;i<N;i++)
		{
			t[i] = ((double)B - (double)x[i])/(double)v[i];
		}
		for(i=N-1;i>=0;i--)
		{
			if(t[i] <= T)
			{
				swapNum = swapNum + notgotNum;
				gotNum++;
				if(gotNum==K)
					break;
			}
			else
				notgotNum++;
		}
		if(gotNum == K)
			fprintf(fp2,"Case #%d: %d",testID,swapNum);
		else
			fprintf(fp2,"Case #%d: IMPOSSIBLE",testID);
		if(testID!=testNum)
			fprintf(fp2,"\n");
	}
	fclose(fp);
	fclose(fp2);
	
}