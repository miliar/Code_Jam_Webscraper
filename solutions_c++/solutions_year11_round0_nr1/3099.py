#include<stdio.h>


int abs(int a)
{
	return (a>0)?a:-a;
}
long solve()
{
	long ans = 0;
	int n = 0;
	int da = 0, db = 0, pa = 1, pb = 1, pos;
	char ty;
	scanf("%d", &n);
	for(int i = 0; i < n ; i++)
	{
		while(1)
		{
			scanf("%c", &ty);
			if('B' == ty || 'O' == ty)
			{
				scanf("%d", &pos);
				break;
			}
		}
		if('B' == ty)
		{
			int t = abs(pos-pb) - db; 
			if(t > 0)
			{
				ans += t;
				da += t;
			}
			ans++;
			da++;
			pb = pos;
			db = 0;	
		}
		else
		{
			int t = abs(pos-pa) - da;
			if(t > 0)
			{
				ans += t;
				db += t;
			}
			ans++;
			db++;
			pa = pos;
			da = 0;
		}
	}
	return ans;
}

int main(int argc, char **argv)
{
	int ncase;

	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	scanf("%d", &ncase);
	for(int icase = 0; icase < ncase; icase++)
	{
		printf("Case #%d: %ld\n", icase+1, solve() );
	}	
		
	return 0;
}
