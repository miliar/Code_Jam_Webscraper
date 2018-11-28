#include <iostream>
#include <cstdio>

using namespace std;

int A[26][26], B[26][26], C[26];
char S[10000];
int m;

char GetC()
{
	char x = ' ';
	while (x < 'A' || x > 'Z')
		cin >> x;
	return x;
}

void add(char x)
{
	S[m] = x;
	m++;
	C[x - 'A']++;
}

void del()
{
	m--;
	C[S[m] - 'A']--;
}

void clear()
{
	m = 0;
	for (int i = 0; i < 26; i++)
		C[i] = 0;
}

void Add(char x)
{
	add(x);
	while (m > 1 && A[S[m - 1] - 'A'][S[m - 2] - 'A'] >= 0)
	{
		char z = 'A' + A[S[m - 1] - 'A'][S[m - 2] - 'A'];
		del();
		del();
		add(z);
	}
	for (int i = 0; i < 26; i++)
		if (B[S[m - 1] - 'A'][i] == 0 && C[i] > 0)
			clear();
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	int I = 0;
	while (t--)
	{
		I++;
		cout << "Case #" << I << ": ";
		int n;
		for (int i = 0; i < 26; i++)
			for (int j = 0; j < 26; j++)
			{
				A[i][j] = -1;
				B[i][j] = -1;
			}
		cin >> n;
		while (n--)
		{
			char x = GetC(), y = GetC(), z = GetC();
			A[x - 'A'][y - 'A'] = z - 'A';
			A[y - 'A'][x - 'A'] = z - 'A';
		}
		cin >> n;
		while (n--)
		{
			char x = GetC(), y = GetC();
			B[x - 'A'][y - 'A'] = 0;
			B[y - 'A'][x - 'A'] = 0;
		}
		for (int i = 0; i < 26; i++)
			C[i] = 0;
		cin >> n;
		m = 0;
		while (n--)
		{
			char x = GetC();
			Add(x);
		}
		cout << "[";
		for (int i = 0; i < m; i++)
		{
			if (i > 0) cout << ", ";
			cout << S[i];
		}
		cout << "]" << endl;
	}
	return 0;
}