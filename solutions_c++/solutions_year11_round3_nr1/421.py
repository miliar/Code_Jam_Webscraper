#define _CRT_SECURE_NO_DEPRECATE


#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<fstream>
#include<string>
#include<cmath>
#include<set>
#include<list>
#include<limits>
#include<string.h>
#include<memory.h>
using namespace std;

#define SZ(x) ((int)x.size())

ifstream inf("A-small-attempt0.in");
ofstream outf("out.txt");

#define cin inf

#define cout outf


char mx[55][55];
char m2[55][55];
int main()
{
	int T;
	cin>>T;
	for(int t=1;t<=T;t++)
	{
		int m,n;
		cin>>m>>n;
		for(int i=0;i<m;i++)
			for(int j=0;j<n;j++)
				cin>>mx[i][j];
		cout<<"Case #"<<t<<":"<<endl;
		for(int i=0;i<m;i++)
		{
			for(int j=0;j<n;j++)
			{
				if(mx[i][j] == '#')
				{
					if(mx[i][j+1]=='#' && 
						mx[i+1][j] == '#' && mx[i+1][j+1] == '#')
					{
						mx[i][j] = '/';
						mx[i][j+1] = '\\';
						mx[i+1][j] ='\\';
						mx[i+1][j+1] = '/';
					}
					else
						goto im;
				}
			}
		}
		for(int i=0;i<m;i++)
		{
			for(int j=0;j<n;j++)
			{
				cout<<mx[i][j];
			}
			cout<<endl;
		}
		continue;
im:
		cout<<"Impossible"<<endl;
	}
} 