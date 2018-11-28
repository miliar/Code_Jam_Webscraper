#include <cstdio>

using namespace std;

int main()
{
	int casenum;
	int a[20];
	scanf("%d", &casenum);
	for (int ii=1; ii<=casenum; ii++)
	{
		printf("Case #%d: ", ii);
		int p, q, cnt = 0;
		scanf("%d%d", &p, &q);
		for (int i=p; i<=q; i++)
		{
			for (int j=0; j<10; j++)
				a[j] = 0;
			int n = i;
			int tmp = 0;
			int flag = 1;
			while (n>0)
			{
				a[tmp] = n%10;
				n /= 10;
				tmp++;
				flag *= 10;
			}
			flag /= 10; 
			for (int j=tmp-2; j>=0; j--)
			{
				int s = 0;
				for (int k=j; k>j-tmp; k--)
				{
					s *= 10;
					s += a[(k+tmp) % tmp];
				}
				if (s >= flag && s != i && s >= p && s <= q && s > i)
				{
					cnt++;
			//		printf("~~ %d: %d %d\n", cnt, i, s);
				}
			}
						
		}
		
		printf("%d\n", cnt);
		
		
	}
	
} 

