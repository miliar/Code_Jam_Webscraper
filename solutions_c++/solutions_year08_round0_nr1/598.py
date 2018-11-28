#include<cstdio>
#include<cstring>
#define INF 0x7fffffff
int ans,q,s;
int minimum[1000][2];
int choose[1000][2];
int f[1000][100];
char str[100][101];
char query[101];
int find()
{
	for (int i = 0; i < s; ++i)
		if (!strcmp(query, str[i])) return i;
	return -1;
}
void updata(int newvalue, int i, int j)
{
	if (newvalue < minimum[i][0])
	{
		minimum[i][1] = minimum[i][0];
		choose[i][1] = choose[i][0];
		minimum[i][0] = newvalue;
		choose[i][0] = j;
	} else if (newvalue < minimum[i][1])
	{
		minimum[i][1] = newvalue;
		choose[i][1] = j;
	}
}
int main()
{
	int n;
	scanf("%d",&n);
	for (int cases = 1; cases <= n; ++cases)
	{
		scanf("%d",&s); getchar();
		for (int i = 0; i < s; ++i) gets(str[i]);
		scanf("%d",&q); getchar();
		for (int i = 0; i < q; ++i) 
		{
			gets(query);
			int ban = find();
			f[i][ban] = INF;
			minimum[i][0] = minimum[i][1] = INF;
			if (!i)
			{
				for (int j = 0; j < s; ++j)
					if (j != ban)
					{
						f[i][j] = 0; updata(f[i][j],i,j);
					}
			}
			else
				for (int j = 0; j < s; ++j)
					if (j != ban)
					{
						f[i][j] = f[i - 1][j];
						int temp;
						if (j == choose[i - 1][0]) temp = minimum[i - 1][1]; else temp = minimum[i - 1][0];
						if (temp != INF && temp + 1 < f[i][j]) f[i][j] =  temp + 1;
						updata(f[i][j],i,j);
					}
			
		}
		printf("Case #%d: %d\n",cases,minimum[q - 1][0]);
	}
	
}
