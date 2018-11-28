// cheburashka, bear-mouse, team template

#include <cstdlib>
#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <map>
#include <algorithm>
#include <cstdio>
#include <sstream>
#include <stack>
#include <cstring>
#include <cmath>
#include <queue>
#include <set>
using namespace std;

typedef long long ll;
typedef vector < string > vs;
typedef vector <int> vi;
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define deb(x) cout << #x << ": " << x << endl;
#define debv(x) for(int i = 0; i < (x).size(); i++) cout << x[i] << ' '; cout << endl;

#define pb(x) push_back(x)

#define mp(x, y) make_pair(x, y)

//string split given string a and delimiters

int gwin(int a, int b, int f)
{
	if(b-a >= a) return f;
	return gwin(b-a,a,1-f);
}

int main()
{
	int T;
	cin >> T;
	for(int tcase = 1; tcase <= T; tcase++)
	{
		long long a1,a2,b1,b2;
		cin >> a1 >> a2 >> b1 >> b2;
		long long ret = 0,temp;
		
		long double grat = (1.0+sqrt((long double)5.0))/2.0;
		for(int a = a1; a <= a2; a++)
		{
			double Q = grat*a + 1.0;
			long long F = (int)Q, S = (int)Q-1;
			F = max(F,b1);
			if(b2 >= F) ret += b2-F+1;
		}
		for(int b = b1; b <= b2; b++)
		{
			double Q = grat*b + 1.0;
			long long F = (int)Q, S = (int)Q-1;
			F = max(F,a1);
			if(a2 >= F) ret += a2-F+1;
		}
		
		printf("Case #%d: %lld\n",tcase,ret);
	}
	return 0;
}
