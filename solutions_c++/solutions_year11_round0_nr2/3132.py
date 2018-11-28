#include<stdio.h>
#include<string.h>


char REPEAT[200][3], clr[200][2], str[200], ans[200];
int C, N, D, pos;
int rFLG[275], cFLG[275];

int AA(char a, char b)
{
	int i;

	for(i=0; i<C; i++)
	{
		if( (REPEAT[i][0]==a && REPEAT[i][1]==b) || (REPEAT[i][0]==b && REPEAT[i][1]==a) )
			return REPEAT[i][2];
	}
	return -1;
}

int BB(int sz)
{
	int i, j;
	for(i=0; i<sz; i++)
	{
		for(j=0; j<D; j++)
		{
			if( (clr[j][0]==ans[sz] && clr[j][1]==ans[i]) || (clr[j][1]==ans[sz] && clr[j][0]==ans[i]) )
				return 1;
		}
	}
	return 0;
}

void solve()
{
	int i, con;
	pos = 0;
	ans[0] = str[0];
	for(i=1; i<N; i++)
	{
		ans[++pos] = str[i];
		if(!pos)continue;
		con = 0;
		con = AA(ans[pos-1], ans[pos]);
		if( con >= 0)
		{
			ans[--pos] = con;
			continue;
		}
		if(BB(pos))
		{
			pos = -1;
			continue;
		}
	}
	ans[++pos] = '\0';
}


int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	//freopen("input.txt", "r", stdin);

	int t, i,len,cs = 1;

	scanf("%d", &t);

	while(t--)
	{
		scanf("%d", &C);

		for(i=0; i<270; i++)
			rFLG[i] = cFLG[i] = 1;

		for(i=0; i<C; i++)
		{
			scanf("%s", REPEAT[i]);
			rFLG[REPEAT[i][0]] = 0;
			rFLG[REPEAT[i][1]] = 0;
		}
		scanf("%d", &D);
		for(i=0; i<D; i++)
		{
			scanf("%s", clr[i]);
			cFLG[clr[i][0]] = 0;
			cFLG[clr[i][1]] = 0;
		}
		scanf("%d%s", &N, str);
		if(!C && !D)
		{
			printf("Case #%d: [", cs++);
			len = strlen(str);
			for(i=0; i<len; i++)
			{
				if(i==len-1)
					printf("%c", str[i]);
				else 
					printf("%c, ", str[i]);
			}
			printf("]\n");
			continue;
		}
		solve();

		printf("Case #%d: [", cs++);

		len = strlen(ans);
		for(i=0; i<len; i++)
		{
			if(i==len-1)
				printf("%c", ans[i]);
			else 
				printf("%c, ", ans[i]);
		}
		printf("]\n");
	}
	return 0;
}