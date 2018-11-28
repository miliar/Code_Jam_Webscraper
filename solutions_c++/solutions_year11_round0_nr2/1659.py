#pragma comment(linker, "/STACK:10000000")
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <set>
#include <map>
#include <cstdio>
#include <cassert>
#include <string>
#include <cstring>
#define ldb long double
#define LL long long
#define fi first
#define se second
#define fill(a, c) memset(a, c, sizeof(a))
#define sqr(a) ((a) * (a))
#define nextLine() {int c = 0; while((c = getchar()) != 10 && c != EOF);}
#define getBit(mask, k) (((mask) / pw[k]) % pw[1])
#define setBit(mask, k, l) (((mask) / pw[k + 1] * pw[1] + (l)) * pw[k] + ((mask) % pw[k]))
#define debug(a) cerr << #a << " = " << a << " ";
#define debugl(a) cerr << #a << " = " << a << "\n";
const ldb LDINF = 9128739847123.00;
const ldb eps = 1e-9;
const int INF = 1 << 28;
const ldb pi = fabsl(atan2(0.0, -1.0));
using namespace std;

int n;
int opposed[256][256];
int form[256][256];
string s;

void Load()
{
	int C, D;
	cin >> C;
	memset(form, -1, sizeof form);
	memset(opposed, 0, sizeof opposed);
	char c1, c2, c3;
	for (int i = 0; i < C; i++)
	{
		cin >> c1 >> c2 >> c3;
		form[c1][c2] = c3, form[c2][c1] = c3;
	}
	cin >> D;
	for (int i = 0; i < D; i++)
	{
		cin >> c1 >> c2;
		opposed[c1][c2] = opposed[c2][c1] = 1;
	}
	int N;
	cin >> N;
	cin >> s;
}
int st[100000];
int cnt[256];
int size;


void Push(int c)
{
	st[size++] = c;
	cnt[c]++;
	while (size > 1 && form[st[size - 2]][st[size - 1]] != -1)
	{
		cnt[st[size - 2]]--;
		cnt[st[size - 1]]--;
		st[size - 2] = form[st[size - 2]][st[size - 1]];
		cnt[st[size - 2]]++;
		size--;
	}
	bool notdone = true;
	for (int i = 'A'; notdone && i <= 'Z'; i++)
	{
		for (int j = i + 1; notdone && j <= 'Z'; j++)
		{
			if (cnt[i] > 0 && cnt[j] > 0 && opposed[i][j])
			{
				notdone = false;
				size = 0;
				memset(cnt, 0, sizeof cnt);
			}
		}
	}
}


void Solve(int Test)
{
	cout << "Case #" << Test << ": ";
	size = 0;
	memset(cnt, 0, sizeof cnt);
	int i;
	for (i = 0; i < s.size(); i++)
	{
		Push(s[i]);
	}
	cout << "[";
	for (i = 0; i < size; i++)
	{
		if (i > 0) cout << ", ";
		cout << (char)st[i];
	}
	cout << "]\n";
}

#define file "b"
int main()
{
	freopen(file".in", "rt", stdin);
	freopen(file".out", "wt", stdout);
	int T;
	cin >> T;
	int i;
	for (i = 0; i < T; i++)
	{
		Load();
		cerr << "Case #" << i + 1 << "\n";
		Solve(i + 1);
	}
	return 0;
}
