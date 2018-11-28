#include <algorithm>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <queue>
#include <map>
#include <cmath>
#include <memory.h>
#include <string>
#include <iostream>
using namespace std;
const int maxn=5001;
const int maxl=16;
string dict[maxn];
bool p[maxl][26];
int l,d,n;

void init(){
	cin>>l>>d>>n;
	for (int i=1;i<=d;i++)
	{
		cin>>dict[i];
	}
	return;
}

bool check(int k)
{
	for (int i=1;i<=l;i++)
	{
		if (!p[i][dict[k][i-1]-'a'])
		{
			return false;
		}
	}
	return true;
}

void process(){
	memset(p,false,sizeof(p));
	int cur=0;
	string str;
	cin>>str;
	for (int i=1;i<=l;i++)
	{
		if (str[cur]!='(')
		{
			p[i][str[cur]-'a']=true;
			cur++;
			continue;
		}
		while (1)
		{
			cur++;
			if (str[cur]==')')
			{
				cur++;
				break;
			}
			p[i][str[cur]-'a']=true;
		}		
	}
	int ans=0;
	for (int i=1;i<=d;i++)
	{
		if (check(i))
		{
			ans++;
		}
	}
	printf("%d\n",ans);
	return;
}

int main(){
	init();
	for (int i=1;i<=n;i++)
	{
		printf("Case #%d: ",i);
		process();
	}
	return 0;
}
