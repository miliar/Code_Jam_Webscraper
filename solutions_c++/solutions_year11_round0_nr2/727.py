#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <cmath>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
using namespace std;
#define MM(a , x) memset(a , x , sizeof(a))
#define sqr(x) ((x) * (x))
#define abs(x) ((x > 0) ? (x) : -(x))
#define REP(i , n) for ((i) = 0; (i) < (n); ++(i))
#define FOR(i , a , b) for ((i) = (a); (i) <= (b); ++(i))
#define FORD(i , a , b) for ((i) = (a); (i) >= (b); --(i))
typedef long long LL;

int n , m , top , testcase , T , tot;
map<char , int> hasht;
int comb[108][108];
bool op[9][9];
int vis[108];
char str[108] , dic[108];
string st;

void init()
{
	MM(comb , 0); MM(op , 0); MM(str , 0);
	hasht.clear(); MM(dic , 0);
	tot = 8;
	hasht['Q'] = 1; hasht['W'] = 2; hasht['E'] = 3; hasht['R'] = 4;
	hasht['A'] = 5; hasht['S'] = 6; hasht['D'] = 7; hasht['F'] = 8;
	int i , j , k;
	cin >> k;
	FOR (i , 1 , k)
	{
		cin >> st;
		if (hasht.find(st[2]) == hasht.end())
		{
			hasht[st[2]] = ++tot;
			dic[tot] = st[2];
		}
		comb[hasht[st[0]]][hasht[st[1]]] = comb[hasht[st[1]]][hasht[st[0]]] = hasht[st[2]];
	}
	cin >> k;
	FOR (i , 1 , k)
	{
		cin >> st;
		op[hasht[st[0]]][hasht[st[1]]] = op[hasht[st[1]]][hasht[st[0]]] = 1;
	}
	cin >> n;
	cin >> st;
}

void work()
{
	top = 0; MM(vis , 0);
	int i , j , k;
	FOR (i , 0 , n - 1)
	{
		str[++top] = st[i];
		vis[hasht[str[top]]]++;
		if (top == 1) continue;
		int ch = comb[hasht[str[top]]][hasht[str[top - 1]]];
		if (ch != 0)
		{
			vis[hasht[str[top]]]--; vis[hasht[str[top - 1]]]--;
			vis[hasht[ch]]++;
			str[top--] = 0;
			str[top] = dic[ch];
			continue;
		}
		FOR (j , 1 , 8) if (vis[j] && op[hasht[st[i]]][j])
		{
			top = 0;
			MM(vis , 0); MM(str , 0);
			break;
		}
	}
	printf("Case #%d: [" , T);
	FOR (i , 1 , top)
	{
		if (i == 1) printf("%c" , str[i]); else printf(", %c" , str[i]);
	}
	printf("]\n");
}

int main()
{
	freopen("in.txt" , "r" , stdin);
	freopen("out.txt" , "w" , stdout);
	cin >> testcase;
	FOR (T , 1 , testcase)
	{
		init();
		work();
	}
	return 0;
}
