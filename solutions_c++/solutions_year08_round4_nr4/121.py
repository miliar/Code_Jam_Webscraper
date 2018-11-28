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

int min(int a, int b)
{
	return a < b ? a : b;
}


int score(string s)
{

	int ret = 1;
	for(int i=1; i<s.size(); i++)
		if(s[i]!=s[i-1]) ret++;
	return ret;
}


int tab1[25][25];
int tab2[25][25];
int table[70000][25];
int seen[70000][25];

int start;
int K;

int doit(int mask, int cur)
{
	if(mask==(1<<K)-1 )
		return table[mask][cur] = tab2[cur][start];

	if(seen[mask][cur]) return table[mask][cur];
	seen[mask][cur] = 1;

	table[mask][cur] = 10000000;

	for(int i=0; i<K; i++)
	{
		if((1<<i)& mask) continue;
		//if(mask==1) cout << i << ' ' << table[mask][cur] << ' ' ;

		table[mask][cur] = min(table[mask][cur], tab1[cur][i] + doit(mask | (1<<i), i) );
		//if(mask==1) cout << table[mask][cur] << endl;
	}

	return table[mask][cur];
}



int main()
{

int G;
fstream In("d-large.in", ios::in);
fstream Out("d-large.out", ios::out);

In >> G;

for(int h=1; h<=G; h++)
{


Out << "Case #" << h << ": ";

string S;
In >> K;
In >> S;

memset(tab1, 0, sizeof(tab1));
memset(tab2, 0, sizeof(tab2));

int i, j, k;

for(i=0; i<K; i++)
for(j=0; j<K; j++)
{
	if(i==j) continue;
	for(k=0; k<S.size(); k+=K)
	{
		if(S[k+i]!=S[k+j])
			tab1[i][j]++;
		if(k)	// tab2 = precompute if segment 1 ends in i and seg 2 starts with j
			if(S[k-K+i]!=S[k+j] ) tab2[i][j]++;
	}
}



memset(table, -1, sizeof(table));

int ret = 1000000;

for(i=0; i<K; i++)
{
	memset(table, -1, sizeof(table));
	memset(seen, 0, sizeof(seen));

	start = i;
	ret = min(ret, doit(1<<i, i) );
//	cout << i << ' ' << doit(1<<i, i) << endl;
/*	if(!i)
	{
		for(j=0; j<16; j++)
		{	cout << j << ' ';
			for(k=0; k<4; k++)
				cout << table[j][k] << ' ';
			cout << endl;
		}
	}
*/
}
/*
for(i=0; i<K; i++)
{
	for(j=0; j<K; j++)
		cout << tab1[i][j] << ' ';
	cout << endl;
}

*/
Out << ret+1 << endl;


}


In.close();
Out.close();
return 0;

}

