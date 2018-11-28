#include <vector>
#include <list>
#include <map>
#include <set>
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
#include <queue>
#include <fstream>
#include <cassert>
#include <memory.h>

using namespace std;

int l,d,n;
char a[10000][19];
int tak[200][26];
char x[10000];

int main()
{
	freopen("nut.txt","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d%d%d",&l,&d,&n);
	for (int i=0;i<d;i++)
		scanf("%s",a+i);
	for (int j=1;j<=n;j++)
	{
		scanf("%s",x);
		memset(tak,0,sizeof(tak));
		int m=strlen(x);
		int f=0,ins=1;
		for (int i=0;i<m;i++)
		{
			if (x[i]=='(')
				ins=0;
			else if (x[i]==')')
			{
				ins=1;
				f++;
			}
			else
			{
				tak[f][x[i]-'a']++;
				if (ins)
					++f;
			}
			if (f>l)
				break;
		}
		int res=0;
		for (int h=0;h<d;h++)
			if (l==f)
			{
				int not=1;
				for (int g=0;g<l;g++)
				{
					if (!tak[g][a[h][g]-'a'])
						not=0;
				}
				res+=not;
			}
		printf("Case #%d: %d\n",j,res);
	}
	return 0;
}