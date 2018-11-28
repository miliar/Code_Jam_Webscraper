#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;
#define forn(i, n) for(int i = 0; i < (int)(n); ++i)

int z[600][60];

string ob = "welcome to code jam";
string line;
int n, sz;

void main()
{
	freopen("inp.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d\n", &n);
	for(int it = 1; it <= n; ++it)
	{
		getline(cin, line);
		memset(z, 0, sizeof z);
		int len = line.size();
		forn(i, len)
			if(line[i] == 'w')
				z[i][0] = 1;
		sz = ob.size();
		for(int cur = 1; cur < sz; ++cur)
			forn(i, len)
				if(line[i] == ob[cur])
				{
					int s = 0;
					forn(j, i + 1)
					{
						s += z[j][cur - 1];
						s %= 10000;
					}
					z[i][cur] = s;
				}
		int ans = 0;
		forn(i, len)
		{
			ans += z[i][sz - 1];
			ans %= 10000;
		}

		char str[10];
		itoa(ans, str, 10);
		cout << "Case #" << it << ": ";
		forn(i, 4 - strlen(str))
			cout << 0;
		forn(i, strlen(str))
			cout << str[i];
		cout << endl;	 	
	}
}