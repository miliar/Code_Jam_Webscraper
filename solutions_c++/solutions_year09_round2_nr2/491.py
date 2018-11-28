#include <algorithm>  
#include <iostream>  
#include <cstdio>  
#include <sstream>  
#include <ctype.h>  
#include <cstring>  
#include <string>  
#include <cmath>  
#include <queue>  
#include <vector>  
#include <map>  
#include <set>  

using namespace std;  
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef pair<int, int> ii;
typedef istringstream iss;
typedef ostringstream oss;   

const int inf = 1<<30;

#define pb push_back
#define mp make_pair
#define all(a) (a).begin(),(a).end()   
#define forr(it,b,lim) for (it = (b); it < (lim); ++it)
#define forn(it,b,lim) for (it = (b); it >= (lim); --it)
#define rep(it,lim) for (it = 0; it < (lim); ++it)
#define mset(array,value) memset(array, value, sizeof(array))

char in[] = "B-large.in";
char out[] = "B-large.out";

int main()
{
	int i, j;
	freopen(in, "rt", stdin); freopen(out, "wt", stdout);

	int T, test;
	scanf("%d", &T);

	rep(test, T)
	{
		int res = 0;

		char s[25];
		scanf("%s", s);

		int L = strlen(s);
		if (next_permutation(s, s + L) == false)
		{
			s[L] = '0';
			s[L+1] = 0;
			L++;

			sort(s, s + L);
			i = 0;
			while (s[i] == '0')
				++i;
			swap(s[i], s[0]);
		}

		printf ("Case #%d: %s\n", test + 1, s);
	}

	return 0;
}