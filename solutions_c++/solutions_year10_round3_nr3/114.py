#include <iostream>
#include <cmath>
#include <vector>
#include <string>
#include <map>
using namespace std;
char g[600][600];
int n,m;

void solve()
{
	scanf("%d%d",&n,&m);
	map<int,int> res;
	char t[100];
	for(int i=0;i<n;i++)
	{
		scanf("%s",t);
		
		for(int j=0;j<m/4;j++)
		{
			int v = t[j]-'0';
			if(v>9) v=t[j]-'A'+10;
			g[i][j*4  ] = ((v & 8)?1:0);
			g[i][j*4+1] = ((v & 4)?1:0);
			g[i][j*4+2] = ((v & 2)?1:0);
			g[i][j*4+3] = ((v & 1)?1:0);
		}
	}
	/*
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<m;j++)
			printf("%d ",g[i][j]);
		puts("");
	}*/

	for(int size=n;size>=1;size--)
	{
		for(int i=0;i<n+1-size;i++)
		{
			for(int j=0;j<m+1-size;j++)
			{
				int diff = 0;
				int flag_a = 1;
				for(int x=i;x<i+size;x++) for(int y=j;y<j+size;y++)
				{
					if(g[x][y] == -1) flag_a = 0;
					diff += (((x+y)%2) ^ (g[x][y]));
				}
				if(flag_a && (diff == size*size || diff == 0))
				{
					//yes count ++
					res[size]++;
					
					//rm map;
					for(int x=i;x<i+size;x++) for(int y=j;y<j+size;y++) g[x][y] = -1;
				}

			}
		}
		
	}

	string result = "";
	char tresult[100];
	int cresult = 0;
	for(map<int,int>::iterator im = res.begin(); im!=res.end(); im++)
	{
		sprintf(tresult,"%d %d\n",im->first ,im->second);
		result = tresult + result;
		cresult ++;
	}
	cout<<cresult<<endl;
	cout<<result;
}
int main()
{


	int Ti,T;
	scanf("%d",&T);
	for(Ti = 1; Ti <= T; Ti++)
	{
		printf("Case #%d: ",Ti);
		solve();
	}
}
