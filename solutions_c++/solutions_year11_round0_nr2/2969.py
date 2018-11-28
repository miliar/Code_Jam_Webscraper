#include <stdio.h>
#include <string.h>

#define HASH(x) (x-'A')
#define MAX 30

void solve()
{
	int carr[MAX][2], darr[MAX], isin[MAX];
	int c, d, n;
	int ans[1000];
	int tail = 0;
	
	memset(carr, 0xff, sizeof(carr));
	memset(darr, 0xff, sizeof(darr));
	memset(isin, 0, sizeof(isin));
	
	scanf("%d", &c);
	for(int i = 0; i < c; i++)
	{
		char g, c, j;
		scanf(" %c%c%c", &g, &c, &j);
		g = HASH(g);
		c = HASH(c);
		j = HASH(j);
		
		carr[g][0] = c;
		carr[g][1] = j;
		
		carr[c][0] = g;
		carr[c][1] = j;
	}
	scanf("%d", &d);
	for(int i = 0; i < d; i++)
	{
		char g, c;
		scanf(" %c%c", &g, &c);
		g = HASH(g);
		c = HASH(c);
		
		darr[g] = c;
		darr[c] = g;
	}
	
	scanf("%d%*c", &n);
	
	tail = 0;
	for(int i = 0; i < n; i++)
	{
		char ch;
		scanf("%c", &ch);

		ch = HASH(ch);
		if(0 == tail)
		{
			ans[tail++] = ch;
			isin[ch]++;
			continue;
		}
		
		if(ch == carr[ans[tail-1]][0])
		{
			isin[ans[tail-1]]--;
			if(isin[ans[tail-1]] < 0) isin[ans[tail-1]] = 0;
			
			isin[ch]--;
			if(isin[ch] < 0) isin[ch] = 0;
	
			ch = carr[ch][1];
			tail--;
		}
		int flag = 1;
		for(int k = 0; tail > 0 && k < MAX; k++)
		{
			if(isin[k] && darr[k] == ch && ch != -1)
			{
				memset(isin, 0, sizeof(isin));
				tail = 0;
				flag = 0;
			}
		}
		if(flag)
		{
			ans[tail++] = ch;
			isin[ch]++;	
		} 
	}
	
	putchar('[');
	for(int i = 0; i < tail; i++)
	{
		if(0 !=  i) printf(", ");
		putchar(ans[i]+'A');
	}
	putchar(']');
}


int main(int argc, char **argv)
{
	int ncase;

	freopen("B-small-attempt0.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	scanf("%d", &ncase);
	for(int icase = 0; icase < ncase; icase++)
	{
		printf("Case #%d: ", icase+1);
		solve();
		printf("\n");
	}	
		
	return 0;
}
