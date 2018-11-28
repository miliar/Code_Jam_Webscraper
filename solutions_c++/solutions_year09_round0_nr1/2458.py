// VS2008.cpp : 定义控制台应用程序的入口点。
//

//written on Sep 3,2009
#include "stdafx.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>
#include <float.h>
#include <math.h>
#include <time.h>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <stack>
#include <cassert>
#include <queue>
#include <bitset>
#include <iomanip>
#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

int L,D,N;
int ans;

void dfs(string s,int d,const vector<string> & vec,const vector< set<string> >& VSet)
{
	if(d >= L)
	{
		if(VSet[d-1].find(s) != VSet[d-1].end())
			ans++;
		return;
	}

	string temp = s;
	for(unsigned i=0;i<vec[d].length();i++)
	{
		s += vec[d][i];
		if(VSet[d].find(s) != VSet[d].end())
			dfs(s,d+1,vec,VSet);
		s = temp;
	}
}

int main()
{
	fstream fin("input.txt");

	freopen("output.txt","w",stdout);
    int i,j;
    while(fin>>L>>D>>N)
    {
		vector< set<string> > VSet;
		for(i=1;i<=L;i++)
		{
			VSet.push_back(set<string>());
		}

        string s;
        for(i=0;i<D;i++)
        {
            fin>>s;
			string temp;
			for(j=0;j<s.length();j++)
			{
				temp += s[j];
				if(VSet[j].find(temp) == VSet[j].end())							//no found
					VSet[j].insert(temp);
			}
        }

        for(i=1;i<=N;i++)
        {
            ans = 0;
			fin>>s;
			j = 0;
			vector<string> vec;
			while(j<s.length())
			{
				string t;
				if(s[j] == '(')
				{
					while(++j<s.length() && s[j] != ')')
					{
						t+=s[j];
					}			
				}
				else
				{
					t += s[j];
				}
				vec.push_back(t);

				j++;
			}
			dfs(string(),0,vec,VSet);
			cout<<"Case #"<<i<<": "<<ans<<endl;
        }//for
    }//while   

	return 0;
}



