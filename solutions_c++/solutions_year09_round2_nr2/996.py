#include <algorithm>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>
 
using namespace std;
 
typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef pair<int, int> ii;
#define FOR(i,a,b) for(typeof(a) i=(a); i < (b); i++)
#define sz(a) int((a).size()) 
#define all(c) (c).begin(), (c).end() 
#define tr(c, i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++) 
#define present(c, x) ((c).find(x) != (c).end()) 
#define cpresent(c, x) (find(all(c), x) != (c).end())
template<class T> T sqr(T x){return x*x;}
int toint(string s){istringstream sin(s); int x; sin>>x; return x;}
string tostring(int x){ostringstream sout; sout<<x; return sout.str();}

void process(int n)
{
	bool flag = true;
	string s1, s2, s;
	cin >> s1;

	s2 = s1;

	next_permutation(s2.begin(), s2.end());

	FOR(i, 1, s1.length())
		flag &= (s1[i] == '0');
		
	if(flag) 
		s = s1 + '0';
	else if(s2[0] == '0') {
		string buf;
		FOR(i, 0, s2.length()) {
			if(s2[i] == '0')
				s += '0';
			else
				buf += s2[i];
		}
		s = buf[0] + (string)"0" + s;
		FOR(i, 1, buf.length())
			s += buf[i];
	}
	else if(s2 <= s1) {
		s = s2[0];
		s += '0';
		FOR(i, 1, s2.length())
			s += s2[i];
	}
	else
		s = s2;

	cout << "Case #" << n << ": " << s << endl;
}

int main()
{
	int n;

	scanf("%d", &n);

	FOR(i, 1, n + 1)
		process(i);
	
	return 0;
} 

