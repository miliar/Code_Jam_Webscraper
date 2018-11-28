#include<iostream>
using namespace std;
int main()
{
	freopen("A.in", "r", stdin);	
	freopen("A.out", "w", stdout);
	int t, n, k, i, ii, j;
	int c[32]={0};
	c[0]=1;
	for(i=1; i<=30; i++)
		c[i]=2*c[i-1];
	char st[2][4]={"OFF", "ON"};
	bool f;
	scanf("%d\n", &t);
	for(ii=1; ii<=t; ii++)
	{
		scanf("%d %d\n", &n, &k);
		f=0;
		if(k%(c[n])==c[n]-1)
			f=1;
		printf("Case #%d: %s\n", ii, st[f]);
	}
	return 0;
}