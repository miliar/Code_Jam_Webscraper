#pragma comment(linker, "/STACK:134217728")
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <string>
#include <stack>
#include <cmath>
#include <list>
#include <iomanip>
#include <set>
#include <map>
using namespace std;
#define RFor(i,a,b) for(int (i)=(a);(i)>=(b);--(i)) 
#define For(i,a,b) for(int (i)=(a);i<=(b);++(i))
#define FOR(i,a,b) for(int (i)=(a);i<(b);++(i))
#define RFOR(i,a,b) for(int (i)=(a)-1;(i)>=(b);--(i)) 
#define ll long long
#define ull unsigned long long
#define UI unsigned int
#define LD long double
#define pii pair<int,int>
#define mp make_pair
#define MOD 1000000007
//#define x first
//#define y second
string s[5];
int res()
{
	int o,x;	
	FOR(i,0,4)
	{
		o=x=0;
		FOR(j,0,4)
		{
			if(s[i][j]=='X'||s[i][j]=='T')x++;
			if(s[i][j]=='O'||s[i][j]=='T')o++;
		}
		if(o==4)return 1;
		if(x==4)return -1;
	}
	FOR(j,0,4)
	{
		o=x=0;
		FOR(i,0,4)
		{
			if(s[i][j]=='X'||s[i][j]=='T')x++;
			if(s[i][j]=='O'||s[i][j]=='T')o++;
		}
		if(o==4)return 1;
		if(x==4)return -1;
	}
	o=x=0;
	FOR(i,0,4)
	{
		if(s[i][i]=='X'||s[i][i]=='T')x++;
		if(s[i][i]=='O'||s[i][i]=='T')o++;
	}
	if(o==4)return 1;
	if(x==4)return -1;
	o=x=0;
	FOR(i,0,4)
	{
		if(s[3-i][i]=='X'||s[3-i][i]=='T')x++;
		if(s[3-i][i]=='O'||s[3-i][i]=='T')o++;
	}
	if(o==4)return 1;
	if(x==4)return -1;
	FOR(i,0,4)
		FOR(j,0,4)
		if(s[i][j]=='.')return 0;
	return 2;
}
int main()
{
	freopen("A-large.in","rt",stdin);
	freopen("output.txt","wt",stdout);
	int t;
	scanf("%d",&t);
	FOR(i,0,t)
	{
		getline(cin,s[0]);
		FOR(j,0,4)
			getline(cin,s[j]);
		string w;
		int a=res();
		if(a==-1)w="X won\n";
		if(a==0)w="Game has not completed\n";
		if(a==1)w="O won\n";
		if(a==2)w="Draw\n";

		cout<<"Case #"<<i+1<<": "<<w;
	}
	return 0;
}