#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <set>
#include <vector>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <cmath>
#include <string>

#define fr(x,y) for(int x=0; x<(y); ++x)
#define fe(x,y,z) for(int x=(y); x<(z); ++x)
#define fw(x,y,z) for(int x=(y); x<=(z); ++x)
#define df(x,y,z) for(int x=(y); x>=(z); --x)
#define mn(x,y) ((x)<(y) ? (x) : (y))
#define mx(x,y) ((x)>(y) ? (x) : (y))
#define ab(x) ((x)<0 ? (-(x)) : (x))
#define MP make_pair
#define PB push_back
#define BIG 1000000000
#define X first
#define Y second
#define dbg(x) if(DEBUG) {cout<<#x<<": "<<(x)<<endl;}
#define dout(x) if(DEBUG) {cout<<x;}
#define dline(x) if(DEBUG) {cout<<x<<endl;}
#define dbgr(x,l) if(DEBUG) {cout<<#x<<": ";fr(innercounter,l) cout<<x[innercounter]<<" ";cout<<endl;}
#define dbge(x,y,z) if(DEBUG) {cout<<#x<<": ";fe(innercounter,y,z) cout<<x[innercounter]<<" ";cout<<endl;}
#define dbgw(x,y,z) if(DEBUG) {cout<<#x<<": ";fw(innercounter,y,z) cout<<x[innercounter]<<" ";cout<<endl;}
#define dbgee(x,l1,l2) if(DEBUG) {cout<<#x<<": "<<endl;fr(icounter,l1){fr(jcounter,l2) cout<<x[icounter][jcounter]<<" ";cout<<endl;}}

bool DEBUG = false;

using namespace std;

int n;
char buf[1000];
string s,t;
char mas[500];

int main()
{
freopen("A-small-attempt1.in", "r",stdin);
freopen("output.txt", "w", stdout);
#ifdef HOME
DEBUG = true;
#endif
/*
getline(cin,s);
getline(cin,t);
fr(i,s.length())
	{
	if(s[i]!=' ')
		mas[s[i]] = t[i];
	}
for(char ch='a'; ch<='z'; ch++) 
	cout<<"mas[\""<<ch<<"\"] = '"<<mas[ch]<<"';"<<endl;*/
mas['a'] = 'y';
mas['b'] = 'h';
mas['c'] = 'e';
mas['d'] = 's';
mas['e'] = 'o';
mas['f'] = 'c';
mas['g'] = 'v';
mas['h'] = 'x';
mas['i'] = 'd';
mas['j'] = 'u';
mas['k'] = 'i';
mas['l'] = 'g';
mas['m'] = 'l';
mas['n'] = 'b';
mas['o'] = 'k';
mas['p'] = 'r';
mas['q'] = 'z';
mas['r'] = 't';
mas['s'] = 'n';
mas['t'] = 'w';
mas['u'] = 'j';
mas['v'] = 'p';
mas['w'] = 'f';
mas['x'] = 'm';
mas['y'] = 'a';
mas['z'] = 'q';
cin>>n;
getline(cin,s);
fr(i,n)
	{
	getline(cin,s);	
	fr(j,s.length())
		if(s[j]!=' ')
		s[j] = mas[s[j]];
	cout<<"Case #"<<(i+1)<<": "<<s;
	if(i!=n-1) cout<<endl;
	}
return 0;
}
