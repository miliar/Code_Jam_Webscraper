#include<iostream>
using namespace std;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("ans.out","w",stdout);
	int runs, n, k, m, cas = 1;
	for(cin >> runs; cas <= runs; cas++)
	{
		cin>>n>>k;
		m = 1;
		for(int i = 1; i <= n; i++)
			m*=2;
		if(k%m==m-1)
			printf("Case #%d: ON\n", cas);
		else
			printf("Case #%d: OFF\n",cas);
	}
}
