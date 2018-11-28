// proga.cpp : Defines the entry point for the console application.
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

bool isleft[50];
int n = 0;
int vals[50];

bool cando()
{
	vector <int> lis;
	for(int i=0; i<n; i++)
	{
		if(isleft[i])
			lis.push_back(vals[i]);
	}
	sort(lis.begin(),lis.end());
	for(int i=0; i<lis.size(); i++)
	{
		if(lis[i]>i)
			return false;
	}
	return true;
}


int main(void)
{
	int ttt;
	cin >> ttt;
	int ct = 0;
	
	while(ttt>0)
	{
		ct++;
		ttt--;
		cin >> n;
		memset(isleft,0,sizeof(isleft));
		int i,j,k;
		for(i=0; i<n; i++)
		{
			string s;
			cin >> s;
			vals[i]=-1;
			for(j=0; j<n; j++)
			{
				if(s[j]=='1')
					vals[i]=j;
			}
		}
		int ans = 0;
		for(i=0; i<n; i++)
		{
			isleft[i]=true;
		}
		for(int x = n; x>1; x--)
		{
			int curr = 0;
			for(k=n-1; k>=0; k--)
			{
				if(!isleft[k])
					continue;
				isleft[k]=false;
				if(cando())
				{
					break;
				}
				else
				{
					isleft[k]=true;
				}
				curr++;
			}
			ans+=curr;
		}

		
		cout << "Case #" << ct << ":" << " " << ans << endl;
		fout << "Case #" << ct << ":" << " " << ans << endl;
		
	}

	
	return 0;
}


