//darkstallion's template

#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<vector>
#include<map>
#include<stack>
#include<queue>
#include<algorithm>
#include<cmath>
#include<string>
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define popb pop_back
#define del erase
#define sz size
#define ins insert
#define FOR(a,b,c) for(int a = b; a < c; a++)
#define FORS(a,b,c) for(int a = b; a <= c; a++)
#define FORN(a,b) for(int a = 0; a < b; a++)
#define FORD(a,b,c) for (int a = b; a >= c; a--)
#define RES(a,b) memset(a,b,sizeof(a))
#define LL long long
#define PII pair<int,int>
#define PLL pair<long long,long long>
#define PDD pair<double,double>
#define PCC pair<char,char>
#define PSS pair<string,string>
using namespace std;

int t;
string st;

int main()
{
	map<char,char> data;
	data['a'] = 'y';
	data['b'] = 'h';
	data['c'] = 'e';
	data['d'] = 's';
	data['e'] = 'o';
	data['f'] = 'c';
	data['g'] = 'v';
	data['h'] = 'x';
	data['i'] = 'd';
	data['j'] = 'u';
	data['k'] = 'i';
	data['l'] = 'g';
	data['m'] = 'l';
	data['n'] = 'b';
	data['o'] = 'k';
	data['p'] = 'r';
	data['q'] = 'z';
	data['r'] = 't';
	data['s'] = 'n';
	data['t'] = 'w';
	data['u'] = 'j';
	data['v'] = 'p';
	data['w'] = 'f';
	data['x'] = 'm';
	data['y'] = 'a';
	data['z'] = 'q';
	scanf("%d",&t);
	getchar();
	FORN(i,t)
	{
		getline(cin,st);
		printf("Case #%d: ",i+1);
		FORN(i,st.sz())
			if (st[i] != ' ')
				printf("%c",data[st[i]]);
			else
				printf(" ");
		printf("\n");
	}
}
