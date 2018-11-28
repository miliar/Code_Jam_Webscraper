#pragma comment(linker,  "/STACK:16777216")
#include <algorithm>
#include <cstring>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <iterator>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <fstream>
#include <locale>
#include <climits>

using namespace std;

typedef long long ll;
typedef unsigned long long Ull;

#define VI vector <int>
#define FOR(i, a, b) for(int (i) = (a); (i) < (b); ++(i))
#define RFOR(i, a, b) for(int (i) = (a)-1; (i) >= (b); --(i))
#define CLEAR(a) memset((a), , sizeof(a))
#define INF 1000000000
#define PB push_back
#define ALL(c) (c).begin(),  (c).end()
#define pi 2*acos(0.0)
#define SQR(a) (a)*(a)
#define MP make_pair
#define MOD 1000000007
#define EPS 1e-7
#define INF 2000000000

string ss = "abcdefghijklmnopqrstuvwxyz";
string S  = "yhesocvxduiglbkrztnwjpfmaq";
int main()
{
	freopen("input.txt","r",stdin);
	freopen("IntegerArray.txt","w",stdout);
	int t;
	cin >> t;
	string s;
	getline(cin,s);
	FOR(i,0,t)
	{
		getline(cin,s);
		FOR(j,0,s.length())
			if (s[j] != ' ')
			s[j] = S[s[j]-'a'];
		cout << "Case #" << i+1 << ": " << s << endl;
	}

	return 0;
}