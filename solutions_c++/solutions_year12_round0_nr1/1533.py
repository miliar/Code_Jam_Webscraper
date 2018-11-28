#include <iostream> 
#include <vector>
#include <set>
#include <cstdio>
#include <cmath>
#include <string>
#include <algorithm>
#include <map>
#include <queue>
#include <memory.h>
#include <fstream>
using namespace std;

#define FOR(i,a,b) for(int (i)=(a);(i)<(b);(i)++)
#define MP make_pair
#define ALL(a) (a).begin(),(a).end()
#define PB push_back
#define PII pair<int,int>
#define CLEAR(a) memset((a),0,sizeof((a)))
#define X first
#define Y second

typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> VI;

const double pi=3.141592653589793;
const int INF=2000000000;
const int mod=1000000007;
map <char,char> a;
int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	a['a']='y';
	a['b']='h';
	a['c']='e';
	a['d']='s';
	a['e']='o';
	a['f']='c';
	a['g']='v';
	a['h']='x';
	a['i']='d';
	a['j']='u';
	a['k']='i';
	a['l']='g';
	a['m']='l';
	a['n']='b';
	a['o']='k';
	a['p']='r';
	a['q']='z';
	a['r']='t';
	a['s']='n';
	a['t']='w';
	a['u']='j';
	a['v']='p';
	a['w']='f';
	a['x']='m';
	a['y']='a';
	a['z']='q';
	int n;
	cin >> n;
	string s;
	getline(cin,s);
	FOR(t,0,n){
		getline(cin,s);
		cout << "Case #" << t+1 << ": ";
		FOR(i,0,s.size())
			if (s[i]!=' ')
				cout << a[s[i]];
			else cout << s[i];
		cout << endl;
	}

	return 0;
}