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

struct node
{

	int val[2];
	int gate;
	int cc;
	node(int v=0, int g=0, int c = 0)
	{
		val[0] = val[1] = 10000000;
		if(v) val[1] = 0;
		else val[0] = 0;
		gate = g;
		cc = c;
	}
};

int min(int a, int b)
{
	return a < b ? a : b;
}
 
int main()
{

int G;
fstream In("a-large.in", ios::in);
fstream Out("a-large.out", ios::out);

In >> G;

for(int h=1; h<=G; h++)
{


Out << "Case #" << h << ": ";

int M, V;

In >> M >> V;

vector<node> v(M+1);

int i, j;

for(i=0; i<M/2; i++)
{
	int a, b;
	In >> a >> b;
	v[i+1] = node(0, 1-a, b);

}
for(; i<M; i++)
{
	int a;
	In >> a;
	v[i+1] = node(a);
}


for(i=M/2; i ; i--)
{
	int lc = i*2;
	int rc = i*2+1;
	if(v[i].cc == 0)
	{	// to get 0
		v[i].val[0] = min(v[lc].val[0]+v[rc].val[0],
			min(v[lc].val[1] + v[rc].val[0] + (v[i].gate==0 ? 0 : 10000000),
			    v[lc].val[0] + v[rc].val[1] + (v[i].gate==0 ? 0 : 10000000)
				 ) );
		v[i].val[1] = min(v[lc].val[1]+v[rc].val[1],
			min(v[lc].val[1] + v[rc].val[0] + (v[i].gate==1 ? 0 : 10000000),
			    v[lc].val[0] + v[rc].val[1] + (v[i].gate==1 ? 0 : 10000000)
				 ) );
	}
	else
	{	// to get 0
		v[i].val[0] = min(v[lc].val[0]+v[rc].val[0],
			min(v[lc].val[1] + v[rc].val[0] + (v[i].gate==0 ? 0 : 1),
			    v[lc].val[0] + v[rc].val[1] + (v[i].gate==0 ? 0 : 1)
				 ) );
		v[i].val[1] = min(v[lc].val[1]+v[rc].val[1],
			min(v[lc].val[1] + v[rc].val[0] + (v[i].gate==1 ? 0 : 1),
			    v[lc].val[0] + v[rc].val[1] + (v[i].gate==1 ? 0 : 1)
				 ) );
	}

	
}


if(v[1].val[V] > M+1)
	Out << "IMPOSSIBLE" << endl;
else Out << v[1].val[V] << endl;

cout << endl;
}
In.close();
Out.close();
return 0;

}

