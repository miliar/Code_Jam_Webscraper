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
typedef multiset<int>	SI;

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


ifstream fin("B-large.in");
#define cin fin
ofstream fout("B-large.out");
#define cout fout

int gnas;
SI gttas;
SI gttae;

int gnbs;
SI gttbs;
SI gttbe;

int CalNumTrain(SI& tte, SI& tts)
{
	int nNumTrains = SZ(tts);
	SI::iterator itts = tts.begin();
	SI::iterator ietts = tts.end();

	SI::iterator itte = tte.begin();
	SI::iterator iette = tte.end();

	for(; itts != ietts && itte != iette; ++itts) {
		if (*itts >= *itte) {
			--nNumTrains;

			//cout << *itte / 60 << ":" << *itte % 60 << " -> " << *itts / 60 << ":" << *itts % 60 << endl;
			++itte;
		}
 		//else
 			//cout << *itts / 60 << ":" << *itts % 60 << endl;
	}

 	//if (itte != iette)
 		//cout << "last train : " << *itte / 60 << ":" << *itte % 60 << endl;

	return nNumTrains;
}

void main()
{
	int N;
	string tmps;
	cin >> N;
	int gtat;
	int atob, btoa;

	FOR(nCase, 1, N) {
		int h, m;

		gttas.clear();
		gttae.clear();
		gttbs.clear();
		gttbe.clear();

		cin >> gtat >> gnas >> gnbs;
		getline(cin, tmps);

		REP(i, gnas) {
			getline(cin, tmps);

			h = atoi(tmps.substr(0, 2).c_str());
			m = atoi(tmps.substr(3, 2).c_str());

			gttas.insert(h * 60 + m);

			h = atoi(tmps.substr(6, 2).c_str());
			m = atoi(tmps.substr(9, 2).c_str());

			gttae.insert(h * 60 + m + gtat);
		}

		REP(i, gnbs) {
			getline(cin, tmps);

			h = atoi(tmps.substr(0, 2).c_str());
			m = atoi(tmps.substr(3, 2).c_str());

			gttbs.insert(h * 60 + m);

			h = atoi(tmps.substr(6, 2).c_str());
			m = atoi(tmps.substr(9, 2).c_str());

			gttbe.insert(h * 60 + m + gtat);
		}

		//cout << "a->b" << endl;
		atob = CalNumTrain(gttbe, gttas);
		//cout << "b->a" << endl;
		btoa = CalNumTrain(gttae, gttbs);

		cout << "Case #"<< nCase << ": " << atob << " "  << btoa << endl;
	}
}

