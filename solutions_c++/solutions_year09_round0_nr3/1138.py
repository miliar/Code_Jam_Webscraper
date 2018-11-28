#include <iostream>

using namespace std;

int ts;

int f[512][20];

char s1[] = "^welcome to code jam";
char s2[10000];

void solve()
{
	memset( f, 0, sizeof f );
	gets(s2 + 1);
	f[0][0] = 1;
	cerr <<(s2+1)<<endl;
	
	int n = (int)strlen(s2+1);
	
	for (int i = 1; i <= (int)strlen(s2+1); i++) for (int j = 0; j <= 19; j++)
	{
		f[i][j] = f[i-1][j];
		if (s1[j] == s2[i]) {
			f[i][j] += f[i-1][j-1];
		}
		//cout << i << ' ' << j << " = " << f[i][j] << endl;
		f[i][j] %= 10000;
	}
	
	printf("Case #%d: %04d\n", ++ts, f[n][19]);
}

int main()
{
	int t; cin >> t; 
	char s[100]; gets(s);
	for (int i = 0; i < t; i++) solve();
	return 0;
}