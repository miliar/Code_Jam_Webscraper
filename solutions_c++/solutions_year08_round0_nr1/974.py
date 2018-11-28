#include <algorithm>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <set>
using namespace std;

#define FOR(i,a,b)	for(int i=(a),_b=(b);i<=_b;i++)
#define REP(i,n)	FOR(i,0,(n)-1)
#define FORD(i,a,b)	for(int i=(a),_b=(b);i>=_b;i--)

#define SZ(v)		((int)(v).size())
#define PB			push_back
#define MP			make_pair

typedef set<string>		SS;

typedef vector<string>	VS;
typedef vector<int>		VI;
typedef vector<VI>		VVI;


vector<string> Tokenize(string s, string ch) {
	vector<string> ret;
	for (int p = 0, p2; p < SZ(s); p = p2+1) {
		p2 = s.find_first_of(ch, p);
		if (p2 == -1) p2 = SZ(s);
		if (p2-p > 0) ret.push_back(s.substr(p, p2-p));
	}
	return ret;
}

vector<int> TokenizeInt(string s, string ch) {
	vector<int> ret;
	vector<string> p = Tokenize(s, ch);
	for( int i = 0; i < SZ(p); i++ )
		ret.push_back(atoi(p[i].c_str()));
	return ret;
}


ifstream fin("A-large.in");
#define cin fin
ofstream fout("A-large.out");
#define cout fout

VS gse;
VS gq;
int gnse;
int gnq;

int CalSwitch()
{
	SS ese;
	int nSwitch = 0;

	REP(iq, gnq) {
		ese.insert(gq[iq]);
		if (ese.size() == gnse) {
			++nSwitch;
			ese.clear();
			ese.insert(gq[iq]);
		}
	}

	return nSwitch;
}

void main()
{
	int N;
	string tmps;
	cin >> N;

	FOR(nCase, 1, N) {
		gse.clear();
		gq.clear();

		cin >> gnse;
		getline(cin, tmps);
		REP(i, gnse) {
			getline(cin, tmps);
			gse.push_back(tmps);
		}
		cin >> gnq;
		getline(cin, tmps);
		REP(i, gnq) {
			getline(cin, tmps);
			gq.push_back(tmps);
		}

		cout << "Case #"<< nCase << ": " << CalSwitch() << endl;
	}
}

