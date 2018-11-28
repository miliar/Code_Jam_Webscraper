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



int rects[2000][4];
int pri[2000];
int ans[1000][2];

int sizes[1000];

int idx[1000];

bool cmp(int a, int b)
{
	return (sizes[a]>sizes[b]);
}

int main(void)
{
	int ttt;
	fin >> ttt;
	int ct = 0;
	string s;
	
	cout.precision(9);
	fout.precision(9);
	
	while(ttt>0)
	{
		ct++;
		ttt--;
		int i,j,k;
		int n,w,h;
		
		fin >> n >> w >> h;
		
		int m = 1;
		
		rects[0][0]=0;
		rects[0][1]=0;
		rects[0][2]=w;
		rects[0][3]=h;
		pri[0]=0;
		
		for(i=0; i<n; i++)
		{
			fin >> sizes[i];
			idx[i]=i;
		}
		
		sort(idx,idx+n,cmp);
		
		for(int ll=0; ll<n; ll++)
		{
			i = idx[ll];
			
			bool isdone = false;
			
			int bestpri = 10000;
			
			k = -1;
			
			for(j=0; j<m; j++)
			{
				if(!isdone || bestpri > pri[j])
				{
					bool okx = false;
					int x = -1;
					
					bool oky = false;
					int y = -1;
					
					if(rects[j][0] == 0 && rects[j][2] == w)
					{
						okx=true;
						x = 0;
					}
					else if(rects[j][0] == 0 && rects[j][2]>=sizes[i])
					{
						okx=true;
						x = 0;
					}
					else if(rects[j][2]-rects[j][0] >= 2*sizes[i])
					{
						okx=true;
						x=rects[j][0]+sizes[i];
					}
					else if(rects[j][2]==w && rects[j][2]-rects[j][0] >= sizes[i])
					{
						okx=true;
						x=rects[j][0] + sizes[i];
					}
					
					if(rects[j][1]==0 && rects[j][3]==h)
					{
						oky=true;
						y=0;
					}
					else if(rects[j][1]==0 && rects[j][3]>=sizes[i])
					{
						oky=true;
						y=0;
					}
					else if(rects[j][3]-rects[j][1] >= 2*sizes[i])
					{
						oky=true;
						y = rects[j][1] + sizes[i];
					}
					else if(rects[j][3]==h && rects[j][3]-rects[j][1]>=sizes[i])
					{
						oky=true;
						y = rects[j][1] + sizes[i];
					}
					
					if(!okx || !oky)
						continue;
					ans[i][0]=x;
					ans[i][1]=y;
					bestpri = pri[j];
					isdone=true;
					k=j;
					
				}
			}
			
			
			if(!isdone)
			{
				//pain
				cout << "FAIL TIME " << endl;
				break;
			}
			
			for(j=0; j<m; j++)
			{
				if(pri[j] > bestpri)
					pri[j]++;
			}
			
			j=k;
			
		//	cout << "PLACE " << idx[ll] << " " << i << " " << sizes[i] << " " << ans[i][0] << " " << ans[i][1] << endl;
		//	cout << "OLD " << rects[j][0] << " " << rects[j][1] << " " << rects[j][2] << " " << rects[j][3] << endl;
			
			pri[m] = pri[j];
			pri[j]++;
			
			rects[m][0] = rects[j][0];
			rects[m][1] = ans[i][1] + sizes[i];
			
			rects[m][2] = ans[i][0] + sizes[i];
			rects[m][3] = rects[j][3];
			
			rects[j][0] = ans[i][0] + sizes[i];
			
		//	cout << "NEW " << rects[j][0] << " " << rects[j][1] << " " << rects[j][2] << " " << rects[j][3] << endl;
		//	cout << "NEW " << rects[m][0] << " " << rects[m][1] << " " << rects[m][2] << " " << rects[m][3] << endl;
			
			m++;
			
			
		}
		
		
		
		
		
		cout << "Case #" << ct << ":";
		fout << "Case #" << ct << ":";
		
		for(k=0; k<n; k++)
		{
			fout << " " << ans[k][0] << " " << ans[k][1];
			cout << " " << ans[k][0] << " " << ans[k][1];
		}
		fout << endl;
		cout << endl;
		
	}
	
	
	return 0;
}

