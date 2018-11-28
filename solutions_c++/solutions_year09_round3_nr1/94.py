#include<cstdio>
#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<map>
#include<cctype>
#include<cstdlib>
#include<queue>
#include<sstream>
#include<cmath>

using namespace std;

#define fo(a,b) for(a=0;a<b;a++)
#define re return
#define co continue
#define sf scanf
#define pf printf

int inf = 1000000000;

int convert(char ch) {
	if( isdigit(ch) ) re ch - '0';
	re ch - 'a' + 10;
}

int main() {
	int t, cases = 1;
	int i, k;
	for( sf("%d", &t); t--; ) {
		string s;
		cin >> s;
		int flag[100] = {0};
		for(i=0;i<s.size();i++)
		{
		  if( isdigit(s[i]) )
		    flag[ s[i] - '0'] = 1;
		  else
		    flag[ s[i] - 'a' + 10 ] = 1;
		}

		int base = 0;
		for(i=0;i<36;i++)
		  base += flag[i];

		if( base == 1 ) base++;

		for(i=0;i<=40;i++) flag[i] = -1;

		int inc = 0;

		for(i=0;i<s.size();i++) {
		  if( i == 0 ) {
		    k = convert(s[i]);
		    flag[k] = 1;
		  }
		  else{
		    k = convert(s[i]);
		    if( flag[k] == -1 )
		      flag[k] = inc++;
		      if( inc == 1 ) inc = 2;
		  }
		}

		long long res = 0;
		for(i=0;i<s.size();i++) {
		  k = convert(s[i]);
		  res = res * base + flag[k];
		}

		pf("Case #%d: %lld\n", cases++, res);
	}
	return 0;
}
