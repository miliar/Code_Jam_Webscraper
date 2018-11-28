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


int adj[100][100];
int wins[100];
int plays[100];
double wp[100];
double owp[100];
double oowp[100];

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
		
		fin >> n;
		
		string s;
		
		for(i=0; i<n; i++)
		{
			fin >> s;
			
			for(j=0; j<n; j++)
			{
				if(s[j]=='.')
					adj[i][j]=2;
				else if(s[j]=='0')
					adj[i][j]=0;
				else {
					adj[i][j]=1;
				}
			}
			wins[i]=plays[i]=0;
		}
		for(i=0; i<n; i++)
		{
			for(j=0; j<n; j++)
			{
				
			if(adj[i][j]==2)
				continue;
			plays[i]++;
			wins[i]+=adj[i][j];
			}
			wp[i]=((double)wins[i])/((double)plays[i]);
			cout << wp[i] << " ";
		}
		cout << endl;
		
		for(i=0; i<n; i++)
		{
			double num = 0.0;
			double denom = 0.0;
			
			for(j=0; j<n; j++)
			{
				if(adj[i][j]==2)
					continue;
				num+=((double)wins[j]-adj[j][i])/((double)plays[j]-1.);
				denom+=1.0;
			}
			owp[i]=num/denom;
			cout << owp[i] << " ";
		}
		cout << endl;
		
		for(i=0; i<n; i++)
		{
			double num,denom;
			num=denom=0;
			for(j=0; j<n; j++)
			{
				if(adj[i][j]==2)
					continue;
				num+=owp[j];
				denom+=1.0;
			}
			oowp[i]=num/denom;
		}
		
		

		
		
		
		cout << "Case #" << ct << ":"  << endl;
		fout << "Case #" << ct << ":" << endl;
		cout.precision(9);
		fout.precision(9);
		for(i=0; i<n; i++)
		{
			cout << 0.25*wp[i]+0.5*owp[i] + 0.25*oowp[i] << endl;
			fout << 0.25*wp[i]+0.5*owp[i] + 0.25*oowp[i] << endl;
		}
		
		
		
	}
	
	
	return 0;
}

