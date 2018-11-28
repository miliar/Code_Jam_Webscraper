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
string mp[10];
int ok()
{
	for (int i=0;i<4;++i)
	{
		for (int j=0;j<4;++j)
		{
			if (mp[i][j]=='.')
			{
				return 0;
			}
		}
	}
	return 1;
}
int judge(char x)
{
	for (int i=0;i<4;++i)
	{
		int ok=1;
		for (int j=0;j<4;++j)
		{
			if (mp[i][j]==x || mp[i][j]=='T')
			{
				continue;
			}
			else
			{
				ok=0;
				break;
			}
		}
		if (ok)
		{
			return 1;
		}
	}

	for (int i=0;i<4;++i)
	{
		int ok=1;
		for (int j=0;j<4;++j)
		{
			if (mp[j][i]==x || mp[j][i]=='T')
			{
				continue;
			}
			else
			{
				ok=0;
				break;
			}
		}
		if (ok)
		{
			return 1;
		}
	}

	int ok=1;
	for (int j=0;j<4;++j)
	{
		if (mp[j][j]==x || mp[j][j]=='T')
		{
			continue;
		}
		else
		{
			ok=0;
			break;
		}
	}
	if (ok)
	{
		return 1;
	}

	ok=1;
	for (int j=0;j<4;++j)
	{
		if (mp[3-j][j]==x || mp[3-j][j]=='T')
		{
			continue;
		}
		else
		{
			ok=0;
			break;
		}
	}
	if (ok)
	{
		return 1;
	}
	return 0;

}
int main()
{
	freopen("E:\\gcj\\input.txt","r",stdin);
	freopen("E:\\gcj\\ouput.txt","w",stdout);

	int T;
	cin >> T;
	for (int kk=1;kk<=T;++kk)
	{
		for (int i=0;i<4;++i)
		{
			cin >> mp[i];
		}
		int xwon=judge('X');
		int owon=judge('O');
		int complete=ok();
		if (xwon==1)
		{
			printf("Case #%d: X won\n",kk);
		}
		else if (owon==1)
		{
			printf("Case #%d: O won\n",kk);
		}
		else if (complete==1)
		{
			printf("Case #%d: Draw\n",kk);
		}
		else
		{
			printf("Case #%d: Game has not completed\n",kk);
		}
	}
	return 0;

}