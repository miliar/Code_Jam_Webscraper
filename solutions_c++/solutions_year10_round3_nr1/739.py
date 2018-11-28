#include <cstring>           
#include <iostream>              
#include <vector>         
#include <algorithm>      
using namespace std;  

int a[1000], b[1000];
int main ( )
{
	freopen("A-large.in","r",stdin);
	freopen("A.out","w",stdout);
	int tCase;
	scanf("%d", &tCase);
	for(int t = 1; t <= tCase; t++)
	{
		int ans = 0, n;
		scanf("%d", &n);
		for(int i = 0; i < n; i++)
			scanf("%d%d", &a[i], &b[i]);
		for(int i = 0; i < n - 1; i++)
			for(int j = i + 1; j < n; j++)
			{
				if(a[i] > a[j] && b[i] < b[j])
					ans ++;
				else if(a[i] < a[j] && b[i] > b[j])
					ans ++;
			}
		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}