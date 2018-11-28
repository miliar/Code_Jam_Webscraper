#include<cstdio>
#include<cstring>
#include<string>
#include<sstream>
#include<set>
using namespace std;
int base[10];
int f[10][1000001];
int n;
int cal(int b, int num )
{
	int ans = 0;
	while (num)
	{
		int digit = num % b;
		ans += digit * digit;
		num /= b;
	}
	return ans;
}
int stack[100000];
bool check(int b, int num)
{
	int s = 0;
	set<int> hash;
	hash.insert(num);
	while (!f[b - 1][num])
	{
		stack[s++] = num;
		num = cal(b , num);
		if (hash.find(num) != hash.end()) break;
		hash.insert(num);
	}
	bool ans;
	if (f[b - 1][num] == 1) ans = true; else ans = false;
	for (int i = 0; i < s; ++i) f[b - 1][stack[i]] = ans ? 1 : 2;
	return ans;
}
void init()
{
	for (int b = 3; b <= 10; ++b)
		{
			f[b - 1][1] = 1;
			for (int i = 2; i <= 100000; ++i)
				check(b, i);
		}

}
char str[10000];
int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	init();
	int cases;
	scanf("%d" , &cases); gets(str);
	for (int ca = 1; ca <= cases; ++ca)
	{
		gets(str);
		string s(str);
		istringstream in(s);
		n = 0;
		int tmp;
		while (in >> tmp) if (tmp != 2) base[n++] = tmp;
		for (int i = 2; i <= 1000000; ++i)
		{
			bool ok = true;
			for (int j = 0; j < n && ok; ++j)
				if (f[base[j] - 1][i] == 2) ok = false;
			if (ok)
			{
				printf("Case #%d: %d\n", ca , i);
				break;
			}
		}
	}
}
