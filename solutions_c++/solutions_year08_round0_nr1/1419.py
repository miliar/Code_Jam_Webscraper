#include <stdio.h>
#include <memory.h>
#include <string.h>
int main()
{
	char engine[100][101];
	bool flag[100];
	char query[101];
	int ncase;
	int pcase;
	int s;
	int q;
	int lcount;
	int nswitch;
	int i, j;
	scanf("%d", &ncase);
	for (pcase = 1; pcase <= ncase; pcase++)
	{
		nswitch = 0;
		scanf("%d", &s);
		gets(engine[0]);
		for (i = 0; i < s; i++)
		{
			gets(engine[i]);
		}
		lcount = 0;
		scanf("%d", &q);
		gets(query);
		memset(flag , false , sizeof(bool) * 100);
		for (i = 0; i < q; i++)
		{
			gets(query);
			for (j = 0; j < s; j++)
			{
				if (strcmp(query, engine[j]) == 0)
				{
					if (!flag[j]) lcount++;	//�µ�һ�����ų���
					flag[j] = true;
					break;
				}
			}
			if (lcount == s)	//�ų���s��Ҫ�л�һ��
			{
				nswitch++;
				memset(flag, false, sizeof(bool) * 100);
				lcount = 1;
				flag[j] = true;	//�����л�������
			}
		}
		printf("Case #%d: %d\n", pcase, nswitch);
	}
	return 0;
}