#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<string>

#define FF(i, a, b) for (int i=a; i<=b; i++)
#define FI(i, a, b) for (int i=a; i>=b; i--)

using namespace std;

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	string s = "yhesocvxduiglbkrztnwjpfmaq";
	int n;
	scanf("%d\n", &n);
	FF(i, 1, n)
	{
		string t;
		getline(cin, t);
		FF(j, 0, (int)t.size() - 1)
			if (t[j] != ' ')
				t[j] = s[t[j] - 'a'];
		cout << "Case #" << i << ": " << t << endl;
	}
	return 0;
}
