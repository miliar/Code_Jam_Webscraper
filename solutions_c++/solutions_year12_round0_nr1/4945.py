#pragma comment(linker, "/STACK:256000000")

#include <set>
#include <map>
#include <list>
#include <stack>
#include <queue>
#include <ctime>
#include <math.h>
#include <vector>
#include <string>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string.h>
#include <algorithm>

using namespace std;


template<class T>
double sqrt(T x)
{
	return sqrt((double) x);
}

template<class T>
T sqr (T x)
{
	return x*x;
}


#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#define X first
#define Y second
#define pb push_back
#define mp make_pair
//#define foreach(e,x) for(__typeof(x.begin()) e=x.begin();e!=x.end();++e)



const double PI = acos(-1.0);
const int INF = 1000000000;
const int MOD = 1000000007;


//#define ONLINE_JUDGE

int main()
{
	double TIME_START = clock();
#ifndef ONLINE_JUDGE
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
#endif

	int T;
	string s;
	scanf(" %d ", &T);

	map<char,char> to;

	to[' ']=' ';
	to['a']='y';
	to['b']='h';
	to['c']='e';
	to['d']='s';
	to['e']='o';
	to['f']='c';
	to['g']='v';
	to['h']='x';
	to['i']='d';
	to['j']='u';
	to['k']='i';
	to['l']='g';
	to['m']='l';
	to['n']='b';
	to['o']='k';
	to['p']='r';
	to['r']='t';
	to['s']='n';
	to['t']='w';
	to['u']='j';
	to['v']='p';
	to['w']='f';
	to['x']='m';
	to['y']='a';
	to['z']='q';
	to['q']='z';


	for (int x = 1 ; x <= T ; x++)
	{
		getline(cin, s);
		for (int y = 0 ; y < s.size() ; y++)
			s[y] = to[s[y]];
		printf("Case #%d: %s\n", x,s.c_str ());
	}
	
	
	eprintf("\n\n%.15lf\n\n",(double)(clock() - TIME_START)/CLOCKS_PER_SEC);
	return 0;
}
