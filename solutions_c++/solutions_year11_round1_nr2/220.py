#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

using namespace std;

int main()
{
	int t;
	scanf("%d", &t);
	int tt = t;
	while(t--)
	{
		int n, m;
		cin>>n>>m;
		vector<string> d(n);
		vector<string> l(m);
		
		for(int i=0; i<n; i++)
		{
			string s;
			cin>>s;
			d[i] = s;
		}
		
		for(int i=0; i<m; i++)
		{
			string s;
			cin>>s;
			l[i] = s;
		}
		
		if(tt - t != 1)
			printf("\nCase #%d:", tt-t);
		else
			printf("Case #%d:", tt-t);
		for(int i=0; i<m; i++)
		{
			int ret = 0;
			string sret = "";
			for(int j=0; j<n; j++)
			{
				vector<int> done(n);
				int adict[26];
				memset(adict, 0, sizeof(adict));
				int len = d[j].size();
				
				for(int k=0; k<n; k++)
				{
					if(d[k].size() != len)
						done[k] = 0;
					else
					{
						done[k] = 1;
						for(int z=0; z<d[k].size(); z++)
						{
							adict[d[k][z]-'a']++;
						}
					}
				}
				
				int ct = 0;
				
				for(int k=0; k<26; k++)
				{
					if(accumulate(done.begin(), done.end(), 0) == 1) break;
					//cout<<accumulate(done.begin(), done.end(), 0);
					if(adict[int(l[i][k] - 'a')] != 0)
					{
						//cout<<"tryin"<<l[i][k]<<endl;
						bool flg = false;
						for(int z=0; z<n; z++)
						{
							for(int y=0; y<d[z].size(); y++)
							{
								if(done[z] == 1 && ((d[z][y] == l[i][k] && d[z][y] != d[j][y]) || (d[j][y] == l[i][k] && d[z][y] != d[j][y])))
								{
									flg = true;
									done[z] = 0;
									for(int x=0; x<d[z].size(); x++)
									{
										adict[d[z][x]-'a']--;
									}
								}
							}
						}
						if(flg)
						{
							flg = false;
							for(int z=0; z<len; z++)
							{
								if(d[j][z] == l[i][k]) {flg = true; break;}
							}
							if(!flg) ct++;
						}
					}
					
					
					
				}
				//cout<<"aaa:"<<ct<<d[j];
				if(ct > ret)
				{
					ret = ct;
					sret = d[j];
				}
				
			}
			if(sret == "") sret = d[0];
			cout<<" "<<sret;
		}
		
	}
	cout<<"\n";
	return 0;
}
