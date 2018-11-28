#include<cstdio>
#include<vector>

using namespace std;

vector<int> pointA,pointB;

int main()
{
	int A,B,count,i,j,k,N,T;
	scanf("%d",&T);
	for(i=1;i<=T;i++)
	{
		scanf("%d",&N);
		for(j=0;j<N;j++)
		{
			scanf("%d %d",&A,&B);
			pointA.push_back(A);
			pointB.push_back(B);
		}
		count=0;
		for(j=0;j<N;j++)
		{
			for(k=j;k<N;k++)
			{
				if(((pointA[j]<pointA[k]) && (pointB[j]>pointB[k])) || ((pointA[j]>pointA[k]) && (pointB[j]<pointB[k])))
						count++;
			}
		}
		printf("Case #%d: %d\n",i,count);
		pointA.clear();
		pointB.clear();
	}
	return 0;
}