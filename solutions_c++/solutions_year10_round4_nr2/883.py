#include <stdio.h>

int most[2000];

int main()
{
	int ti, T, p, i,j, k , x;
	bool flag;
	freopen("b.txt", "r", stdin);
	freopen("b.out", "w", stdout);	
	scanf("%d", &T);
	for (ti=1; ti<=T; ti++)
	{
		scanf("%d", &p);
		for (i=0; i<1<<p; i++)
		  scanf("%d", &most[i]);
		for (i=0; i<p; i++)
		 for (j=0; j<(1<<i); j++)
		   scanf("%d", &x);
   		int ans=0;
		for (i=p-1; i>=0; i--)
		 for (j=0; j<(1<<i); j++)
		 {
		 	flag=false;
		 	for (k=0; k<(1<<p); k++)
		 	  if ((k>>(p-i))==j)
		 		if (most[k]+i<=p-1)
			 		flag=true;
		 	if (flag) ans++;
		 }
		 printf("Case #%d: %d\n",ti, ans);
	}
	return 0;
}
