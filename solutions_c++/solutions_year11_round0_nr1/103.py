#include<cstdio>
#include<cstring>
#include<vector>
#include<cmath>
#include<algorithm>
using namespace std;

int main()
{
//	freopen("1.txt" , "r" , stdin);
//	freopen("2.txt" , "w" , stdout);
	int t;scanf("%d" , &t);
	int ii = 0;
	while(t--)
	{
		ii++;
		int n;
		scanf("%d" , &n);
		int i;
		int ret = 0;
		int apos = 1;
		int acan = 0;
		int bpos = 1;
		int bcan = 0;
		for(i = 0;i < n;i++)
		{
			char c[3];
			int x;
			scanf("%s%d" , &c , &x);
			if(c[0] == 'O')
			{
				int temp = abs(x - apos);
				if(temp <= acan)
				{
					ret++;
					bcan ++;
				}
				else
				{
					ret += temp - acan + 1;
					bcan += temp - acan + 1;
				}
				acan = 0;
				apos = x;
			}
			else 
			{
				int temp = abs(x - bpos);
				if(temp <= bcan)
				{
					ret++;
					acan ++;
				}
				else
				{
					ret += temp - bcan + 1;
					acan += temp - bcan + 1;
				}
				bcan = 0;
				bpos = x;
			}
		}
		printf("Case #%d: %d\n" , ii , ret);
	}
	return 0;
}