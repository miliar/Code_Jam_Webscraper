#include<iostream>
#include<cmath>

using namespace std;

int po(int k)
{
	int res = 1;
	while(k)
	{
		res *= 2;
		k--;
	}
	return res;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int cas, icas;
	int n, k;
	scanf("%d", &cas);
	for(icas = 1; icas <= cas; icas++)
	{
		scanf("%d %d", &n, &k);
		int t = po(n);
		if((k+1)%t == 0)
			printf("Case #%d: ON\n", icas);
		else
			printf("Case #%d: OFF\n", icas);
	}
	return 0;
}