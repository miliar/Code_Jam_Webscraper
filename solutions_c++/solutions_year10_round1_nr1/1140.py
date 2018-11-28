#include <iostream>
char str[200][200];
char rotate[200][200];
int b[200];
using namespace std;
bool istrue(int n, int k, char c)
{
	int i, j, kk;
	for(i = 0; i < n; i ++)
	{
		for(j = 0; j < n; j ++)
		{
			if(rotate[i][j] == c)
			{
				if(i + k - 1 < n)
				{
					for(kk = 0; kk < k; kk ++)
					{
						if(rotate[i + kk][j] != c)
							break;
					}
					if(kk == k)
						return true;
				}

				if(j + k - 1 < n)
				{
					for(kk = 0; kk < k; kk ++)
					{
						if(rotate[i ][j + kk] != c)
							break;
					}
					if(kk == k)
						return true;
				}
				
				if(i + k - 1 < n && j + k - 1 < n)
				{
					for(kk = 0; kk < k; kk ++)
					{
						if(rotate[i + kk ][j + kk] != c)
							break;
					}
					if(kk == k)
						return true;
				}


				if(i + k - 1 < n && j - k + 1 >= 0)
				{
					for(kk = 0; kk < k; kk ++)
					{
						if(rotate[i + kk ][j - kk] != c)
							break;
					}
					if(kk == k)
						return true;
				}
			}
		}
	}
	return false;
}
int main()
{
	int t, i, j, k, n, temp,cas = 0;
	//freopen("A-small.in","r", stdin);
	freopen("A-large.in","r", stdin);
	freopen("A.out", "w", stdout);
	scanf("%d", &t);
	while(t--)
	{
		scanf("%d %d", &n, &k);
		for(i = 0; i < n; i ++)
		{
			scanf("%s", &str[i]);
		}
		for(i = 0; i < n; i ++ )
		{
			for(j = 0; j < n; j ++)
			{
				rotate[j][n - 1 - i] = str[i][j];
			}
		}
// 		cout<<endl;
// 		for(i = 0; i < n; i ++)
// 			printf("%s\n", rotate[i]);
		memset(b, -1, sizeof(b));
		for(i = n - 1; i >= 0; i --)
		{
			for(j = 0; j < n; j ++)
			{
				if(rotate[i][j] == '.' && b[j] == -1)
					b[j] = i;
				if(rotate[i][j] != '.' && b[j] != -1)
				{
					rotate[b[j]][j] = rotate[i][j];
					rotate[i][j] = '.';
					b[j] --;
				}
			}
		}
	//	for(i = 0; i < n; i ++)
 	//		printf("%s\n", rotate[i]);
		bool flag_b, flag_r;
		flag_b = flag_r = false;
		flag_b = istrue(n, k, 'B');
		flag_r = istrue(n, k, 'R');
		if(!flag_b && !flag_r)
			printf("Case #%d: Neither\n", ++cas);
		else if(flag_b && flag_r)
			printf("Case #%d: Both\n", ++cas);
		else if(flag_b)
			printf("Case #%d: Blue\n", ++cas);
		else 
			printf("Case #%d: Red\n", ++cas);
		
		
	}
}