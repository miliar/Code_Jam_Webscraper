#include <stdio.h>
#include <string>
#include <cstring>

using namespace std;
#define character_num 129

int main()
{
	char com[character_num],com_out[character_num],opp[character_num];
	char exist[character_num];
	freopen("F:\\code\\topcoder\\compete\\compete\\codejam_2011\\B-small-attempt1.in","r",stdin);
	freopen("F:\\code\\topcoder\\compete\\compete\\codejam_2011\\result.txt","w",stdout);
	int t;
	scanf("%d",&t);
	int caseNum = 0;
	char buf[105];
	char res_buf[105],res;
	while (caseNum < t)
	{
		memset(com,-1,sizeof(com));
		memset(com_out,-1,sizeof(com_out));
		memset(opp,-1,sizeof(opp));
		memset(exist,0,sizeof(exist));
		int c,d,n;
		scanf("%d",&c);
		for (int i = 0;i<c;i++)
		{
			scanf("%s",buf);
			com[buf[0]] = buf[1];
			com_out[buf[0]] = buf[2];
			com[buf[1]] = buf[0];
			com_out[buf[1]] = buf[2];
		}
		scanf("%d",&d);
		for (int i = 0;i<d;i++)
		{
			scanf("%s",buf);
			opp[buf[0]] = buf[1];
			opp[buf[1]] = buf[0];
		}
		scanf("%d",&n);
		scanf("%s",buf);
		res = 0;
		char now;
		char badd = 0;
		for (int i = 0;i<n;i++)
		{
			badd = 0;
			now = buf[i];
			if (0 == res)
			{
				res_buf[res] = now;
				res++;
				exist[now]++;
			}
			else
			{
				while (res>0)
				{
					if (com[now] == res_buf[res-1])
					{
						exist[res_buf[res-1]]--;
						now = com_out[now];
						res--;
					}
					else if(opp[now]!=-1 && exist[opp[now]])
					{
						badd = 1;
						res = 0;
						memset(exist,0,sizeof(exist));
						break;
					}
					else
					{
						badd = 1;
						res_buf[res] = now;
						res++;
						exist[now]++;
						break;
					}
				}
				if (!badd)
				{
					res_buf[res] = now;
					res++;
					exist[now]++;
				}
			}
		}
		printf("Case #%d: [",caseNum+1);
		for (int i = 0;i<res;i++)
		{
			if (i<res-1)
			{
				printf("%c, ",res_buf[i]);
			}
			else
			{
				printf("%c",res_buf[i]);
			}
		}
		printf("]\n");
		caseNum++;
	}
}