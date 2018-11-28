#include <cstdio>
#include <cstring>
#include <iostream>
#include <string>

using namespace std;

#define forn(i, n) for (i = 0; i < (int)(n); ++i)

char W[] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int n, i, k, j;
	scanf("%d\n", &n);
	string str;
	forn(i, n) {
		getline(cin, str);
		cout << "Case #" << i + 1 << ": ";
		k = str.length();
		forn(j, k) {
			if (str[j] == ' ')
				cout << ' ';
			else
				cout << W[str[j] - 'a'];
		}
		cout << endl;
	}

	return 0;
}