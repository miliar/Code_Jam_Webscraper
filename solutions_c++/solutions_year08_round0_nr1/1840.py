#include<cstdio>
#include<iostream>
#include<string>
#include<map>

using namespace std;

int arr[105][1005];

int main()
{
	int t;
	scanf("%d",&t);
	for(int T=0;T<t;T++)
	{
		int S,Q,que[1005];
		char inp[105];
		map<string,int> SE;
		scanf("%d",&S);
		for(int i=0;i<S;i++)
		{
			scanf(" %[^\n]",inp);
			string eng(inp);
//			cout << eng << endl;
			SE[eng] = i;
		}
		scanf("%d",&Q);
		for(int i=0;i<Q;i++)
		{
			scanf(" %[^\n]",inp);
			string eng(inp);
//			cout << eng << endl;
			que[i] = SE[eng];
		}
		memset(arr,0,sizeof(arr));
		for(int i=0;i<Q;i++)
		{
			for(int j=0;j<S;j++)
			{
				if(j==que[i])
				{
					arr[i+1][j+1]=-1;
					continue;
				}
				arr[i+1][j+1]=INT_MAX-10000;
				for(int k=0;k<S;k++)
					if(k!=j)
					{
						if(arr[i][k+1]!=-1 && arr[i+1][j+1]>arr[i][k+1]+1)
							arr[i+1][j+1] = arr[i][k+1]+1;
					}
					else if(arr[i][k+1]!=-1 && arr[i+1][j+1]>arr[i][k+1])
						arr[i+1][j+1] = arr[i][k+1];
//				printf("%d %d\n",i+1,j+1);
//				for(int k=0;k<Q+1;k++,printf("\n"))
//					for(int j=0;j<S+1;j++)
//						printf("%d ",arr[k][j]);
//				int x;
//				cin >> x;
			}
		}
		int max=INT_MAX;
		for(int i=0;i<S;i++)
			if(max>arr[Q][i+1] && arr[Q][i+1]!=-1)
				max = arr[Q][i+1];
			else if(max==0)
				break;
		printf("Case #%d: %d\n",T+1,max);
	}
	return 0;
}
