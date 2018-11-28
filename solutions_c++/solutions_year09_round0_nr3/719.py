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

char a[10000];
int z=19,n;
char pat[]="welcome to code jam";
int was[2][555];

int main()
{
	freopen("nut.txt","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&n);
	getchar();
	for (int i=0;i<n;i++)
	{
		gets(a);
		int res=0;
		int m=strlen(a);
		int y=0;
		for (int h=0;h<m;h++)
			if (a[h]==pat[0])
				was[y][h]=1;
		for (int j=1;j<z;j++,y^=1)
		{
			memset(was[y^1],0,sizeof(was[y^1]));
			for (int h=0;h<m;h++)
				if (a[h]==pat[j])
					for (int g=0;g<h;g++)
						if (a[g]==pat[j-1])
							was[y^1][h]=(was[y^1][h]+was[y][g])%10000;
		}
		for (int j=0;j<m;j++)
			res=(res+was[y][j])%10000;
		printf("Case #%d: %d%d%d%d\n",i+1,res/1000,res/100%10,res/10%10,res%10);
	}
	return 0;
}