#include<stdio.h>
#include<algorithm>
using namespace std;

char s[50][50];
int num[50], n;

int ok(int inx[])
{
	for(int i = 0; i < n; i++)
		if(num[inx[i]] > i) return -1;
	int ans = 0;
	for(int i = 0; i < n; i++)
		for(int j = 0; j < i; j++)
			if(inx[j] > inx[i]) ans++;
			
	return ans;
}

int main()
{
	int tcse;
	freopen("ain.txt", "r", stdin);
	freopen("aout.txt", "w", stdout);
	scanf("%d", &tcse);
	for(int i = 1; i <= tcse; i++)
	{
		scanf("%d", &n);
		for(int j = 0; j < n; j++)
		{
			 scanf("%s", s[j]);
			 int k = n-1;
			 while(k >= 0 && s[j][k] == '0') k--;
			 num[j] = k;
			 
		}
	//	for(int j = 0; j < n; j++) printf("%d ", num[j]);
		//printf("\n");
		int inx[50];
		for(int j = 0; j < n; j++) inx[j] = j;
		int ans = 100000000;
		do 
		{
			int tmp = ok(inx);
			if(tmp < ans && tmp != -1)
			{
				ans = tmp;
			}
		}while(next_permutation(inx, inx+n));
		
		printf("Case #%d: %d\n", i, ans);
	}
	return 0;
}
