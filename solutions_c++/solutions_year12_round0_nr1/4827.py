// A.cpp: определяет точку входа для консольного приложения.
//

#include "stdafx.h"
#include <iostream>
#include <ctime>
#include <cstdio>
#include <memory>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <list>
#include <stack>
#include <string>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <utility>
#include <iterator>
#include <bitset>
#include <sstream>
#include <numeric>

#define pb push_back
#define mp make_pair
#define pii pair<int,int>
#define pdd pair<double,double>
#define LL long long
#define ULL unsigned LL
#define VI vector<int>
#define X first
#define Y second
#define sz(_v) ((int)_v.size())
#define all(_v) (_v).begin(),(_v).end()
#define FOR(i,a,b) for (int i(a); i<=(b); ++i)
#define rep(i,a) FOR(i,1,a)
#define rept(i,a) FOR(i,0,(int)(a)-1)
#define x1 X1
#define y1 Y1
#define sqr(a) ((a)*(a))
#define INF 2000000000
#define PI 3.141592653589
#define eps 0.00000001
#define MOD 1000000007
#define PRIME 1000003

using namespace std;
map<char,char> m;
int main()
{
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	
		
	int n;
	char s[200],g[200];
	cin>>n;
	gets(s);
	//y n f i c w l b k u o m x s e v z p d r j g a t h a q
	//a b c d e f g h i j k l m n o p q r s t u v y w x y z
	m['a']='y';//abcdefgh
	m['b']='h';
	m['c']='e';
	m['d']='s';
	m['e']='o';
	m['f']='c';
	m['g']='v';
	m['h']='x';
	m['i']='d';
	m['j']='u';
	m['k']='i';
	m['l']='g';
	m['m']='l';
	m['n']='b';
	m['o']='k';
	m['p']='r';
	m['q']='z';
	m['r']='t';
	m['s']='n';
	m['t']='w';
	m['u']='j';
	m['v']='p';
	m['w']='f';
	m['x']='m';
	m['y']='a';
	m['z']='q';
	m[' ']=' ';
	rep(test,n)
	{
		gets(s);
		printf("Case #%d: ",test);
		rept(j,strlen(s))
			g[j]=m[s[j]];
		g[strlen(s)]='\0';
		puts(g);
	}
	return 0;
}

