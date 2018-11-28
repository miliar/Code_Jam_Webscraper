#include <iostream>
#include <string>
#include <algorithm>
#include <cstring>
#include <stdlib.h>
#include <cmath>
using namespace std;
string oppo[40];
string comb[50];
string res;

bool check(int n)
{
	int flag=-1;
	int size=res.size();
	if(res[size-1] == oppo[n][1])
		flag=0;
	if(res[size-1] == oppo[n][0])
		flag=1;
	if(flag == -1)
		return false;
	for(int i=0;i<(size-1);i++)
	{
		if(res[i] == oppo[n][flag])
			return true;
	}
	return false;
}

void comb_f(int n)
{
	int flag=-1;
	int size=res.size();
	if(res[size-1] == comb[n][1])
		flag=0;
	if(res[size-1] == comb[n][0])
		flag=1;
	if(flag == -1)
		return;
	if(res[size-2] == comb[n][flag])
	{
		res.pop_back();
		res.pop_back();
		res.push_back(comb[n][2]);
	}
	return ;
}

int main()
{
	freopen("e:\\B-small.in", "r", stdin);	freopen("e:\\B-small.out", "w", stdout);
	int T;
	scanf("%d",&T);
	for(int i=0;i<T;i++)
	{
		res.clear();
		printf("Case #%d: ",i+1);
		int c,d,n;
		scanf("%d",&c);
		for(int i=0;i<c;i++)
		{
			cin>>comb[i];
		}
		scanf("%d",&d);
		for(int i=0;i<d;i++)
		{
			cin>>oppo[i];
		}
		scanf("%d",&n);
		string list;
		cin>>list;
		res.push_back(list[0]);
		for(int i=1;i<n;i++)
		{
			res.push_back(list[i]);
			int ressize=res.size();
			if(ressize < 2)
				continue;
			for(int j=0;j<c;j++)
			{
				comb_f(j);
			}
			for(int j=0;j<d;j++)
			{
				if(check(j))
					res.clear();
			}
		}
		int size1=res.size();
		printf("[");
		for(int i=0;i<size1;i++)
		{
			if(i != 0)
				printf(", ");
			printf("%c",res[i]);
		}
		printf("]\n");
		
	}
	return 0;
}