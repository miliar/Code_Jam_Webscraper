#include <iostream>
#include <string>
#include <string.h>
#include <stdio.h>
using namespace std;

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.txt","w",stdout);
	int b[2][101];
	int num[2][101];
	int N,T;
	scanf("%d",&T);
	int cas = 0;
	while(T--)
	{
		scanf("%d",&N);
		b[0][0] = b[1][0] = num[0][0] = num[1][0] = 0;
		char cc[4];
		int tmp;
		for(int i=1;i<=N;i++)
		{
			scanf("%s%d",cc,&tmp);
			if(cc[0] == 'O')
			{
				b[0][++b[0][0]] = tmp;
				num[0][++num[0][0]] = i;
			}
			else
			{
				b[1][++b[1][0]] = tmp;
				num[1][++num[1][0]] = i;
			}
		}
		int pos_o = 1,pos_b = 1;
		int now_o = 1,now_b = 1;
		int cnt = 1;
		int ans = 0;
		while(cnt <= N)
		{
			bool flag = false;
			if(now_o <= b[0][0])
			{
				if(pos_o == b[0][now_o] && cnt == num[0][now_o])
				{
					now_o++;
					cnt++;
					flag = true;
				}
				else if(pos_o < b[0][now_o]) pos_o++;
				else if(pos_o > b[0][now_o]) pos_o--;
			}
			if(now_b <= b[1][0])
			{
				if(pos_b == b[1][now_b] && cnt == num[1][now_b] && !flag)
				{
					now_b++;
					cnt++;
				}
				else if(pos_b < b[1][now_b]) pos_b++;
				else if(pos_b > b[1][now_b]) pos_b--;
			}
			ans++;
		}
		printf("Case #%d: %d\n",++cas,ans);
	}
	return 0;
}
