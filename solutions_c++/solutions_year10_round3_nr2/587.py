#include <cstring>           
#include <iostream>              
#include <vector>         
#include <algorithm>      
using namespace std;  

int a[32],b[32];
int main ( )
{
	freopen("B-small-attempt1.in","r",stdin);
	freopen("A.out","w",stdout);
	int tCase;
	scanf("%d", &tCase);
	for(int t = 1; t <= tCase; t++)
	{
		int ans = 0, max = 0;
		int l, p, c, k = 0;
		scanf("%d%d%d", &l, &p, &c);
		while( l*c  < p)
		{
			l *= c;
			ans ++;
		}
		if (ans != 0)
		{
			int tl = 1;
			int cou = 0;
			while(tl <= ans) 
			{
				tl *= 2;
				cou++;
			}
			printf("Case #%d: %d\n", t, cou);
		}
		else printf("Case #%d: %d\n", t, ans);

	}
	return 0;
}