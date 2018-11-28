#include <stdio.h>
#include <memory.h>
#include <string.h>
#define N 101
#define M 1000
char words[M][N];
int pw;
int child[M][M];
int pchild[M];

char slice[N][N];
int ps;

int n, m;



int split(char *str, char c)
{
	int pos = 0;
	int index = 0;

	while(*str)
	{
		if(*str == c) {
			slice[pos][index] = 0;
			pos++;
			index = 0;
		} else {
			slice[pos][index++] = *str;		
		}
		str++;
	}
	slice[pos][index] = 0;
	pos++;
	return pos;
}

int mk(int node, int k)
{
	int i;
	if(k >= ps) return 0;

	for(i = 0; i < pchild[node]; i++)
	{
		if(strcmp(words[child[node][i]], slice[k]) == 0)
		{
			break;
		}
	}

	if(i < pchild[node])	{
		return mk(child[node][i], k + 1);
	} else {
		strcpy(words[pw], slice[k]);
		child[node][pchild[node]] = pw;
		pchild[pw] = 0;

		pw++;
		pchild[node]++;
		
		return mk(child[node][i], k + 1) + 1;
	}
}

int insert(char *path)
{
	ps = split(path, '/');	
	return mk(0, 1);
}

int main()
{
	freopen("A-small.in.txt", "r", stdin);
	freopen("A-small.out.txt", "w", stdout);
	//freopen("A-large.in.txt", "r", stdin);
	//freopen("A-large.out.txt", "w", stdout);

	int t, i, j;
	int sum = 0;
	char one[N];
	scanf("%d", &t);
	for(i = 0; i < t; i++)
	{
		scanf("%d %d", &n, &m);
		pchild[0] = 0;
		pw = 1;		
		for(j = 0; j < n; j++)
		{
			scanf("%s", one);
			insert(one);
		}

		sum = 0;
		for(j = 0; j < m; j++)
		{
			scanf("%s", one);
			sum += insert(one);			
		}
		
		printf("Case #%d: %d\n", i + 1, sum);
		
	}
	return 0;
}