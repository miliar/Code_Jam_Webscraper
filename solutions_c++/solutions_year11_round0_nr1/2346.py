#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<queue>
#define MAXL 110
using namespace std;


typedef struct node
{
	char c;
	int num;
}node;

node info[MAXL];

int main()
{
	int a,b,i,j;
	int T;
	int n;
	int t = 0;
	int sum;
	int temp;
	int b_pos[MAXL];
	int o_pos[MAXL];
	int b_cnt,o_cnt;
	int pre_b,pre_o;
	int move_b,move_o;
	char s[3];
	char now;
	FILE *fin = fopen("A-large.in","r");
	FILE *fout = fopen("A-large.txt","w");
	fscanf(fin,"%d",&T);
	while(T--)
	{
		o_cnt = 0;
		b_cnt = 0;
		pre_b = 1;
		pre_o = 1;
		move_b = 0;
		move_o = 0;
		sum = 0;
		fscanf(fin,"%d",&n);
		for(i=0;i<n;i++)
		{
			fscanf(fin,"%s %d",s,&a);
			info[i].c = s[0];
			info[i].num = a;
			if(s[0] == 'B')
				b_pos[b_cnt++] = i;
			else if(s[0] == 'O')
				o_pos[o_cnt++] = i;
		}
		for(i=0;i<n;i++)
		{
			now = info[i].c;
			if(now == 'B')
			{
				if( abs(info[i].num - pre_b) > move_o)
				{
					temp = abs(info[i].num - pre_b) - move_o + 1;
					move_b += temp;
					sum += temp;
					move_o = 0;
					pre_b = info[i].num;
				}
				else
				{
					sum++;
					move_b++;
					move_o = 0;
					pre_b = info[i].num;
				}
			}
			else
			{
				if( abs(info[i].num - pre_o) > move_b)
				{
					temp = abs(info[i].num - pre_o) - move_b + 1;
					move_o += temp;
					sum += temp;
					move_b = 0;
					pre_o = info[i].num;
				}
				else
				{
					sum++;
					move_o++;
					move_b = 0;
					pre_o = info[i].num;
				}
			}
		}
		fprintf(fout,"Case #%d: %d\n",++t,sum);
	}
	return 0;
}
