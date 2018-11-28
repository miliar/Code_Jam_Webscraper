#include <iostream>

using namespace std;

const int MAXN = 10100;

int m, v, s[MAXN], c[MAXN], f[MAXN][2];

void init()
{
	int i;
	scanf("%d %d", &m, &v);
	for (i=1; i<=(m-1)/2; i++)
		scanf("%d%d", &s[i], &c[i]);		
	for (i=(m-1)/2+1; i<=m; i++)
		scanf("%d", &s[i]);	
}

void update(int &a, int x)
{
	if (x!=-1 && (a==-1 || a>x))
		a=x;	
}

int min(int a, int b)
{
	if (a==-1) return b; else
	if (b==-1) return a; else	
	if (a<b) return a; else return b;
}


void work()
{
	int i;
	
	memset(f, 0xFF, sizeof(f));	
	for (i=m; i>(m-1)/2; i--)
		f[i][s[i]]=0;
	for (i=(m-1)/2; i>=1; i--){
		if (s[i]==0){
			if (f[i*2][1]!=-1 || f[i*2+1][1]!=-1) {
				if (f[i*2][1]!=-1)
					update(f[i][1], f[i*2][1]+min(f[i*2+1][0], f[i*2+1][1]));
				if (f[i*2+1][1]!=-1)
					update(f[i][1], f[i*2+1][1]+min(f[i*2][0], f[i*2][1]));
			}
			if (f[i*2][0]!=-1 && f[i*2+1][0]!=-1)
				update(f[i][0], f[i*2][0]+f[i*2+1][0]);
		}
		else
		{
			if (f[i*2][0]!=-1 || f[i*2+1][0]!=-1) {
				if (f[i*2][0]!=-1)
					update(f[i][0], f[i*2][0]+min(f[i*2+1][0], f[i*2+1][1]));
				if (f[i*2+1][0]!=-1)
					update(f[i][0], f[i*2+1][0]+min(f[i*2][0], f[i*2][1]));
			}
			if (f[i*2][1]!=-1 && f[i*2+1][1]!=-1)
				update(f[i][1], f[i*2][1]+f[i*2+1][1]);
		}
		if (c[i]==1){
			if (s[i]==1){
				if (f[i*2][1]!=-1 || f[i*2+1][1]!=-1) {
					if (f[i*2][1]!=-1)
						update(f[i][1], f[i*2][1]+min(f[i*2+1][0], f[i*2+1][1])+1);
					if (f[i*2+1][1]!=-1)
						update(f[i][1], f[i*2+1][1]+min(f[i*2][0], f[i*2][1])+1);
				}
				if (f[i*2][0]!=-1 && f[i*2+1][0]!=-1)
					update(f[i][0], f[i*2][0]+f[i*2+1][0]+1);
			}
			else
			{
				if (f[i*2][0]!=-1 || f[i*2+1][0]!=-1) {
					if (f[i*2][0]!=-1)
						update(f[i][0], f[i*2][0]+min(f[i*2+1][0], f[i*2+1][1])+1);
					if (f[i*2+1][0]!=-1)
						update(f[i][0], f[i*2+1][0]+min(f[i*2][0], f[i*2][1])+1);
				}
				if (f[i*2][1]!=-1 && f[i*2+1][1]!=-1)
					update(f[i][1], f[i*2][1]+f[i*2+1][1]+1);
			}			
				
		}
	}

	if (f[1][v]==-1)
		printf("IMPOSSIBLE\n");
	else
		printf("%d\n", f[1][v]);
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int cas=0, t;
	scanf("%d", &t);
	while (t--){
		cas++;
		printf("Case #%d: ", cas);
		init();
		work();
	}
	
	return 0;
}
