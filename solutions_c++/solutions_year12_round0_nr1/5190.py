//TC Accretia Code Template
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <bitset>
#include <sstream>
#include <string>

#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>

#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

#define FILL(arr,n) memset(arr,n,sizeof(arr))
#define FORUP(i,m,n) for(int i=(m); i<(n); i++)
#define FORDOWN(i,m,n) for(int i=(m)-1; i>=(n); i--)

#define PB push_back
#define MP make_pair
#define F first
#define S second

#define INF 2000000000
#define EPS 1e-11
#define PI acos(-1.0)
using namespace std;

typedef long long ll;
typedef pair<int,int> pii;
typedef vector<pii> vii;

map<char,char> dict;
void fill_dict()
{
	dict['a'] = 'y';
	dict['b'] = 'h';
	dict['c'] = 'e';
	dict['d'] = 's';
	dict['e'] = 'o';
	dict['f'] = 'c';
	dict['g'] = 'v';
	dict['h'] = 'x';
	dict['i'] = 'd';
	dict['j'] = 'u';
	dict['k'] = 'i';
	dict['l'] = 'g';
	dict['m'] = 'l';
	dict['n'] = 'b';
	dict['o'] = 'k';
	dict['p'] = 'r';
	dict['q'] = 'z';
	dict['r'] = 't';
	dict['s'] = 'n';
	dict['t'] = 'w';
	dict['u'] = 'j';
	dict['v'] = 'p';
	dict['w'] = 'f';
	dict['x'] = 'm';
	dict['y'] = 'a';
	dict['z'] = 'q';
	dict[' '] = ' ';
}

int
main()
{
	int T;
	scanf("%d\n",&T);
	string str;
	fill_dict();
	for(int tc = 1;tc <= T;tc++)
	{
		str.clear();
		getline (cin,str);
		printf("Case #%d: ",tc);
		for(int i = 0;i < str.size();i++)
		{
			printf("%c",dict[str[i]]);
		}
		printf("\n");
	}
return 0;
}