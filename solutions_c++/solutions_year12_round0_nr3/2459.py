#include <iostream>
#include <cstring>
#include <cstdio>
#include <string>
#include <vector>
#include <set>
#include <algorithm>
using namespace std;

#define MAX 2000000
vector<int> arr[MAX];

void init()
{
	for(int i=1;i<=MAX;++i)
	{
		int cur_idx = -1;
		int num = i;
		char cur[16];
		sprintf(cur, "%d", num);
		int len = strlen(cur);
		for(int l=0;l<len-1;++l)
		{
			char nxt[16];
			sprintf(nxt,"%s%c",cur+1, cur[0]);
			strcpy(cur, nxt);
			if(nxt[0]=='0')
				continue;
			int num;
			sscanf(nxt, "%d", &num);
			if(num!=i)
				arr[i].push_back(num);
		}
	}

	for(int i=1;i<=MAX;++i)
	{
		sort(arr[i].begin(), arr[i].end());
		arr[i].resize(unique(arr[i].begin(), arr[i].end()) - arr[i].begin());
	}
}

int main()
{
	init();
	int tc;
	scanf("%d",&tc);
	for(int tt=0;tt<tc;++tt)
	{
		int a,b;
		scanf("%d %d", &a, &b);
		int num=0;
		for(int i=a;i<=b;++i)
		{
			for(int j=0;j<arr[i].size();++j)
			{
				if(arr[i][j] > i && arr[i][j] >= a && arr[i][j] <= b)
					++num;
			}
		}
		printf("Case #%d: %d\n", tt+1, num);
	}
	return 0;
}
