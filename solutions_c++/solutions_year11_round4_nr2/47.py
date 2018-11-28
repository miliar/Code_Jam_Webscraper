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

int norm[501][501];
int col[501][501];
int row[501][501];
int vals[501][501];

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
		int n,i,j,k;
		
		int ans = 0;
		
		int r,c;
		
		memset(norm,0,sizeof(norm));
		memset(col,0,sizeof(col));
		memset(vals,0,sizeof(vals));
		memset(row,0,sizeof(row));
		
		fin >> r >> c >> k;
		
		string s;
		
		for(i=0; i<r; i++)
		{
			fin >> s;
			for(j=0; j<c; j++)
			{
				vals[i][j] = s[j]-'0';
			}
		}
		
		for(i=0; i<r; i++)
		{
			k=0;
			for(j=0; j<c; j++)
			{
				k+=vals[i][j];
				norm[i+1][j+1]=norm[i][j+1]+k;
			}
		}
		
		for(i=0; i<r; i++)
		{
			k=0;
			for(j=0; j<c; j++)
			{
				k+=vals[i][j]*(i+1);
				row[i+1][j+1]=row[i][j+1]+k;
			}
		}
		
		for(i=0; i<c; i++)
		{
			k=0;
			for(j=0; j<r; j++)
			{
				k+=vals[j][i]*(i+1);
				col[j+1][i+1]=col[j+1][i]+k;
			}
		}
		
		/*for(i=0; i<=r; i++)
		{
			for(j=0; j<=c; j++)
			{
				cout << norm[i][j] << " ";
			}
			cout << endl;
		}
		
		for(i=0; i<=r; i++)
		{
			for(j=0; j<=c; j++)
			{
				cout << row[i][j] << " ";
			}
			cout << endl;
		}
		
		for(i=0; i<=r; i++)
		{
			for(j=0; j<=c; j++)
			{
				cout << col[i][j] << " ";
			}
			cout << endl;
		}*/
		
		
		for(i=0; i<r; i++)
		{
			for(j=0; j<c; j++)
			{
				for(k=3; i+k<=r && j+k<=c; k++)
				{
					int normsum = norm[i+k][j+k]-norm[i][j+k]-norm[i+k][j]+norm[i][j];
					int rowsum = row[i+k][j+k]-row[i][j+k]-row[i+k][j]+row[i][j];
					int colsum = col[i+k][j+k]-col[i][j+k]-col[i+k][j]+col[i][j];
					
					int topsum = rowsum - normsum*i - vals[i][j] - vals[i][j+k-1] - k*vals[i+k-1][j] - k*vals[i+k-1][j+k-1];
					int botsum = normsum*(i+k+1) - rowsum - k*vals[i][j] - k*vals[i][j+k-1] - vals[i+k-1][j] - vals[i+k-1][j+k-1];
					
					int leftsum = colsum - normsum*j - vals[i][j] - vals[i+k-1][j] - k*vals[i][j+k-1] - k*vals[i+k-1][j+k-1];
					int rightsum = normsum*(j+k+1) - colsum - k*vals[i][j] - k*vals[i+k-1][j] - vals[i][j+k-1] - vals[i+k-1][j+k-1];
					
					//cout << i << " " << j << " " << k << " " << normsum << " " << rowsum << " " << colsum << " " << topsum << " " << botsum << " " << leftsum << " " << rightsum << endl;
					
					if(topsum==botsum && leftsum==rightsum && k>ans)
						ans=k;
				}
			}
		}
		
		
		if(ans>0)
		{
			cout << "Case #" << ct << ":" << " " << ans << endl;
			fout << "Case #" << ct << ":" << " " << ans << endl;
		}
		else {
			cout << "Case #" << ct << ":" << " IMPOSSIBLE" << endl;
			fout << "Case #" << ct << ":" << " IMPOSSIBLE" << endl;
		}

		
		
		
	}
	
	
	return 0;
}

