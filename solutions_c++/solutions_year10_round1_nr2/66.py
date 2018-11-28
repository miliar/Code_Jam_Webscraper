#include<iostream>

#include<fstream>


using namespace std;

ifstream in("B.in");
ofstream out("B.out");
const int MAX = 1000000;
int D,I,M,N;

int value[108];

int cost[108][256];

int diff(int a,int b)
{
	if(a<b)
		return b-a;
	return a-b;
}

int insertCost(int a, int b)
{
	int d = diff(a,b);
	if(d<=M) return 0;
	if(M==0)
		return MAX;
	return ((d-1)/M)*I;
}
int main()
{
	int T;
	in>>T;

	
	for(int c=0;c<T;c++)
	{
		in>>D>>I>>M>>N;
		for(int i=1;i<=N;i++)
			in>>value[i];

		memset(cost,0,sizeof(cost));

		for(int i=1;i<108;i++)
			for(int j=0;j<256;j++)
				cost[i][j]=300;

		for(int i=1;i<=N;i++)
		{
			for(int j=0;j<256;j++)
			{
				int minCost = MAX;
				
				for(int last=0;last<256;last++)
				{
					int preCost=cost[i-1][last];

					if(value[i]==j)
					{
						//insert to make it legal
						minCost = min(minCost, preCost + insertCost(last,j));
					}
					else
					{
						//modify, then insesrt to make it legal
						minCost = min(minCost, preCost + insertCost(last,j) + diff(value[i],j));

						//if last==j, consider direct delete
						if(last==j)
							minCost = min(minCost, preCost+D);

						minCost = min(minCost, preCost+D+I+ insertCost(last,j));

						//delete, insert, make it legal

						//insert, make it legal
						minCost = min(minCost, preCost+insertCost(last,value[i]) + I + insertCost(value[i],j));
					}


				}

				cost[i][j] = minCost;
			}
		}

		int res = cost[N][0];
		for(int i=0;i<256;i++)
			res = min(res,cost[N][i]);



	

		cout<<"Case #"<<c+1<<": "<<res<<endl;
		out<<"Case #"<<c+1<<": "<<res<<endl;
	}
		
	return 0;
}