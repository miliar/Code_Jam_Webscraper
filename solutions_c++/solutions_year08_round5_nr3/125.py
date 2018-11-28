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

ofstream fout("output.txt");
ifstream fin("input.txt");

bool isok[10][10];
int anses[11][1024];
int oklis[10];

bool isgd[1024];
int tots[1024];

void mkgd(void)
{
	int i,j,k,l;
	for(i=0; i<1024; i++)
	{
		isgd[i]=true;
		for(j=0; j<10; j++)
		{
			if( (i&(1<<j))>0 && (i&(1<<(j+1)))>0)
			{
				isgd[i]=false;
			}
			if( i&(1<<j))
			{
				tots[i]++;
			}
		}
	}
	return;
}

int main(void)
{
	mkgd();
	int ttt;
	cin >> ttt;
	int ct = 0;
	while(ttt>0)
	{
		ct++;
		ttt--;
		int i,j,k,l;
		int m,a,b;
		memset(isok,0,sizeof(isok));
		memset(anses,0,sizeof(anses));
		int n;
		cin >> m >> n;
		char c;
		for(i=0; i<m; i++)
		{
			oklis[i]=0;
			for(j=0; j<n; j++)
			{
				cin >> c;
				if(c=='.')
				{
					isok[i][j]=true;
					oklis[i]+=(1<<j);
				}
			}
		}
		int ans = 0;
		for(i=0; i<m; i++)
		{
			for(j=0; j<(1<<n); j++)
			{
				k=0;
				for(l=0; l<n; l++)
				{
					if(j&(1<<l))
					{
						
						if(l>0)
						{
							k|=(1<<(l-1));
						}
						if(l<n-1)
						{
							k|=(1<<(l+1));
						}
					}
				}
				for(l=0; l<(1<<n); l++)
				{
					if( isgd[l] && (l&k)==0 && (l&oklis[i])==l)
					{
						if(anses[i][j]+tots[l] > anses[i+1][l])
						{
							anses[i+1][l]=anses[i][j]+tots[l];
							if(anses[i+1][l]>ans)
							{
								ans=anses[i+1][l];
								//cout << ans << " " << l << endl;
							}
						}
					}
				}
			}
			cout << i << " " << ans << endl;
		}
		
		for(i=0; i<1024; i++)
		{
			if(anses[m][i]>ans)
			{
				ans=anses[m][i];
			}
		}
		cout << "Case #" << ct << ":" << " " << ans << endl;
		fout << "Case #" << ct << ":" << " " << ans << endl;
		
		
	}

	
	return 0;
}

	