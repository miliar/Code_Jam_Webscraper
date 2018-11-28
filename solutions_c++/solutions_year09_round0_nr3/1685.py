#include<iostream>
#include<fstream>

using namespace std;

int main()
{
	fstream inf("c.in");
	ofstream ouf("c.out");
	const int bn = 19;
	int n, tc, an, i, j, k, tmp, ans;
	char a[510];
	const char b[256] = "welcome to code jam";
	int f[510][30];
	inf>>n;
	inf.getline(a, 100000);
	for (tc = 1; tc <= n; tc++) {
		an = 0;
		inf.getline(a, 100000);
		an = strlen(a) + 1;
		for (i = 0; i < 510; i++)
		 for (j = 0; j < 30; j++)
			f[i][j] = 0;
		for (i = 0; i < 30; i ++)
			f[i][0] = 1;
		for (i = 1; i <= an; i++)
		{
			tmp = i;
			if (tmp > bn) tmp = bn;
			for (j = 1; j <= tmp; j ++)	{
				f[i][j] = f[i - 1][j];
				if (a[i - 1] == b[j - 1]) f[i][j] += f[i - 1][j - 1];
				f[i][j] = f[i][j] % 10000;
			}		
		}
		ans = f[an][bn];
		ouf<<"Case #"<<tc<<": "<<ans / 1000<<ans%1000/100<<ans%100/10<<ans%10<<endl;
	}
	inf.close();
	ouf.close();
}