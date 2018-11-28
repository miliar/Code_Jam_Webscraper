#include<iostream>
#include<string>
#include<sstream>
using namespace std;

const int maxl = 500 + 10;
const string wel = "welcome to code jam";
const int len = 19;
const int rest = 10000;
int d[len][maxl], T;
char a[maxl];

int main()
{
	freopen("p3.in", "r", stdin);
	freopen("p3.out", "w", stdout);
	scanf("%d\n", &T);
	for (int t = 1; t <= T; t++)
	{
		printf("Case #%d: ", t);
		string z;
		getline(cin, z);
		for (int i = 0; i < z.size(); i++) 
			d[0][i] = (wel[0] == z[i]);
		int ans = 0;
		for (int i = 1; i < wel.size(); i++)
			for (int j = 0; j < z.size(); j++)
			{
				d[i][j] = 0;
				if (z[j] == wel[i])
					for (int k = 0; k < j; k++)
						d[i][j] += d[i - 1][k];
				d[i][j] %= rest;
				if (i == wel.size() - 1) ans += d[i][j];
			}
		ans %= rest;
		stringstream ss;
		ss << ans;
		string zz = ss.str();
		while (zz.size() < 4) zz = "0" + zz;
		cout << zz << endl;
	}
	return 0;
}
