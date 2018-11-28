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
#include <algorithm>

using namespace std;

const int M = 510;
const char* dest = "welcome to code jam";
char s[M],t[M];
int num[M];
int ans;
int sta[M];
int len;

void dfs(int d,int p)
{
	if(d >= 19)
	{
		int temp = 1;
		for(int i=0;i<d;i++)
		{
			temp *= sta[i];
			temp %= 10000;
		}
		ans += temp;
		ans %= 10000;
		return;
	}
	if(!t[p])																	//end
		return;
	if(d+len-p < 19)															//剪枝
		return;

	if(dest[d] == t[p])
	{
		sta[d] = num[p];
		dfs(d+1,p+1);
	}
	
	for(int i=p+1;t[i];i++)
		if(dest[d] == t[i])
		{
			dfs(d,i);
			break;
		}
}

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	int i,j,k,m,n;
	scanf("%d ",&n);
	for(i=1;i<=n;i++)
	{
		gets(s);
		k = strlen(s);
		if(k < 19)
		{
			printf("Case #%d: %04d\n",i,0);
			continue;
		}
		j = 0;
		m = 0;
		while(j<k)
		{
			t[m] = s[j++];
			num[m] = 1;
			while(j<k && s[j] == s[j-1])	
			{
				j++;
				num[m]++;
			}
			m++;
		}
		len = m;
		t[len] = '\0';

		ans = 0;
		dfs(0,0);
		ans %= 10000;
		printf("Case #%d: %04d\n",i,ans);
	}
	return 0;
}



