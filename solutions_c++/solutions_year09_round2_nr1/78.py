#include <iostream>
#include <algorithm>
#include <cmath>
#include <cassert>
#include <vector>
#include <set>
#include <string>
#include <map>
#define ldb long double
#define LL long long
#define sqr(a) (a) * (a)
#define nextLine() {int c = 0; while((c = getchar()) != 10 && c != EOF);}
const ldb LDINF = 9128739847123.00;
const ldb eps = 1e-9;
const int INF = 2147483647 / 2;
#define ws ws2
using namespace std;

const int MAXN = 20000;

ldb prob[MAXN];
string feat[MAXN];
int l[MAXN];
int r[MAXN];
int L;
set <string> ws; 
int q;
int root;

int stack[MAXN];
int sz;


void Load()
{
	cin >> L;
	int i;
	root = 1;
	l[root] = 2;
	sz = 0;
	q = 0;
	int c;
	memset(l, 0xFF, sizeof(l));
	memset(r, 0xFF, sizeof(r));
	nextLine();
	for (i = 1; i <= L; i++)
	{
		while ((c = getchar()) != 10 && c != EOF)
		{
			if (c == '(')
			{
				q++;
				if (sz > 0)
				{
					l[stack[sz - 1]] = r[stack[sz - 1]];
					r[stack[sz - 1]] = q;
				}
				feat[q] = "";
				stack[sz++] = q;
				cin >> prob[q];
			}
			else if (c == ')')
			{
				sz--;
			}
			else if (c >= 'a' && c <= 'z')
			{
				feat[q] += c;
			}
		}
	}
	
	
}

string animal, feature;
ldb res;

void go(int t)
{
	res *= prob[t];
	if (l[t] == 0 || r[t] == 0)
	{
		return;
	}                 
	else if (feat[t] != "")
	{
		if (ws.find(feat[t]) != ws.end())
		{
			go(l[t]);
		}
		else
		{
			go(r[t]);
		}
	}
}

void Solve(int Test)
{
	int M, K;
	cin >> M; 
	int i;
	cout << "Case #" << Test << ":\n";
	cout.setf(ios::fixed|ios::showpoint);
	cout.precision(10);
	int j;
	for (i = 1; i <= M; i++)
	{
		cin >> animal;
		cin >> K;
		res = 1.0;
		ws.clear();
		for (j = 1; j <= K; j++)
		{
			cin >> feature;
			ws.insert(feature);
		}
		go(1);
		cout << res << "\n"; 
	}
}

#define file "a"
int main()
{
	freopen(file".in", "rt", stdin);
	freopen(file".out", "wt", stdout);
	int T;
	cin >> T;
	int i;
	for (i = 1; i <= T; i++)
	{
		Load();
		Solve(i);
	}
	return 0;
}