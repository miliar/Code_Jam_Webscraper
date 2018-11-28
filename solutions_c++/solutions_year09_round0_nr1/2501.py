#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

set<string>ret;
vector<string>Vec;
char str[1000];


int main()
{
	freopen("ain.txt","r",stdin);
	freopen("aout.txt","w",stdout);
	ret.clear();
	Vec.clear();
	int L,D,N;	
	scanf("%d %d %d",&L,&D,&N);
	int ans;
	int i, j, k, cnt, l;
	bool flag;
	for(i = 0;i < D; i++)
	{
		scanf("%s",str);
		Vec.push_back(str);
	}

	
	for(i = 0; i < N; i++)
	{
		set<char>ss[30];
		scanf("%s",str);
		l = strlen(str);
		flag = false;
		ans = 0;
		for(j = 0,cnt = 0;j < l;j++)
		{
			if(flag)
			{
				if(str[j]==')')
				{
					cnt++;
					flag = false;
				}
				else
				{
					ss[cnt].insert(str[j]);
				}
			}
			else
			{
				if(str[j]=='(')
				{
					flag = true;
				}
				else
				{
					ss[cnt++].insert(str[j]);
				}
			}
		}
		for(k = 0; k < D; k++)
		{
			for(j = 0;j < L;j++)
			{
				if(ss[j].find(Vec[k][j]) == ss[j].end())
					break;
			}
			if(j == L)
				ans++;
		}
		printf("Case #%d: %d\n",i+1,ans);
	}

}
