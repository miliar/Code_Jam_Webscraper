#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <stack>
#include <queue>
#include <vector>
#include <cstdio>
#include <string>
#include <bitset>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <utility>
#include <sstream>
#include <iostream>
#include <algorithm>
#define sqr(x) ((x)*(x))
#define ABS(x) ((x<0)?(-(x)):(x))
#define eps (1e-9)
#define mp make_pair
#define pb push_back
#define Pair pair<int,int>
#define equal(a,b) (ABS(a-b)<eps)
using namespace std;

template<class T> string tostring(T x) { ostringstream out; out<<x; return out.str();}
long long toint(string s) { istringstream in(s); long long x; in>>x; return x; }

int dx[8]={0, 0, 1,-1, 1, 1,-1,-1};
int dy[8]={1,-1, 0, 0,-1, 1,-1, 1};
int kx[8]={1, 1,-1,-1, 2, 2,-2,-2};
int ky[8]={2,-2, 2,-2, 1,-1, 1,-1};

/////////////////////////////////////////////////////////////////////////////////////////////////////

string fileName = "A-small-attempt0";

string first  = "ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjvzq";
string second = "ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveupqz";
void solveSingle(int testNumber) {
	int enc[26];
	char buf[200];
	gets(buf);
	string s(buf);
	for (int i = 0; i < first.size(); i++)
		enc[first[i] - 'a'] = second[i] - 'a';
	for (int i = 0; i < s.size(); i++)
		if (s[i] != ' ') s[i] = 'a' + enc[s[i] - 'a'];
	printf("Case #%d: %s\n", testNumber, s.c_str());
}

int main() {
	freopen((fileName + ".in").c_str(), "r", stdin);
	freopen((fileName + ".out").c_str(), "w", stdout);
	int T;
	scanf("%d\n", &T);
	for (int t = 1; t <= T; t++) {
		solveSingle(t);
	}
	return 0;
}
