#include<iostream>
#include<vector>

#define INF 100000

using namespace std;

int main()
{
	int T,caseNo=1;
	scanf("%d\n",&T);
	while(T--)
	{
		printf("Case #%d: ",caseNo);
		caseNo++;

		int engine,query;

		scanf("%d\n",&engine);
		vector<string> engineNames(engine);
		for(int i=0;i<engine;i++)
			getline(cin,engineNames[i]);
		
		scanf("%d\n",&query);
		if(query < 1)
		{
			printf("0\n");
			continue;
		}
		string q;
		int matrix[engine][query];

		getline(cin,q);
		for(int i=0;i<engine;i++)
			if(engineNames[i]==q) matrix[i][0] = INF;
			else matrix[i][0] = 0;

		for(int i=1;i<query;i++)
		{
			getline(cin,q);
			for(int j=0;j<engine;j++)
			{
				if(q==engineNames[j]) matrix[j][i] = INF;
				else 
				{
					matrix[j][i] = INF;
					for(int k=0;k<engine;k++)
						if( matrix[k][i-1]+(j!=k) < matrix[j][i] )
							matrix[j][i] = matrix[k][i-1]+(j!=k);
				}
			}
		}

		int min=INF;
		for(int i=0;i<engine;i++)
		{
			if(matrix[i][query-1] < min)
				min = matrix[i][query-1];
		}
		printf("%d\n",min);
	}
	return 0;
}
