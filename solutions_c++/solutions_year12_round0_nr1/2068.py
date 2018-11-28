#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstring>
#include <deque>
#include <iomanip>
#include <limits>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <sstream>
#include <utility>
#include <vector>

using namespace std;

#define rep(i, b, n) for(int i=(b); i<(n); ++i)
#define repd(i, b, n) for(int i=(b); i>(n); --i)
#define trav(it, col) for(typeof((col).begin()) it = (col).begin(); it != (col).end(); ++it)
#define clr(pt) memset((pt), 0, sizeof(pt))
#define EPS 1e-8
#define IFD if(DEBUG)
#define dbg(x) DEBUG && cerr << __LINE__ << ": " << x << endl
#define DL cerr << __LINE__ << endl;
#define mp make_pair

#define DEBUG true

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef pair<int, double> pid;
typedef pair<double, double> pdd;
typedef stringstream ss;

int INMODE = 0; // 0 specify cases, 1 single run, 2 indefinite runs
char tl[26];

void calc()
{
    string crypt("ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv");
	string orig("our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up");
	
	for(int i=0; i<26; i++)
	{
		tl[i] = ' ';
		for(int j=0; j<crypt.size(); j++)
		{
			if(crypt[j] == ('a' + i)) tl[i] = orig[j];
		}
		
	}
	tl['z' - 'a'] = 'q';
	tl['q' - 'a'] = 'z';
	
	//for(int i=0; i<26; i++) cout << (char('a'+i)) << " " << tl[i] << endl;
}

bool solve(int cn){
    string sol = "";
	char buf[200];
	cin.getline(buf, 200);
	string in(buf);
	rep(i, 0, in.size())
	{
		if(in[i] == ' ') sol += ' ';
		else sol += tl[in[i] - 'a'];
	}

    cout << "Case #" << cn << ": " << sol << endl;
    return 1;
}

int main(){
    //cout << setiosflags(ios::fixed) << setprecision(10);
    int cases = 1 << 30;
    if(INMODE == 0) cin >> cases;
    if(INMODE == 1) cases = 1;
    calc();
	char buf[200];
	cin.getline(buf, 200);
    for(int cn = 1; cn <= cases; ++cn)
        if(!solve(cn) && INMODE == 2) break;
    return 0;
}
