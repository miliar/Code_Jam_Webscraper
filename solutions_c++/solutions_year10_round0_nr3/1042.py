#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
using namespace std;


int s;
int a[1002];
int r,k,n;

int get()
{
	int i;
	int spare = k;
	int ct = 0;

	for (i=s; ct < n;i++)
	{
		i = i % n;
		if (spare - a[i] >= 0)
		{
			spare -= a[i];
		}
		else break;
		ct++;
	
	}
	s=i%n;

	return k - spare; 
}

int main()
{

	int cas,ct=1;
	int i,j;


	int res[100002];
	int used[1002];

	//freopen("input.txt","r",stdin);
	freopen("C-small-attempt1.in","r",stdin);
	freopen("C-small-attempt1.out","w",stdout);

	scanf("%d",&cas);
	while (cas--)
	{
		scanf("%d%d%d",&r,&k,&n);


		for (i=0; i<n; i++)
		{
			scanf("%d",&a[i]);
		}

		memset(used,0,sizeof(used));

		s = 0;
		res[0] = 0;
		for (i=1; ; i++)
		{
			if (used[s]) break;
			else used[s] = i;
			res[i] = get();
		}
		
		int ls = used[s];
		int le = i-1;
		int loop = le - ls + 1;
		int loop_v = 0;
		for (i=ls; i<=le; i++) loop_v += res[i]; 

		int sum = 0;
		if (r < ls) 
		{
			for (i=1; i<=r;i++) sum += res[i];
		}
		else
		{
			for (i=1; i<ls; i++) sum += res[i];
			r -= ls;

		
			sum += loop_v * (r / loop);
			r %= loop;
			for (i=ls; i<=ls+r; i++) sum += res[i];
		}
		
		printf("Case #%d: ",ct++);
		printf("%d\n",sum);
	}

	return 0;
}