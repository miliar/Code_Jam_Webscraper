#include<stdio.h>

int orange[200][2], blue[200][2];
int no, nb;
int poso, posb;

int iabs(int a)
{
	return a > 0 ? a : -a;
}

int next(int stat, int goal, int time)
{
	int ret;
	if(iabs(goal - stat) <= time)
		return goal;
	else
		return stat + ((goal - stat) / iabs(goal - stat)) * time;
}
int get_ans(int N)
{
	poso = 1; posb = 1;
	int to, tb, step, time = 0, t;
	to = 0; tb = 0;
	for(step = 0; step < N; step ++)
	{
		if(to < no && orange[to][1] == step)
		{
			t = iabs(orange[to][0] - poso) + 1;
			time = time + t;
			poso = orange[to][0];
			if(tb != nb)
				posb = next(posb, blue[tb][0], t);
			to ++;
		}
		else
		{
			t = iabs(blue[tb][0] - posb) + 1;
			time = time + t;
			posb = blue[tb][0];
			if(to != no)
				poso = next(poso, orange[to][0], t);
			tb ++;
		}
//		printf("poso = %d posb = %d, time = %d, to = %d tb = %d\n", poso, posb, time, to, tb);
	}
	
	return time;
}

int main()
{
    int T, test, N, i, ans;
    char c;
    scanf("%d", &T);
    for(test = 1; test <= T; test ++)
    {
    	scanf("%d", &N);
    	no = 0;
		nb = 0;
    	for(i = 0; i < N; i ++)
    	{
			while(c = getchar(), c != 'O' && c != 'B');
			if(c == 'O')
			{
				scanf("%d", orange[no] + 0);
				orange[no][1] = i;
				no ++;
			}	
			else
			{
				scanf("%d", blue[nb] + 0);
				blue[nb][1] = i;
				nb ++;
			}
		}
//		for(i = 0; i < no; i ++)
//			printf("%d %d     o\n", orange[i][0], orange[i][1]);
//		for(i = 0; i < nb; i ++)
//			printf("%d %d     b\n", blue[i][0], blue[i][1]);
		ans = get_ans(N);
		printf("Case #%d: %d\n", test, ans);
    }
    return 0;
}
