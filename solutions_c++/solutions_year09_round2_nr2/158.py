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

int t;
char s[33];
int mat[11];

int main()
{
	freopen("out.txt","r",stdin);
	freopen("nut.txt","w",stdout);
	scanf("%d",&t);
	for (int cas=1;cas<=t;cas++)
	{
		memset(mat,0,sizeof(mat));
		scanf("%s",s);
		int l=strlen(s);
		for (int i=0;i<l;i++)
			mat[s[i]-'0']++;
		if (!next_permutation(s,s+l))
		{
			int ml=0;
			for (int i=1;i<10;i++)
				if (mat[i]&&!ml)
				{
					ml=i;
					mat[i]--;
				}
			l++;
			for (int i=0;i<l;i++)
				s[i]='0';
			s[l]=0;
			s[0]='0'+ml;
			int go=l-1;
			for (int j=9;j>=1;j--)
				while (mat[j])
				{
					mat[j]--;
					s[go--]='0'+j;
				}
		}
		printf("Case #%d: %s\n",cas,s);
	}
	return 0;
}