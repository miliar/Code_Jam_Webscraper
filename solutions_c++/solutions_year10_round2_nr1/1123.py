#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
vector<string> exist;

bool pd(string a, string b)
{
	if( a.size() < b.size())	return false;
	int i;
	for(i = 0; i < b.size(); i ++)
	{
		if(a[i] != b[i])
			return false;	
	}
	if(a.size() == b.size())
	return true;	
	
	if( a[i] == '/')
		return true;
	
	return false;
}

bool IsIn(string b)
{
	int i;
	for(i = 0; i < exist.size(); i ++)
	{
		if(pd(exist[i], b))
			return true;	
	}	
	return false;
}


int check(string t)
{
	string sub;
	int cnt = 0;
	char b[255];
	b[0] = '/';
	int i;
	for(i = 1; i < t.size(); i ++)
	{
		if(t[i] == '/')
		{
			b[i] = '\0';
			if(!IsIn(b))	
			{
				exist.push_back(b);
				cnt ++;
			}
			b[i] = t[i];
		}	
		else	b[i] = t[i];
	}
	b[i] = '\0';
	if(!IsIn(b))	
	{
		exist.push_back(b);
		cnt ++;
	}
	return cnt;
}


void work()
{
	int cnt = 0;
	int n, m;
	scanf("%d%d", &n, &m);
	int i;
	char pt[255];
	exist.clear();
string t;

	for(i = 0; i < n; i ++)
	{
//		scanf("%s", pt);
		cin >> t;
		exist.push_back(t);
	}
	
	sort(exist.begin(), exist.end());
	
	for(i = 0; i < m; i ++)
	{
		cin >> t;
//		scanf("%s", pt);
//		path.push_back(pt);
		cnt += check(t);
	}
	
	printf("%d\n", cnt);
		
	
}





int main()
{
//	freopen("A.in","r",stdin);
//	freopen("A-small-attempt0.in","r",stdin);freopen("111A-small-attempt0.out","w",stdout);
//	freopen("A-small-attempt1.in","r",stdin);freopen("111A-small-attempt1.out","w",stdout);
//	freopen("A-small-attempt2.in","r",stdin);freopen("A-small-attempt2.out","w",stdout);
	freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);

	int kase;
	int t;
	scanf("%d", &t);
	for(kase = 1; kase <= t; kase ++)
	{
		printf("Case #%d: ", kase);
		work();
	}	

	return 0;
	
}
