#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
//#define DEBUG
#ifdef DEBUG
	#define DEB printf
	#define FF fflush(stdout)
#else
	#define DEB(...) 
	#define FF
#endif
#define REP(x, n) for(int x = 0; x < (n); x++)
#define FOR(x, b, e) for(int x = (b); x <= (e); x++)
#define FORD(x, u, d) for(int x = (u); x >= (d); x--)
#define VAR(x, a) __typeof(a) x = (a)
#define FOREACH(x, c) for(VAR(x, (c).begin()); x != (c).end(); x++)
#define ALL(c) (c).begin(), (c).end()
#define SIZE(x) ((int)(x).size())
#define INF 1000000
#define PB push_back
#define MP make_pair
#define ST first
#define ND second
using namespace std;
typedef vector<int> VI;
typedef pair<int, int> PII;
typedef long long LL;
typedef unsigned long long ULL;
typedef long double LD;

string encoded = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jvq",
	   decoded = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give upz",
	   input;

const int A = 'z' - 'a' + 1;
char decode[A];
bool used[A];
int n;

int main() {
	REP(i, A) decode[i] = '#';
	REP(i, SIZE(encoded)) if(encoded[i] != ' ') {
		int pos = encoded[i] - 'a'; 
		if(decode[pos] != '#' && decode[pos] != decoded[i]) {
			DEB("Failure %d: %c -> %c %c\n", i + 1, encoded[i], decoded[i], decode[pos]);
		}
		decode[pos] = decoded[i];
		used[decoded[i] - 'a'] = 1;
	}
	int it1 = 0, it2 = 0;
	while(decode[it1] != '#') it1++;
	while(used[it2]) it2++;
	decode[it1] = it2 + 'a';

	REP(i, A) DEB("%c -> %c\n", 'a' + i, decode[i]);
	getline(cin, input);
	n = atoi(input.c_str());
	REP(i, n) {
		cout << "Case #" << i + 1 << ": ";
		getline(cin, input);
		REP(j, SIZE(input)) if(input[j] == ' ') {
			cout << " ";
		} else {
			cout << decode[input[j] - 'a'];
		}
		cout << endl;
	}

	return 0;
}

	

