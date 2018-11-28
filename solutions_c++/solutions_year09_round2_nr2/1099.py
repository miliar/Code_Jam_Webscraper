#include <iostream>
#include <memory.h>

using namespace std;

int a[10], b[10];
int p[25];
int len;

void read()
{
	char s[25];
	memset(s, 0, 25);
	gets(s);

	len = 0;
	for (int i = 0; s[i] != 0; i++, len++)
		p[i] = s[i] - '0';

	for (int i = 0; i < len / 2; i++ )
	{
		int x = p[i];
		p[i] = p[len - i - 1];
		p[len - i - 1] = x;
	}
}

void write()
{
	for (int i = len - 1; i >= 0; i--)
		cout << p[i];
}

void sort(int r)
{
	if (r < 2)
		return;

	memset(a, 0, sizeof(a));
	for (int i = 0; i < r; i++)
		a[p[i]] ++;

	int cur = 1;
	while (a[cur] == 0)
		cur++;

	int l = 0;
	if (r == len)
	{
		p[len] = cur;
		p[len - 1] = 0;
		a[cur] --;

		len ++;
		r --;
	}

	cur = 0;
	for (int i = r - 1; i >= 0; i--)
	{
		while (a[cur] == 0)
			cur ++;

		p[i] = cur;
		a[cur] --;
	}
}

int get_next(int r, int x)
{
	int min = 10;
	for (int i = 0; i < r; i++)
	{
		if (p[i] < min && p[i] > x)
			min = p[i];
	}

	return min;
}

void _swap(int r, int x)
{
	for (int i = 0; i < r; i++)
	{
		if (p[i] == x)
		{
			p[i] = p[r];
			p[r] = x;
			return;
		}
	}
}

int main()
{
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);

	int n;
	scanf("%d\n", &n);

	for(int i = 0; i < n; i++)
	{
		read();

		if (i == 340)
			i = 340;
		int cur;
		for (cur = 1; cur < len; cur++)
			if (p[cur] < p[cur - 1])
				break;

		if (cur == len)
		{
			sort(len);
			cout << "Case #" << i + 1 << ": ";
			write();
			cout << endl;
			continue;
		}

		_swap(cur, get_next(cur, p[cur]));
		sort(cur);

		cout << "Case #" << i + 1 << ": ";
		write();
		cout << endl;
	}
	return 0;
}