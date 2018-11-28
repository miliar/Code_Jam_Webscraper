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

bool cando[101][101][101];


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
		int n,i,j,k,s,p;
		
		int m;
		
		fin >> n >> s  >> p;
		
		memset(cando,0,sizeof(cando));
		
		cando[0][0][0]=true;
		
		
		for(m=0; m<n; m++)
		{
			int x;
			fin >> x;
			
			bool canboth = false;
			bool canspec = false;
			bool cansucnotspec = false;
			bool canneither = false;
			
			for(i=0; i<=10; i++)
			{
				for(j=i; j<=10; j++)
				{
					for(k=j; k<=10; k++)
					{
						if(i+j+k==x && k-i<=1 && k>=p)
							cansucnotspec=true;
						if(i+j+k==x && k-i==2 && k<p)
							canspec=true;
						if(i+j+k==x && k-i==2 && k>=p)
							canboth=true;
						if(i+j+k==x && k<p && k-i<=1)
							canneither=true;
					}
				}
			}
			
			//cout << x << " " << canboth << " " << canspec << " " << cansucnotspec << endl;
			
			for(i=0; i<n; i++)
			{
				for(j=0; j<n; j++)
				{
					if(cando[m][i][j])
					{
						if(canboth)
							cando[m+1][i+1][j+1]=true;
						if(cansucnotspec)
							cando[m+1][i+1][j]=true;
						if(canspec)
							cando[m+1][i][j+1]=true;
						if(canneither)
							cando[m+1][i][j]=true;
						
					}
				}
			}
			
		}
		
		int ans =0;
		
		for(i=0; i<=n; i++)
		{
			if(cando[n][i][s])
				ans=i;
		}
						
		
				
		cout << "Case #" << ct << ":" << " " << ans << endl;
		fout << "Case #" << ct << ":" << " " << ans << endl;
		
	}
	
	
	return 0;
}

