#include <vector>
#include <string>
#include <stdlib.h>
#include <math.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <sstream>
#include <map>
#include <ctime>
#include <cassert>

using namespace std;

ofstream fout("../../output.txt");
ifstream fin("../../input.txt");


int adj[36][36];
int dists[36][36];

int currat[36];

int threats[36];

int n;

int dfs(int vx, int dep)
{
	if(dists[vx][1]==1)
	{
		//we are done - let's have a check
		int i,j;
		
		for(i=0; i<n; i++)
			threats[i]=0;
		threats[0]=1;
		
		for(i=0; i<=dep; i++)
		{
			for(j=0; j<n; j++)
			{
				if(adj[currat[i]][j]==1)
					threats[j]=1;
			}
		}
		int tot = 0;
		for(i=0; i<n; i++)
		{
			tot+=threats[i];
		}
		return tot;
	}
	int ans = 0;
	for(int i=0; i<n; i++)
	{
		if(adj[vx][i]==1 && dists[i][1]<dists[vx][1])
		{
			currat[dep+1]=i;
			int j = dfs(i,dep+1);
			if(j>ans)
				ans=j;
		}
	}
	return ans;
}
		

int main(void)
{
	int ttt;
	fin >> ttt;
	int ct = 0;
	string s;
	
	while(ttt>0)
	{
		ct++;
		ttt--;
		int i,j,k;
		
		fin >> n >> k;
		
		memset(adj,0,sizeof(adj));
		for(i=0; i<n; i++)
		{
			for(j=0; j<n; j++)
			{
				if(i!=j)
				{
					dists[i][j]=1000;
				}
				else {
					dists[i][j]=0;
				}
			}
		}
		
		char c;
		int a,b;
		
		for(i=0; i<k; i++)
		{
			fin >> a >> c >> b;
			adj[a][b]=adj[b][a]=1;
			dists[a][b]=dists[b][a]=1;
		}
		
		for(k=0; k<n; k++)
		{
			for(i=0; i<n; i++)
			{
				for(j=0; j<n; j++)
				{
					if(dists[i][k]+dists[k][j] < dists[i][j])
					{
						dists[i][j]=dists[i][k]+dists[k][j];
					}
				}
			}
		}
		
		int threat = dfs(0,0);
		
		
		
		
		
		
		cout << "Case #" << ct << ":" << " " << dists[0][1]-1 << " " << threat-dists[0][1] << endl;
		fout << "Case #" << ct << ":" << " " << dists[0][1]-1 << " " << threat-dists[0][1] << endl;
		
		
		
	}
	
	
	return 0;
}

