#include <iostream>
#include <cstdio>
#include <cstring>
#include <cassert>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <cmath>
#include <bitset>
#include <sstream>

using namespace std;

#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define forsn(i,s,n) for(int i=(int)(s);i<(int)(n);i++)
#define forall(i,c) for(typeof((c).begin()) i=(c).begin();i!=(c).end();i++)
#define dforn(i,n) for(int i=((int)(n)-1);i>=0;i--)
#define dforsn(i,s,n) for(int i=((int)(n)-1);i>=(int)(n);i--)
#define esta(i,c) ((c).find(i) != (c).end())
#define dbg(x) cerr << #x << " = " << x << endl;
#define raya cerr << string('=',80) << endl;
typedef long long tint;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector< pair<int,int> > vii;

string start[]  = {
	"ejp mysljylc kd kxveddknmc re jsicpdrysi",
	"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
	"de kr kd eoya kw aej tysr re ujdr lkgc jv"
};

string end[] = { 
	 "our language is impossible to understand",
	 "there are twenty six factorial possibilities",
	 "so it is okay if you want to just give up"
};

map<char,char> alphabet;
string s;
int main(){
	#ifdef JUAMPI
		freopen("SpeakingInTongues.in","r",stdin);
		freopen("SpeakingInTongues.out","w",stdout);
	#endif

	forn(i,3){
		forn(j,start[i].size()){
			alphabet[start[i][j]] = end[i][j];
		}
	}
	alphabet['z'] = 'q';
	alphabet['q'] = 'z';
	
	getline(cin, s);
	istringstream ss(s);
	
	int t; ss >> t;
	forn(tt,t){
		getline(cin, s);
		string x = s;
		
		forn(i,s.size()){
			x[i] = alphabet[s[i]];
		}
		
		cout << "Case #" << 1+tt << ": " << x << endl;
	}
	return 0;
}
