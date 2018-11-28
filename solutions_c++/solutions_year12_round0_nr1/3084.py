#include <iostream> 
#include <algorithm> 
#include <vector> 
#include <cstdio> 
#include <string> 
#include <bitset> 
#include <cmath> 
#include <list> 
#include <cstdlib> 
#include <map> 
#include <cstring> 
#include <set> 
#include <stack> 
#include <sstream> 
#include <queue> 
#include <deque> 
#include <ctime> 

using namespace std; 

#define debug(x) cout<<#x<<" = "<<x<<"\n" 
#define REP(i,n) for(int (i)=0;(i)<(n);(i)++) 
#define PI 3.1415926535897932385 
#define INF (1<<29) 
#define EPS (1e-7) 
#define pb push_back 
#define sz size() 
#define ln length() 
#define mp make_pair 
#define all(a) a.begin(),a.end() 
#define fill(ar,val) memset(ar,val,sizeof ar) 
#define sqr(x) ((x)*(x)) 
#define min(a,b) ((a)<(b)?(a):(b)) 
#define max(a,b) ((a)>(b)?(a):(b)) 
#define FORE(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++) 

typedef long long LL; 
typedef long double LD; 
typedef vector<int> VI; 

int main()
{
	map < char, char > mp;
	mp['a'] = 'y';
	mp['b'] = 'h';
	mp['c'] = 'e';
	mp['d'] = 's';
	mp['e'] = 'o';
	mp['f'] = 'c';
	mp['g'] = 'v';
	mp['h'] = 'x';
	mp['i'] = 'd';
	mp['j'] = 'u';
	mp['k'] = 'i';
	mp['l'] = 'g';
	mp['m'] = 'l';
	mp['n'] = 'b';
	mp['o'] = 'k';
	mp['p'] = 'r';
	mp['q'] = 'z';
	mp['r'] = 't';
	mp['s'] = 'n';
	mp['t'] = 'w';
	mp['u'] = 'j';
	mp['v'] = 'p';
	mp['w'] = 'f';
	mp['x'] = 'm';
	mp['y'] = 'a';
	mp['z'] = 'q';
	mp[' '] = ' ';
	int t;
	string s;
	cin >> t;
	cin.ignore();
	for ( int j = 1; j <= t; j++ ) {
		getline(cin,s);
		cout << "Case #"<<j<<": ";
		int n = s.sz;
		REP(i,n) {
			cout << mp[s[i]];
		}
		
		cout << endl;
	}
	
	return 0;
}
