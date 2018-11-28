#include <iostream>
using namespace std;

struct node
{
	char c;
	int num;
};
int T, N;
node Op[101];
int Ora[101];
int Blu[101];
int o, b;
void solve()
{
	int res = 0, brtime = 1, ortime = 1;
	int Orange = 1, Blue = 1;
	for (int i=0; i<N; i++)
	{
		if (Op[i].c == 'O')
		{
			if(ortime< o)
				ortime++;
			int temp = abs(Op[i].num - Orange) + 1;
			res += temp;
			if (brtime< b)
			{
				int tmp = abs(Blue -  Blu[brtime]);
				if(temp >= tmp)
					Blue = Blu[brtime];
				else 
				{
					if (Blue > Blu[brtime])
						Blue -= temp;
					else Blue += temp;
				}
			}
			Orange = Op[i].num;
		}
		if (Op[i].c == 'B')
		{
			if(brtime< b)
				brtime++;
			int temp = abs(Op[i].num - Blue) + 1;
			res += temp;
			if (ortime< o)
			{
				int tmp = abs(Orange -  Ora[ortime]);
				if(temp >= tmp)
					Orange = Ora[ortime];
				else 
				{
					if (Orange > Ora[ortime])
						Orange  -= temp;
					else Orange += temp;
				}
			}
			Blue = Op[i].num;
		}
	}
	printf("%d\n", res);	
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	memset(Op, 0, sizeof(Op));
	memset(Ora, 0, sizeof(Ora));
	memset(Blu, 0, sizeof(Blu));

	scanf("%d", &T);
	for ( int i=1; i<=T; i++ )
	{
		scanf("%d", &N);
		o = 1, b = 1;
		for(int j=0; j<N; j++)
		{
			getchar();
			scanf("%c%d", &Op[j].c, &Op[j].num);
			if (Op[j].c == 'O')
				Ora[o++] = Op[j].num;
			else Blu[b++] = Op[j].num;
		}
		printf("Case #%d: ", i);
		solve();
	}
//	while(1);
	return 0;
}