#include<cstdio>
#include<cstring>
const int maxn = 60;
char c[maxn][maxn];
char temp[maxn][maxn];

int find(int n , int k)
{
	int i , j , l;
/*
	printf("\n");
	for(i = 0;i < n;i++)
	{
		for(j = 0;j < n;j++)
			printf("%c" , c[i][j]);
		printf("\n");
	}
*/

	bool red = false;
	bool black = false;
	for(i = 0;i < n;i++)
		for(j = 0;j < n;j++)
			if(c[i][j] == 'R')
			{
				for(l = 0;l < k && i + l < n;l++)
					if(c[i + l][j] != 'R') break;
				if(l == k) red = true; 
				for(l = 0;l < k && j + l < n;l++)
					if(c[i][j + l] != 'R') break;
				if(l == k) red = true;
				for(l = 0;l < k && i + l < n && j + l < n;l++)
					if(c[i + l][j + l] != 'R') break;
				if(l == k) red = true; 
				for(l = 0;j < k && i - l >= 0 && j + l < n;l++)
					if(c[i - l][j + l] != 'R') break;
				if(l == k) red = true; 
			}
			else
			{
				for(l = 0;l < k && i + l < n;l++)
					if(c[i + l][j] != 'B') break;
				if(l == k) black = true; 
				for(l = 0;l < k && j + l < n;l++)
					if(c[i][j + l] != 'B') break;
				if(l == k) black = true;
				for(l = 0;l < k && i + l < n && j + l < n;l++)
					if(c[i + l][j + l] != 'B') break;
				if(l == k) black = true; 
				for(l = 0;l < k && i - l >= 0 && j + l < n;l++)
					if(c[i - l][j + l] != 'B') break;
				if(l == k) black = true; 
			}
	if(red && black) return 2;
	if(!red && !black) return 3;
	if(red) return 0;
	return 1;
}

void rote(int n)
{
	int i , j;
	for(i = 0;i < n;i++)
		for(j = 0;j < n;j++)
			c[i][j] = temp[n - 1 - j][i];
	for(i = 0;i < n;i++)
	{
		int left = n - 1, right = n - 1;
		while(left >= 0)
		{
			if(c[left][i] != '.') c[right--][i] = c[left][i];
			left--;
		}
		while(right >= 0)
		{
			c[right][i] = '.';
			right--;
		}
	}
}

int main()
{
//	freopen("A-small-attempt2.in.txt" , "r" , stdin);
//	freopen("1.txt" , "w" , stdout);
	int t , p;
	scanf("%d" , &t);
	for(p = 1;p <= t;p++)
	{
		int n , k;
		scanf("%d%d\n" , &n , &k);
		int i , j;
		for(i = 0;i < n;i++)
		{
			for(j = 0;j < n;j++)
				scanf("%c" , &temp[i][j]);
			scanf("%*c");
		}
		rote(n);
		printf("Case #%d: " , p);
		int ret = find(n , k);
		if(ret == 0) printf("Red\n");
		if(ret == 1) printf("Blue\n");
		if(ret == 2) printf("Both\n");
		if(ret == 3) printf("Neither\n");
	}
	return 0;
}