#include <stdio.h>
#include<stdlib.h>
#include<time.h>

int N;
int turn;
int order[200][2];
int b, o;
int tot;

int nextPos(int bot)
{
	for(int i = turn; i < N; i++)
		if (order[i][0] == bot) return order[i][1];
	return -1;
}

int main()
{
	FILE *fin=fopen("input.txt","r");
	FILE *fout = fopen("output.txt","w");
	int T;
	fscanf(fin, "%d", &T);
	for(int aaa=1; aaa<=T; aaa++)
	{
		fscanf(fin, "%d", &N);
		for(int i = 0; i < N; i++)
		{
			char s;
			do{
				order[i][0]= fscanf(fin,"%c",&s);
			}while(s != 'O' && s != 'B');
			order[i][0] = (int)s;
			fscanf(fin, "%d", &order[i][1]);
		}
		b=o=1;
		tot=0;
		for(turn = 0;turn < N;turn++)
		{
			int bnext = nextPos((int)'B');
			int onext = nextPos((int)'O');
			bool ok = false;

			for(;!ok;tot++)
			{
				if(bnext == b)
				{
					if(order[turn][0] == 'B')
						ok = true;
				}
				else if(bnext < b)
					b--;
				else b++;

				if(onext == o)
				{
					if(order[turn][0] == 'O')
						ok = true;
				}
				else if(onext < o)
					o--;
				else o++;
			}
		}
		fprintf(fout, "Case #%d: %d\n", aaa, tot);
	}

	return 0;
}
