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

int getbits(int n)
{
	return n ? (1+getbits(n&(n-1))) : 0;
}
 
int main()
{

int G;
fstream In("b-small.in", ios::in);
fstream Out("b-small.out", ios::out);

In >> G;

for(int h=1; h<=G; h++)
{
// designed for easy
int N, M;

In >> N >> M;

vector<int> liken(M, 0), likem(M, 0);
int i, j;
for(i=0; i<M; i++)
{
	int T;
	In >> T;
	for(j=0; j<T; j++)
	{
		int x, y;
		In >> x >> y;
		if(y)
			likem[i] |= (1<<(x-1));
		else liken[i] |= (1<<(x-1));
	}

}

int best = 1000000;
int bi = -1;

for(i=0; i<(1<<N); i++)
{
	for(j=0; j < M; j++)
	{
		if(!(likem[j] & i) && !(liken[j] & ~i) ) break;
	}
	if(j < M) continue;

	int t = getbits(i);
	if(t < best)
	{
		bi = i; best = t;
	}

}

Out << "Case #" << h << ": ";

if(bi > -1)
{
for(i=0; i<N; i++)
Out << (((1<<i) & bi) ? 1 : 0) << ' ';
Out << endl;
}
else Out << "IMPOSSIBLE" << endl;



}


In.close();
Out.close();
return 0;

}

