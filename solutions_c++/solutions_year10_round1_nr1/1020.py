#include <iostream>
#include <cstring>
using namespace std;

const int maxN = 100;

int T, N, K;
char g[maxN][maxN];

void work(int p)
{
	int i, j, k, t;
	char str[maxN], R[maxN], B[maxN];
	bool Rwin, Bwin;
	
	for(i=0; i<K; i++)
	{
		R[i] = 'R';
		B[i] = 'B';
	}
	R[K] = B[K] = 0;
	Rwin = Bwin = 0;
	for(i=0; i<N; i++)
	{
		if(!Rwin && strstr(g[i], R) != NULL) Rwin = true;
		if(!Bwin && strstr(g[i], B) != NULL) Bwin = true;
		if(Rwin && Bwin) break;
	}
	for(i=0; i<N; i++)
	{
		for(j=0; j<N; j++)
			str[j] = g[j][i];
		str[N] = 0;
		if(!Rwin && strstr(str, R) != NULL) Rwin = true;
		if(!Bwin && strstr(str, B) != NULL) Bwin = true;
		if(Rwin && Bwin) break;
	}
	
	for(i=0; i<N; i++)
		str[i] = g[i][i];
	str[N] = 0;
	if(!Rwin && strstr(str, R) != NULL) Rwin = true;
	if(!Bwin && strstr(str, B) != NULL) Bwin = true;
	
	for(i=0; i<N; i++)
		str[i] = g[i][N-i-1];
	str[N] = 0;
	if(!Rwin && strstr(str, R) != NULL) Rwin = true;
	if(!Bwin && strstr(str, B) != NULL) Bwin = true;
	
	for(i=1; i<N; i++)
	{
		if(N-i < K) break;
		
		j = 0;
		k = i;
		t = 0;
		memset(str, 0, sizeof(str));
		while(k<N)
		{
			str[t] = g[j][k];
			j++;
			k++;
			t++;
		}
		str[t] = 0;
		if(!Rwin && strstr(str, R) != NULL) Rwin = true;
		if(!Bwin && strstr(str, B) != NULL) Bwin = true;
		if(Rwin && Bwin) break;
		
		j = 0;
		k = i;
		t = 0;
		while(k<N)
		{
			str[t] = g[k][j];
			j++;
			k++;
			t++;
		}
		str[t] = 0;
		if(!Rwin && strstr(str, R) != NULL) Rwin = true;
		if(!Bwin && strstr(str, B) != NULL) Bwin = true;
		if(Rwin && Bwin) break;
	}
	
	for(i=N-2; i>=0; i--)
	{
		if(i+1 < K) break;
		
		j = i;
		k = 0;
		t = 0;
		while(j>=0)
		{
			str[t] = g[j][k];
			j--;
			k++;
			t++;
		}
		str[t] = 0;
		if(!Rwin && strstr(str, R) != NULL) Rwin = true;
		if(!Bwin && strstr(str, B) != NULL) Bwin = true;
		if(Rwin && Bwin) break;
		
		j = N-1-i;
		k = N-1;
		t = 0;
		
		while(j<N)
		{
			str[t] = g[j][k];
			j++;
			k--;
			t++;
		}
		str[t] = 0;
		if(!Rwin && strstr(str, R) != NULL) Rwin = true;
		if(!Bwin && strstr(str, B) != NULL) Bwin = true;
		if(Rwin && Bwin) break;
	}
	if(Rwin && Bwin)	printf("Case #%d: Both\n", p);
	else if(Rwin)	printf("Case #%d: Red\n", p);
			else if(Bwin)	printf("Case #%d: Blue\n", p);
					else	printf("Case #%d: Neither\n", p);
}

int main()
{
	freopen("1.in", "r", stdin);
	freopen("1.out", "w", stdout);
    int i, j, k, l;
	char str[maxN];
	scanf("%d", &T);
	for(i=0; i<T; i++)
	{
		scanf("%d%d", &N, &K);
		for(j=0; j<N; j++)
		{
			for(k=0; k<N; k++)
				g[j][k] = 'O';
			g[j][N] = 'O';
			g[N][j] = 'O';
		}
			
		for(j=0; j<N; j++)
		{
			scanf("%s", str);
			l = 0;
			for(k=N-1; k>=0; k--)
				if(str[k] == 'R' || str[k] == 'B')
				{
					g[j][l] = str[k];
					l++;
				}
		}
		work(i+1);
	}
	return 0;
}
