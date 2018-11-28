// GCJ.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <memory.h>
#include <set>
#include <map>
#include <string>
using namespace std;
int T;
int N,M;
set<string> dir;
string w_dir[105];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output1.txt","w",stdout);
	scanf("%d",&T);
	for(int i = 1; i <= T; ++ i)
	{
		scanf("%d%d",&N,&M);
		dir.clear();
		for(int k = 0;k < N; ++ k)
		{
			cin >> w_dir[0];
			dir.insert(w_dir[0]);
			//cout << w_dir[0] << endl;
			//printf("%s\n",dir[k]);
		}
		for(int k = 0;k < M; ++ k)
		{
			cin >> w_dir[k];
			//cout << w_dir[k] << endl;
			//printf("%s\n",w_dir[k]);
		}
		int Z = 0;
		for(int k = 0; k < M; ++ k)
		{
			if(w_dir[k].size() == 1) continue;
			string L ="/";
			int beg = 1;
			while (true)
			{
				for(;w_dir[k].length() != beg && w_dir[k].at(beg) != '/'; ++ beg) {L += w_dir[k].at(beg);}
				
				if(dir.empty() || dir.find(L) == dir.end()) {++ Z;dir.insert(L);}
				if(w_dir[k].length() == beg) break;
				if(w_dir[k].at(beg) == '/') {
					L += '/';
					beg ++;
				}
			}
		}
		printf("Case #%d: ",i);
		printf("%d\n",Z);
	}
	return 0;
}
