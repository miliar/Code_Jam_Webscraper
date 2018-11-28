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
template<class Item>
Item max(Item a, Item b)
{
	return a > b ? a : b;
}


int table[1024][20];
int M, N;

int room[10];

int bc(int n)
{
	return n ? (1+bc(n&(n-1))): 0;
}

int dp(int mask, int cur)
{	
	if(cur==M) return 0;
	if(table[mask][cur] > -1) return table[mask][cur];

	table[mask][cur] = 0;

	for(int i=(1<<N)-1; i>-1; i--)
	{
		if(i & room[cur]) continue;
		if(i & mask) continue;
		int g;
		for(g=1; g+1<N; g++)
		{	if((i & (1<<g) ) == 0) continue;
			if(i & (1<<(g-1))) break;
			if(i & (1<<(g+1))) break;
		}
		if(g+1 < N) continue;
		int nmask = 0;
		for(int j=0; j<N; j++)
			if(i&(1<<j) )
			{	nmask |= (j ? (1<<(j-1)) : 0);
				nmask |= (j+1==N ? 0 : (1<<(j+1)) );
			}
		table[mask][cur] = max(table[mask][cur], bc(i) + dp(nmask, cur+1) );
	}

	return table[mask][cur];
}


 
int main()
{

int G;
fstream In("c-small.in", ios::in);
fstream Out("c-small.out", ios::out);

In >> G;

for(int h=1; h<=G; h++)
{
Out << "Case #" << h << ": ";

In >> M >> N;
cout << h << endl;
memset(room, 0, sizeof(room));
memset(table, -1, sizeof(table));

for(int i=0; i<M; i++)
{
	string s;
	In >> s;
	for(int j=0; j<N; j++)
		if(s[j]=='x') room[i] |= (1<<j);
}

Out << dp(0, 0) << endl;

}


In.close();
Out.close();
return 0;

}

