#include <iostream>
#include <string>
#include <vector>
int subset[100];
int hash[26];
using namespace std;
int main()
{
	int t, i, j, k, n, m, temp,cas = 0, len;
	freopen("C-small.in","r", stdin);
//	freopen("A-large.in","r", stdin);
	freopen("C.out", "w", stdout);
	scanf("%d", &t);
	int count = 0 ;
	while(t--)
	{
		count = 0;
		scanf("%d", &n);
		for(i = 0; i < (1 << (n - 2)); i ++)
		{
			len = 0;
			memset(hash, -1, sizeof(hash));
			for(j = 0; j < n - 2; j ++)
			{
				if(i & (1 << j))
				{
					subset[len ++] = j + 2;
				}
			}
			subset[len] = n;
			for(j = 0; j <= len; j ++)
			{
				hash[subset[j]] = j + 1;
			}
			int temp = n;
			while(1)
			{
				if(hash[temp] == -1)
					break;
				if(hash[temp] == 1)
				{
					count = (count + 1) % 100003;
					break;
				}
				temp = hash[temp];
			}
			
		}
		
		printf("Case #%d: %d\n", ++cas, count);
	}
}