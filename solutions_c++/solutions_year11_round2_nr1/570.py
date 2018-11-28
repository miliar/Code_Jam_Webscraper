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
#define nextLine() { for (int c = getchar(); c != '\n' && c != EOF; c = getchar()); }
#define sqr(a) ((a)*(a))
#define has(mask,i) (((mask) & (1<<(i))) == 0 ? false : true)
using namespace std;

#define pii pair<int,int>
#define mp make_pair
#define pb push_back
typedef long long LL;
typedef long double ldb;

const int inf = (1 << 30) - 1;
const ldb eps = 1e-9;

int n;
char a[105][105];
void Load()
{
	scanf("%d", &n);
	nextLine();
	for (int i = 0; i < n; i++)
		gets(a[i]);
}

inline ldb countWp(int t)
{
	int wg = 0, ag = 0;
	for (int i = 0; i < n; i++)
	{
		if (a[t][i] == '1')
		{
			wg++;
			ag++;
		}
		if (a[t][i] == '0')
			ag++;
	}
	ldb wp = (ag == 0 ? 0 : (ldb)wg / ag);
	return wp;
}

inline ldb countOwp(int t)
{
	int opc = 0;
	ldb owp = 0;
	for (int i = 0; i < n; i++)
		if (a[t][i] != '.')
		{
			int cur = a[t][i] - '0';
			a[t][i] = a[i][t] = '.';
			opc++;
			owp += countWp(i);
			a[t][i] = char('0' + cur);
			a[i][t] = char('0' + (cur ^ 1));
		}
	if (opc > 0)	
		owp /= opc;
	return owp;	
}

inline ldb count(int t)
{
	ldb wp = countWp(t);
	ldb owp = countOwp(t);
	ldb oowp = 0;
	int oowc = 0;
	for (int i = 0; i < n; i++)
		if (a[t][i] != '.')
		{
			oowc++;
			oowp += countOwp(i);
		}
	if (oowc > 0)
		oowp /= oowc;
	//cerr << "team = " << t << " oowp = " << oowp << endl;
	return 0.25 * wp + 0.50 * owp + 0.25 * oowp;
}

void Solve()
{
	for (int i = 0; i < n; i++)
	{
		if (i > 0)
			cout << "\n";
		cout << count(i);
	}
}

int main()
{
	int nt;
	scanf("%d", &nt);
	cout.setf(ios::fixed|ios::showpoint);
	cout.precision(12);
	for (int tt = 1; tt <= nt; tt++)
	{ 
		Load();
		printf("Case #%d:\n", tt);
		Solve();
		printf("\n");
	}	
	return 0;
}
