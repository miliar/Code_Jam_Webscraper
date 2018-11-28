#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <deque>
#include <map>

#define FOR(i, s, e) for(int i=s; i<e; i++)
#define INP(arr) for(int i=0; i<arr.size(); i++) cin >> arr[i];

using namespace std;

int main()
{
	freopen("B-small.in", "r", stdin);
	freopen("B-small.out", "w+", stdout);
	int t, c, d, n;
	scanf("%d\n", &t);
	char sym;
	for(int l=1; l<=t; l++)
	{
		vector<char> st;
		scanf("%d", &c);
		char* c1=new char[c];
		char* c2=new char[c];
		char* c3=new char[c];
		FOR(i, 0, c) scanf(" %c%c%c", &c1[i], &c2[i], &c3[i]);
		
		scanf(" %d", &d);
		char* d1=new char[d];
		char* d2=new char[d];
		FOR(i, 0, d) scanf(" %c%c", &d1[i], &d2[i]);
		
		scanf(" %d ", &n);
		FOR(i, 0, n)
		{
			cin >> sym;
			if(st.size())
			{
				bool flag=true;
				for(int j=0; j<c && flag; j++)
				{
					if((sym==c1[j] && st.back()==c2[j]) || (sym==c2[j] && st.back()==c1[j]))
					{
						st.pop_back();
						st.push_back(c3[j]);
						flag=false;
					}
				}
				if(flag) st.push_back(sym);
				FOR(j, 0, d)
				{
					if(st.back()==d1[j])
					{
						int k=0;
						while(k<st.size() && st[k]!=d2[j]) k++;
						if(st[k]==d2[j])
						{
							st.clear();
						}
					}
					
					if(st.back()==d2[j])
					{
						int k=0;
						while(k<st.size() && st[k]!=d1[j]) k++;
						if(st[k]==d1[j])
						{
							st.clear();
						}
					}
				}
			}
			else  st.push_back(sym);
		}
		
		printf("Case #%d: [", l);
		if(st.size()) cout << st[0];
		FOR(i, 1, st.size())
			cout << ", " << st[i];
		printf("]\n");
	}
	return 0;
}
