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

int mns[2000];
int anses[3000][20];
int costs[3000];

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
		int n,i,j,k,p;
		fin >> p;
		for(i=0; i<(1<<p); i++)
		{
			fin >> mns[i];
		}
		for(i=0; i<(1<<p)-1; i++)
		{
			fin >> costs[i];
		}
		for(i=0; i<(1<<p); i+=2)
		{
			for(j=0; j<20; j++)
			{
				if(mns[i] > j && mns[i+1] > j)
				{
					anses[i/2][j]=0;
				}
				else if(mns[i]>=j && mns[i+1]>=j) {
					anses[i/2][j]=costs[i/2];
				}
				else
				{
						anses[i/2][j]=500000000;
				}
			}
		}
		int tot = 0;
		int last = 0;
		for(k=1; k<p; k++)
		{
			tot += (1<<(p-k));
			
			for(i=0; i<(1<<(p-k-1)); i++)
			{
				int now = tot + i;
				int chd1 = last+2*i;
				int chd2 = last+2*i+1;
				cout << now << " " << chd1 << " " << chd2 << endl;
				for(j=0; j<=10; j++)
				{
					anses[now][j]=500000000;
					int val1 = anses[chd1][j]+anses[chd2][j]+costs[now];
					int val2 = anses[chd1][j+1]+anses[chd2][j+1];
					if(val1<anses[now][j])
						anses[now][j]=val1;
					if(val2<anses[now][j])
						anses[now][j]=val2;
					cout << anses[now][j] << " ";
				}
				cout << endl;
			}
			
			
			last+= (1<<(p-k));
		}
						
		int ans = anses[(1<<p)-2][0];
		cout << "Case #" << ct << ":" << " " << ans << endl;
		fout << "Case #" << ct << ":" << " " << ans << endl;
		
	}
	
	
	return 0;
}

