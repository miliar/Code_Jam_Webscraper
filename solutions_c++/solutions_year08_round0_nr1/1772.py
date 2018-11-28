#include <cstdio>
#include <string>
#include <vector>
#include <set>
#include <algorithm>
#include <iostream>

using namespace std;

vector <string> query;
set <string> isExist;
vector <int> dynamic;

int N, M;

int main(void)
{
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);

	for(int q=1;q<=T;q++)
	{
		query.clear();
		isExist.clear();
		dynamic.clear();

		scanf("%d\n", &N);
		for(int i=0;i<N;i++) { 	char ttemp[1000]; string temp; gets(ttemp); temp=ttemp; isExist.insert(temp); }
		scanf("%d\n", &M);
		for(int i=0;i<M;i++) { char ttemp[1000]; string temp; gets(ttemp); temp=ttemp; query.push_back(temp); }
		dynamic.resize(M);
		
		for(int i=1;i<M;i++) 
		{
			int dy=999999;
			for(set<string>::iterator it=isExist.begin();it!=isExist.end();it++)
			{
				for(int k=i;k>=0;k--)
				{
					if(*it==query[k]) break;
					if(k>0) dy=min(dy, dynamic[k-1]+1);
					else dy=0;
				}				
			}
			dynamic[i]=dy;
		}

		if(M!=0) printf("Case #%d: %d\n", q, dynamic[M-1]);		
		else printf("Case #%d: 0\n", q);		
	}

	return 0;
}