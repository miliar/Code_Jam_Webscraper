#include <iostream>
#include <string>
using namespace std;

const string p = "welcome to code jam";

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int T;
	scanf("%d\n", &T);
	for (int t = 1; t <= T; ++t)
	{
		string st;
		getline(cin, st);
		int f[600][30] = {};
		for (int i = 0; i <= st.length(); ++i)
			f[i][0] = 1;
		for (int i = 1; i <= st.length(); ++i)
			for (int j = 1; j <= p.length(); ++j)
			{
				f[i][j] = f[i-1][j];
				if (st[i-1] == p[j-1]) f[i][j] += f[i-1][j-1];
				f[i][j] %= 10000;
			}
		cout << "Case #" << t << ": ";
		int ans = f[st.length()][p.length()];
		if (ans < 10) cout << "000";
		else if (ans < 100) cout << "00";
		else if (ans < 1000) cout << "0";
		cout << ans << endl;
	}
	fclose(stdin);
	fclose(stdout);
}