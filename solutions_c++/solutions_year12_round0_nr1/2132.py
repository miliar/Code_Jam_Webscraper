#include <iostream>
#include <vector>
#include <stdio.h>
#include <string>
#include <math.h>
#include <algorithm>
#include <set>
#include <math.h>
#include <time.h>
#include <stdio.h>
#define rep(i,k,n) for(int (i) = (k); (i) < (n); (i)++)
#define sqr(r) (r)*(r)
#define ii pair<int,int>
#define vii vector<ii>
#define vi vector<int>
using namespace std;


set<long long> si;
long long mod;
long long n,m,k,d,l,r, INF = 10000009;
string s = "ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv";
string g = "our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up";
char c[300] = {0}, t;


int main()
{
	freopen("in","r", stdin);
	freopen("out", "w", stdout);
	cin >> n;
	k = 1;
	t = getchar();
	t = getchar();
	rep(i,0,s.size())
		c[(int) s[i]] = g[i];
		c['e'] = 'o';
		c['y'] = 'a';
		c['q'] = 'z';
		c['z'] = 'q';
	cout << "Case #" << k << ": ";
	while(t > 0)
	{
		if(t == '\n' && k == n)
			break;
		if(t == '\n')
			cout << "\nCase #" << ++k << ": ";
		else
			cout << c[(int)t];
		t = getchar();	
	}
	
	return 0;
}
