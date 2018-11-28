#include <stdio.h>
#include<stdlib.h>
#include<time.h>

int C,D,N;
char stack[200];
int stack_cnt;
char clist[100][5];
char dlist[100][5];
char invoke[200];

void combine(char a)
{
	stack_cnt--;
	stack[stack_cnt-1] = a;
}

void clear()
{
	stack_cnt = 0;
}

int main()
{
	FILE *fin=fopen("input.txt","r");
	FILE *fout = fopen("output.txt","w");
	int T;
	fscanf(fin, "%d", &T);
	for(int aaa=1; aaa<=T; aaa++)
	{
		fscanf(fin, "%d", &C);
		for(int i = 0; i < C; i++)
			fscanf(fin,"%s",clist[i]);
		fscanf(fin, "%d", &D);
		for(int i = 0; i < D; i++)
			fscanf(fin,"%s",dlist[i]);
		fscanf(fin, "%d", &N);
		fscanf(fin,"%s",invoke);

		stack_cnt=0;
		for(int i = 0; i < N; i++)
		{
			char topush = invoke[i];
			stack[stack_cnt++] = topush;
			if(stack_cnt > 1)
			{
				for (int j = 0; j < C; j++)
				{
					if(stack[stack_cnt-2] == clist[j][0] && topush == clist[j][1]
					|| stack[stack_cnt-2] == clist[j][1] && topush == clist[j][0])
					{
						combine(clist[j][2]);
						goto hell;
					}
				}
				for (int j = 0; j < D; j++)
				{
					for(int k = 0; k < stack_cnt -1; k++)
					{
						if(stack[k] == dlist[j][0] && topush == dlist[j][1]
						|| stack[k] == dlist[j][1] && topush == dlist[j][0])
						{
							clear();
							goto hell;
						}
					}
				}
			}
			hell:0;
		}
		if(stack_cnt > 0)
		{
			fprintf(fout, "Case #%d: [%c", aaa, stack[0]);
			for(int i = 1; i < stack_cnt; i++)
				fprintf(fout,", %c", stack[i]);
			fprintf(fout,"]\n");
		}
		else fprintf(fout, "Case #%d: []\n", aaa);
	}

	return 0;
}
