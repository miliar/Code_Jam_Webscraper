#include <iostream>
#include <string>
#include <vector>

using namespace std;
typedef vector <int> vi;
typedef vector <vi> vvi;

string s = "welcome to code jam";
vvi mem;
char a[1000];
int alen = 0;

int func(int i, int j)
{
	if (i >= s.length())
		return 1;

	if (j >= alen || alen - j < s.length() - i)
		return 0;

	if (mem[j][i] != -1)
		return mem[j][i];

	int res = 0;
	res += func(i, j + 1);
	if (s[i] == a[j])
		res += func(i + 1, j + 1);

	return mem[j][i] = res % 10000;
}

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int N;
	scanf("%d\n", &N);

	int t = 0;
	while (t < N)
	{
		gets(a);
		alen = strlen(a);

		mem.clear();
		mem.resize(alen, vi(s.length(), -1));

		cout << "Case #" << t + 1 << ": ";
		printf("%04d\n", func(0, 0));
		t++;
	}
	return 0;
}