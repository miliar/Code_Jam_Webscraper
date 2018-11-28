#include<iostream>
#include<fstream>
using namespace std;
bool FloydAlgo(int numNodes, int** path);
bool isExchange(int a, int b);
int main()
{
   ifstream ipfile1;
   int numCases;
   int numNodes;
   int** edges;
   ipfile1.open("input.txt");
   ipfile1>>numCases;
   for (int i=0; i<numCases; i++)
   {
	ipfile1>>numNodes;
	edges = new int*[numNodes];
	for (int j=0; j<numNodes; j++)
	{
		edges[j] = new int[numNodes];
	}
	for (int j=0; j<numNodes; j++)
	{
		for (int k=0; k<numNodes; k++)
		{
			edges[j][k] = 1000000;
		}
	}
	for (int j=0; j<numNodes; j++)
	{
		int numEdges;
		ipfile1>>numEdges;
		for (int k=0; k<numEdges; k++)
		{
			int l;
			ipfile1>>l;
			edges[j][l-1]  = 1;
		}
	}
	if (FloydAlgo(numNodes, edges))
	{
		cout<<"Case #"<<i<<": Yes"<<endl;
	}
	else
	{
		cout<<"Case #"<<i<<": No"<<endl;
	}
   }
}


bool FloydAlgo(int numNodes, int** path)
{
	for (int k=0; k<numNodes; k++)
	{
		for (int i=0; i<numNodes; i++)
		{
			for (int j=0; j<numNodes; j++)
			{
				if (i!=k && j!=k)
				{
					if (isExchange(path[i][j], path[i][k]+path[k][j]))
					{
						return true;
					}
					else
					{
						path[i][j] = min(path[i][j], path[i][k]+path[k][j]);
					}
				}
			}
		}
	}
	return false;
}



bool isExchange(int a, int b)
{

   if (a >= 1000000 )
	return false;

   if (b>=1000000)
	return false;

   if (a<=b)
	return true;
   if (a>b)
	return true;
}
