#include<vector>
#include<algorithm>
#include<string>
#include <stdio.h>
#include <iostream.h>
using namespace std;

#define FOR(i,n) for (int i=0; i<(int)(n); i++)
#define D "%d"


void main()
{
//	vector <int> a;
//	vector<int>::iterator   it;
	FILE *fp = fopen("A-large.in.txt","r");
	FILE *fp2 = fopen("A-large.out.txt","w");

	if(!fp)
	{
		printf("cannot open file\n");
		exit(0);
	}
	int testNum;
	fscanf(fp,"%d",&testNum);
	for(int testID=1;testID<=testNum;testID++)
	{
		int N,A[1000],B[1000];
		fscanf(fp,"%d",&N);
		int num=0;
		for(int i=0;i<N;i++)
		{
			fscanf(fp,"%d",&A[i]);
//			printf("%d ",A[i]);
			fscanf(fp,"%d",&B[i]);
//			printf("%d ",B[i]);
		}
//		printf("\n");
		for(i=0;i<N;i++)
		{
//			printf("%d ",A[i]);
			for(int j=0;j<N;j++)
			{
				if(A[i]<A[j] && B[i] > B[j])
					num++;
			}
		}
		fprintf(fp2,"Case #%d: %d",testID,num);
		if(testID!=testNum)
			fprintf(fp2,"\n");
	}
	fclose(fp);
	fclose(fp2);
	
}