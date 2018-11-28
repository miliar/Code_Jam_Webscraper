#include <cstdlib>  
#include <cctype>  
#include <cstring>  
#include <cstdio>  
#include <cmath>  
#include <algorithm>  
#include <vector>  
#include <string>  
#include <iostream>  
#include <sstream>  
#include <map>  
#include <set>  
#include <queue>  
#include <stack>  
#include <fstream>  
#include <numeric>  
#include <iomanip>  
#include <bitset>  
#include <list>  
#include <stdexcept>  
#include <functional>  
#include <utility>  
#include <ctime>  
using namespace std;  

#define PB push_back  
#define MP make_pair  

#define REP(i,n) for(i=0;i<(n);++i)  
#define FOR(i,l,h) for(i=(l);i<=(h);++i)  
#define FORD(i,h,l) for(i=(h);i>=(l);--i)  
#define CLOCK cout << "Clock " << (double)clock()/CLOCKS_PER_SEC << endl
const int maxs = 1003;

int main()
{
	freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
	int t;
	scanf("%d",&t);
	getchar();
	char chess[4][10];
	for(int cases=1;cases<=t;cases++)
	{
		for (int i=0;i<4;i++)	scanf("%s",chess[i]);
		bool flag1 = true;
		for (int i=0;i<4;i++)
		{
			flag1 = true;
			for (int j=0;j<4;j++)
			{
				if(chess[i][j] != 'X' && chess[i][j] != 'T')
				{flag1 = false;break;}
			}
			if (flag1) break;
			flag1 = true;
			for (int j=0;j<4;j++)
			{
				if(chess[j][i] != 'X' && chess[j][i] != 'T')
				{flag1 = false;break;}
			}
			if (flag1) break;
			flag1 = true;
			for (int j=0;j<4;j++)
				if (chess[j][j] != 'X' && chess[j][j] != 'T')
					{flag1 = false;break;}
			if (flag1) break;
			flag1 = true;
			for (int j=0;j<4;j++)
				if (chess[j][3-j] != 'X' && chess[j][3-j] != 'T')
					{flag1 = false;break;}
			if (flag1) break;
		}
		bool flag2 = true;
		for (int i=0;i<4;i++)
		{
			flag2 = true;
			for (int j=0;j<4;j++)
			{
				if(chess[i][j] != 'O' && chess[i][j] != 'T')
				{flag2 = false;break;}
			}
			if (flag2) break;
			flag2 = true;
			for (int j=0;j<4;j++)
			{
				if(chess[j][i] != 'O' && chess[j][i] != 'T')
				{flag2 = false;break;}
			}
			if (flag2) break;
			flag2 = true;
			for (int j=0;j<4;j++)
				if (chess[j][j] != 'O' && chess[j][j] != 'T')
					{flag2 = false;break;}
			if (flag2) break;
			flag2 = true;
			for (int j=0;j<4;j++)
					if (chess[j][3-j] != 'O' && chess[j][3-j] != 'T')
						{flag2 = false;break;}
			if (flag2) break;
		}
		printf("Case #%d: ",cases);
		if (flag1)
			printf("X won\n");
		else if(flag2)
			printf("O won\n");
		else 
		{
			bool flag = true;
			for (int i=0;i<4;i++)
			{
				for (int j=0;j<4;j++)
				{
					if (chess[i][j] == '.')
					{
						flag = false;break;
					}
				}
			}
			if (flag) printf("Draw\n");
			else printf("Game has not completed\n");
		}
	}
	return 0;
}