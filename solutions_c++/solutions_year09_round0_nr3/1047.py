//
//  untitled
//
//  Created by  on 2009-09-03.
//  Copyright (c) 2009 __MyCompanyName__. All rights reserved.
//

#include <string>
#include <vector>
#include <map>
#include <set>
#include <iostream>
#include <sstream>
#include <list>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>

using namespace std;

typedef long long LL;
typedef vector <int> VI;
typedef vector <double> VD;
typedef vector <vector<int> > VVI;
typedef pair <int,int> PII;
typedef pair <int,PII> PIII;
typedef vector <LL> VL;
typedef vector <string> VS;

int dp[1000][50];
char msg[] = "welcome to code jam";
int main()
{
	int n;
	scanf("%d\n", &n);
	int msg_len = strlen(msg);
	for(int line = 0; line < n; ++line)
	{
		char buf[1000];
		gets(buf);
		int buf_len = strlen(buf);
		int ret = 0;
		memset(dp,0,sizeof(dp));
		for(int k = 0; k < msg_len; ++k)
		{
			for(int i = 0; i < buf_len; ++i)
			{
				if (buf[i] == msg[k]) {
					if (k == 0) {
						dp[i][k] = 1;
					} else {
						for(int j = 0; j < i; ++j)
						{
							dp[i][k] = (dp[i][k] + dp[j][k-1]) % 10000;
						}
					}
				}
			}
		}
		ret = 0;
		for(int i = 0; i < buf_len; ++i)
		{
			ret = (ret + dp[i][msg_len-1]) % 10000;
		}
		printf("Case #%d: %04d\n", line+1, ret);
	}
	return 0;
}