#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <vector>
#include <string>
#include <queue>

using namespace std;

#define see(x) cout<<#x<<" "<<x<<endl
#define sp system("pause")

int belong[110];
int pos[110];

int main(int argc, char *argv[])
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.txt", "w", stdout);
	int t, T, n;
	scanf("%d", &T);
	for(t = 1; t <= T; ++t)
	{
		scanf("%d", &n);
		for(int i = 0; i < n; ++i)
		{
			char tmp1,tmp2;
			scanf("%c%c%d", &tmp1, &tmp2, &pos[i]);
			if(tmp2 == 'O')
				belong[i] = 0;
			else
				belong[i] = 1;
			//see(belong[i]);
			//see(pos[i]);
		}
		int prePos[2] = {1,1};
		int res = 0;
		int preTime = 0;
		int preBelong = -1;
		for(int i = 0; i < n; ++i)
		{
			if(preBelong !=-1 && preBelong != belong[i])
			{
				int temp = abs(pos[i] -prePos[belong[i]]);
				//see(temp);
				if(temp >= preTime)
				{
					int temp2 = temp;
					temp -= preTime;
					preTime = temp2 - preTime +1;
				}
				else
				{
					temp = 0;
					preTime = 1;
				}
				res += temp + 1;
			}
			else if(preBelong != -1 && preBelong == belong[i])
			{
				int temp = abs(pos[i] -prePos[belong[i]]);
				//see(temp);
				preTime += temp +1;
				res += temp +1;
			}
			if(preBelong == -1)
			{
				int temp = abs(pos[i] -prePos[belong[i]]);
				//see(temp);
				res += temp +1;
				preTime = temp +1;
			}
			prePos[belong[i]] = pos[i];
			preBelong = belong[i];
			//see(preBelong);
			//see(preTime);
			//see(res);
		}
		printf("Case #%d: %d\n", t, res);
	}	
	return 0;
}
