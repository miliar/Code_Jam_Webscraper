#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cassert>
#include <algorithm>
#include <numeric>
#include <string>
#include <sstream>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <iterator>
#include <cmath>
using namespace std;

#define REP(i,n) for(int i = 0; i < n; i++)
#define FOR(i,s,e) for(int i = s; i < e; i++)
#define FORD(i,e,s) for(int i = e; i > s; i--)
#define ALL(x) x.begin(), x.end()
#define OUT(x) cout<<#x<<" = "<<x<<endl;
#define PB push_back
typedef long long ll;

char sentence [] = "welcome to code jam";
int length;

char s[501];
int T[500][19];
#define MOD 10000

int main()
{
	ios_base::sync_with_stdio(0);
	int N;
	cin>>N;
	cin.getline(s, 501);
	length = strlen(sentence);

	REP(tests, N)
	{
		cin.getline(s, 501);
		int howmuch = strlen(s);
		memset(T, 0, sizeof(T));
		T[0][0] = (s[0] == sentence[0] ? 1 : 0);
		FOR(i, 1, howmuch)
			T[i][0] = T[i-1][0]+(s[i] == sentence[0] ? 1 : 0);

		FOR(i, 1, howmuch)
			FOR(j, 1, length)
		{
			T[i][j] = T[i-1][j];
			if(s[i] == sentence[j])
				T[i][j] = (T[i-1][j-1] + T[i][j])%MOD;
		}

		printf("Case #%d: %0.4d\n", tests+1, T[howmuch-1][length-1]);
	}

	return 0;
}

