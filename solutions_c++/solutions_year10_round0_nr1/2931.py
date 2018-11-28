#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<algorithm>
#include<vector>
#include<cstring>

using namespace std;

int main()
{
	FILE* fin = freopen("in.txt", "r", stdin);
	FILE* fout = freopen("out.txt", "w", stdout);

	long long k;
	int t,n;
	cin >> t;
	for(int i=0;i<t;++i)
	{
		int res = 1;
		cin >> n >> k;

		for(int j=0;j<n;++j)
		{
			if(k%2==0){res=0;break;}
			k/=2;
		}
		cout << "Case #" << i+1 << ": ";
		if(res) cout << "ON\n";
		else cout << "OFF\n";
	}
}
