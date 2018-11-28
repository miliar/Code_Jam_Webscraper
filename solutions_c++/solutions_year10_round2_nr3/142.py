#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <cstring>
#include <set>
#include <vector>
using namespace std;
#define VI vector<int>
#define PII pair<int,int>
#define MP make_pair
#define eps 1e-9
#define f0(i,n) for (i = 0; i < n; i++)



int n , m , k , i , j , p , t , x , tm;
int f[510][510];

int main()
{
	freopen("d:/input.txt" , "r" , stdin);
	freopen("d:/output.txt" , "w" , stdout);
	
	

	for (i = 0; i <= 505; i++)
		f[0][i] = 1;

	for (i = 1; i <= 505; i++)
	{
		for (j = 1; j <= 505; j++)
		{
			for (k = 1; k <= j && i - k >= 0; k++)
			{
				f[i][j] += f[i-k][j];
				f[i][j] %= 100003;
			}
		}
	}

	/*
	for (i = 0; i < 10; i++)
	{
		for (j = 0; j < 10; j++)
		cout<<f[i][j]<<" ";

		cout<<endl;
	}
	*/
	


	cin>>t;
	for (int tt = 1; tt <= t; tt++)
	{
		cin>>n;
		n--;
		cout<<"Case #"<<tt<<": ";
		
		int ans = 0;
		k = 0;
		while (n >= 0)
		{
			ans += f[n][k];
			n--;
			k++;
		}

		ans %= 100003;
		
		cout<<ans<<endl;
	}
	
	return 0;
}