#include <iostream>
#include <cassert>
#include <cmath>
#include <string>
#include <cstring>
#include <vector>
#include <fstream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#define nextline { for (int c = getchar(); c != '\n' && c != EOF; c = getchar()); }
#define sqr(a) ((a)*(a))
#define has(mask,i) (((mask) & (1<<(i))) == 0 ? false : true)
using namespace std;

#define PII pair<int,int>
#define mp make_pair
#define pb push_back
typedef long long LL;
typedef long double ldb;

const int inf = (1 << 30) - 1;
const ldb eps = 1e-9;

int c;
int comb[30][30];
int d;
bool dest[30][30];
int n;
string inv;
void Load()
{
	memset(comb, -1, sizeof(comb));
	memset(dest, false, sizeof(dest));
	cin >> c;
	string s;
	for (int i = 0; i < c; i++)
	{
		cin >> s;
		comb[s[0] - 'A'][s[1] - 'A'] = s[2] - 'A';
		comb[s[1] - 'A'][s[0] - 'A'] = s[2] - 'A';
	}
	cin >> d;
	for (int i = 0; i < d; i++)
	{	
		cin >> s;
		dest[s[0] - 'A'][s[1] - 'A'] = true;
		dest[s[1] - 'A'][s[0] - 'A'] = true;
	}
	cin >> n;
	cin >> inv;
}

int st[100005];
void Solve()
{
	int sp = 0;
	for (int i = 0; i < n; i++)
	{
		st[sp++] = inv[i] - 'A';
		while (sp >= 2 && comb[st[sp - 2]][st[sp - 1]] != -1)
		{
			int ne = comb[st[sp - 2]][st[sp - 1]];
			sp -= 2;
			st[sp++] = ne;
		}
		for (int j = 0; j < sp - 1; j++)
			if (dest[st[j]][st[sp - 1]])
			{
				sp = 0;
				break;
			}
	}
	printf("[");
	for (int i = 0; i < sp; i++)
	{
		if (i > 0) printf(", ");
		printf("%c", st[i] + 'A');
	}
	printf("]");
}

int main()
{
	int nt;
	scanf("%d", &nt);
	for (int tt = 1; tt <= nt; tt++)
	{ 
		Load();
		printf("Case #%d: ", tt);
		Solve();
		printf("\n");
	}	
	return 0;
}
