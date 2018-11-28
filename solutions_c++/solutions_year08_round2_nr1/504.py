#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<map>
using namespace std;

#ifndef ONLINE_JUDGE
#include<fstream>
  ifstream in("A-small-attempt0.in.txt");
  ofstream out("a.out");
#define cin in
#define cout out
#endif

#define maxn  100001
int mapa[maxn],mapb[maxn];
int main()
{
	int cs;
	cin>>cs;
	for(int ct = 1; ct <= cs; ct ++)
	{
		cout << "Case #"<<ct<<": ";

		int n;
		int a,b,c,d,x0,y0,m;
		
		cin >> n;
		cin >> a>>b>>c>>d;
		cin >> x0>>y0>>m;

		int x = x0, y = y0;
		mapa[0] = x;
		mapb[0] = y;

		for(int i = 1; i <= n-1; i ++)
		{
			long long temp1 = x;
			long long temp2 = y;

			temp1 = (temp1 * a + b ) % m;
			temp2 = (temp2 * c + d) % m;

			mapa[i] = x = temp1;
			mapb[i] = y = temp2;
		}

		long long ans = 0;
		for(int i = 0; i < n - 2; i ++)
			for(int j = i + 1; j < n-1; j++)
				for(int k = j + 1; k < n; k ++)
				{
					if( (mapa[i] + mapa[j] + mapa[k] ) % 3 == 0 && (mapb[i] + mapb[j] + mapb[k] ) % 3 == 0)
						ans ++;
				}

		cout << ans << endl;

	}
}
