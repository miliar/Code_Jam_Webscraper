#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <math.h>
#include <sstream>
#include <ctype.h>
#include <queue>
#include <stack>
#include <fstream>
using namespace std;

#define debug(x) cout << #x << "=" << x << endl;

template<class Item>
void display(vector<Item> v)
{
	for(int i=0; i<v.size(); i++)
		cout << v[i] << ' ';
	cout << '\n';
}

string out(__int64 n)
{
	string ret = "";
	string flag = n<0 ? "-" : "";
	n = n < 0 ? -n : n;
	do
	{	char c = (n%10) + '0';
		ret = c + ret;
		n /=10;
	}
	while(n);
	return flag + ret;
}

template<class Item>
Item min(Item a, Item b)
{
	return a < b ? a : b;
}

int H, W, R;
int MOD = 10007;

int table[101][101];

set< pair<int, int> > bad;

int dp(int x, int y)
{
	if(x> H) return 0;
	if(y > W) return 0;
	if(x==H) return y==W;
	pair<int, int> p;
	p.first = x; p.second = y;
	if(bad.find(p)!= bad.end() ) return 0;

	if(table[x][y] > -1) return table[x][y];

	table[x][y] = (dp(x+2, y+1) + dp(x+1, y+2) ) % MOD;

	return table[x][y];
}
 
int main()
{

int G;
fstream In("d-small.in", ios::in);
fstream Out("d-small.out", ios::out);

In >> G;

for(int h=1; h<=G; h++)
{

bad.clear();
Out << "Case #" << h << ": ";

In >> H >> W >> R;

H--; W--;

for(int i=0; i<R; i++)
{
	int a, b;
	In >> a >> b;
	bad.insert(make_pair(a-1, b-1));
}

memset(table, -1, sizeof(table));

Out << dp(0, 0) << endl;

}


In.close();
Out.close();
return 0;

}

