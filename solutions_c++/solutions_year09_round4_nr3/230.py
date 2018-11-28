// progc.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


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

int vals[100][25];

bool isok[100][100];

int dolis[20000];

int bm(int n)
{
	int i,j,k;
	int tox[100];
	int fromy[100];



	for(i=0; i<n; i++)
	{
		tox[i]=-1;
		fromy[i]=-1;
	}
	
	int ans = 0;
	int donex[100];
	int doney[100];
	while(true)
	{
		for(i=0; i<n; i++)
		{
			donex[i]=doney[i]=-1;
		}
		int readfrom,writeto;
		readfrom=writeto=0;
		for(i=0; i<n; i++)
		{
			if(tox[i]==-1)
			{
				dolis[writeto]=i;
				donex[i]=100;
				writeto++;
			}
		}
		while(readfrom<writeto)
		{
			k=dolis[readfrom];
			if(k<100)
			{
				for(i=0; i<n; i++)
				{
					if(isok[k][i] && doney[i]==-1)
					{
						doney[i]=k;
						dolis[writeto]=i+100;
						writeto++;
					}
				}
			}
			else
			{
				if(k>=100)
				{
					k-=100;
					if(fromy[k]==-1)
					{
						//done, exit

						fromy[k]=doney[k];
						tox[fromy[k]]=k;
						ans++;
						k=fromy[k];
						while(donex[k]!=100)
						{
							k=donex[k];
							fromy[k]=doney[k];
							tox[fromy[k]]=k;
							k=fromy[k];
						}
						writeto=100000;
						break;
					}
					else
					{
						if(donex[fromy[k]]==-1)
						{
							donex[fromy[k]]=k;
							dolis[writeto]=fromy[k];
							writeto++;
						}
					}
				}
			}
			readfrom++;
		}
		if(readfrom==writeto)
			break;
	}
	return ans;
}

int main(void)
{
	int ttt;
	cin >> ttt;
	int ct = 0;
	string s;
	while(ttt>0)
	{
		ct++;
		ttt--;
		
		int n,i,j,k,m;
		cin >> n >> m;
		for(i=0; i<n; i++)
		{
			for(j=0; j<m; j++)
			{
				cin >> vals[i][j];
			}
		}
		memset(isok,0,sizeof(isok));
		for(i=0;i<n; i++)
		{
			for(j=0; j<n; j++)
			{
				for(k=0; k<m; k++)
				{
					if(vals[i][k]>=vals[j][k])
						break;
				}
				if(k==m)
					isok[i][j]=true;
			}
		}

		int ans=bm(n);
		cout << ans << endl;
		ans = n-ans;
		
		cout << "Case #" << ct << ":" << " " << ans << endl;
		fout << "Case #" << ct << ":" << " " << ans << endl;
		
	}

	
	return 0;
}

