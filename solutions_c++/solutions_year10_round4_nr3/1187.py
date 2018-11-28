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
#include <ctime>

bool gr[105][105];
int row, col;
bool isOK()
{
	int i, j;
	for (i = 1; i <= row; ++i)
	{
		for (j = 1; j <= col; ++j)
		{
			if(gr[i][j])
				return false;
		}
	}
	return true;
}

void Solve()
{
	int i, j;
	bool temp[105][105];
	memset(temp,0,sizeof(temp));
// 	for (i = 1; i <= row; ++i)
// 		for(j =1 ; j <= col; ++j)
// 			temp[i][j] = gr[i][j];
	memcpy(temp, gr, 105*105*sizeof(bool));
	for (i = 1; i <= row; ++i)
	{
		for (j = 1; j <= col; ++j)
		{
			if(gr[i][j] && !temp[i-1][j] && !temp[i][j-1])
				gr[i][j] = 0;
			else if(!gr[i][j] && temp[i-1][j] && temp[i][j-1])
				gr[i][j] = 1;
		}
	}
}

int main()
{
	
	freopen("C-small-attempt0.in","r",stdin);freopen("C-small-output.txt","w",stdout);
	//freopen("B-small-attempt1.in","r",stdin);freopen("B-small-output.txt","w",stdout);
//	freopen("B-large.in","r",stdin);freopen("B-large-output.txt","w",stdout);

	int C, R,t;
	scanf("%d",&C);
	t = 1;
	while (C--)
	{
		scanf("%d",&R);
		int i, j, k, x1,x2,y1,y2, ret;
		ret = row = col = 0;
		memset(gr,0,sizeof(gr));
		for (i = 0; i < R; ++i)
		{
			scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
			if(row < y2)
				row = y2;
			if(col < x2)
				col = x2;
			for (j = y1; j <= y2; ++j)
				for (k = x1; k <=x2; ++k)
					gr[j][k] = 1;
		}
		while(true)
		{
			if(isOK())
				break;
			else
				Solve();
			ret++;
		}
		printf("Case #%d: %d\n",t++, ret);
	}
	return 0;
}
