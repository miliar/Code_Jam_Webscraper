#include <iostream>
#include <cstdio>
#include <cstring>
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
#define raya cerr << string(80,'=') << endl;

typedef long long tint;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector< pair<int,int> > vii;

int compare(const string & s, const string & t){
	int diff = -1;
	forn(i,s.size()){
		if(s[i] != t[i]){
			diff = i;
			break;
		}
	}
	if(diff == -1) return 0;
	return s[diff]-t[diff];
}

void shift(string & s){
	char t = *(s.rbegin());
	
	char pre = s[0];
	forsn(i,1,s.size()){
		char temp = s[i];
		s[i] = pre;
		pre = temp;
		
	}
	s[0] = t;
}

int rep(const string & s){
	int r = 0;
	forn(i,s.size())
		r = 10*r + (s[i]-'0');
	return r;
}

set< pii > pos;
int main(){
	#ifdef JUAMPI
		freopen("RecycledNumbers.in","r",stdin);
		freopen("RecycledNumbers.out","w",stdout);
	#endif

	int tests; cin >> tests;
	forn(test,tests){
		int A, B; cin >> A >> B;
		string sA, sB;
	
		ostringstream temp;

		temp << A; sA = temp.str();
		temp.str("");
		temp << B; sB = temp.str();

		ostringstream oss;
		pos.clear();

		for(int i = A; i <= B; i++){
			ostringstream oss; 
				
			oss << i; oss.flush();
			string s = oss.str(),t = s;
			
			forn(j,s.size()-1){
				shift(s);
				if(s[0] == '0') continue;
			
				if(compare(sA, s) <= 0 && compare(sB,s) > 0 && compare(t,s) > 0){
					pos.insert(make_pair(rep(s),rep(t)));
				}
			}
		}
				
		cout << "Case #" << test+1 << ": " << pos.size() << endl;
	}
	return 0;
}
