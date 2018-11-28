// aa.cpp : Defines the entry point for the console application.
//

#include<iostream>
#include <string>
#include <fstream>
#include <math.h>
#include <list>
#include <stack>
#include <queue>
#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define fore(i, a, n) for(int i = (int)(a); i < (int)(n); i++)
using namespace std;

int main()
{
	ifstream in("A-large.in");
	ofstream out("output.txt");
	int t;
	int mat;
	in>>t;
	forn(i,t)
	{
		out<<"Case #"<<i+1<<": "<<endl;
		in>>mat;
		char arr[100][100];
		for(int j=0;j<mat;j++)
		{

			for(int k=0;k<mat;k++)
			{
				in>>arr[j][k];
			}
			
		}
		for(int j=0;j<mat;j++)
		{
			double n0=0,n1=0;
			double wp=0,owps[100] = {0},oowps[100]= {0},count[100]={0};
			
			for(int k=0;k<mat;k++)
			{
				if(arr[j][k]=='1')
						n1++;
				else if(arr[j][k]=='0')
						n0++;
				
			}
			wp=n1/(n1+n0);

			int team =0;
			for(int k=0;k<mat;k++)
			{if(k==j)continue;

			if(arr[j][k] == '.')
			{
				continue;
			}
			team++;
				double n2=0,n3=0;
				for(int x=0;x<mat;x++)
				{
					if(x==j)
							continue;
					if(arr[k][x]=='1')
						n2++;
					else if(arr[k][x]=='0')
						n3++;
				}
				owps[k]=n2/(n2+n3);
				count[k]=n2+n3;
			}

			double owp=0;
			for(int y=0;y<mat;y++)
					owp+=owps[y];
			owp=owp/team;
			
			int team2 = 0;
			for(int z=0;z<mat;z++)
			{
				if(j==z)continue;
				if(arr[j][z] == '.')
				{
					continue;
				}
				team2++;

				for(int s=0; s<mat; s++)
				{
					owps[s] = 0;
					count[s]=0;
				}

				int team1 = 0;
				for(int k=0;k<mat;k++)
				{if(k==z)continue;

				if(arr[z][k] == '.')
				{
					continue;
				}
				team1++;

				double n2=0,n3=0;
				for(int x=0;x<mat;x++)
				{
					if(x==z)
						continue;
					if(arr[k][x]=='1')
						n2++;
					else if(arr[k][x]=='0')
						n3++;
				}
				owps[k]=n2/(n2+n3);
				count[k]=n2+n3;
				}
				double owp=0;
				for(int y=0;y<mat;y++)
					owp+=owps[y];
				oowps[z]=owp/team1;
			}
			double oowp=0;
			for(int y=0;y<mat;y++)
				oowp+=oowps[y];
			oowp=oowp/team2;
		//	out<<wp<<endl<<owp<<endl<<oowp<<endl;

			out<<0.25 * wp + 0.50 * owp+ 0.25 * oowp<<endl;
		}

	}
	system("pause");
}
		

	


