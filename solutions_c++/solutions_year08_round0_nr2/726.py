#include <functional> 
#include <numeric> 
#include <sstream> 
#include <iostream> 
#include <iterator> 
#include <algorithm> 
#include <utility> 

// container 
#include <vector> 
#include <string> 
#include <set> 
#include <map> 

// C-style 
#include <cmath> 
#include <cstdio> 
#include <cstdlib> 

using namespace std;

#define FOR(_I,_A,_B) for(int _I=(_A);(_I)<(_B);_I++)
#define FORE(_I,_A,_B) for(int _I=(_A);(_I)<=(_B);_I++) 
#define REP(_I,_B) for(int _I=(0);(_I)<(_B);_I++) 

typedef long long ll;
typedef long double ld;

int N, NAB, NBA, T;

enum { arrive=0, depart=1 };

struct timetable {
	int type;
	int station;
	int time;

	timetable(){}
	timetable(int _type, char _station, int _time) : type(_type), station(_station), time(_time) {}
	bool operator<(timetable t) const {
		if(time==t.time) return type < t.type;
		return time< t.time;
	}
};

vector<timetable> tbl;

int gettime(string s) {
	return ((s[0]-'0')*10+s[1]-'0')*60+(s[3]-'0')*10+s[4]-'0';
}

int main(void) {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	cin >> N;

	FORE(tc, 1, N) {
		tbl.clear();

		cin >> T >> NAB >> NBA;
		
		REP(i, NAB) {
			string s, e;
			cin >> s >> e;
			
			tbl.push_back(timetable(depart, 'A', gettime(s)));
			tbl.push_back(timetable(arrive, 'B', gettime(e)+T));
		}

		REP(i, NBA) {
			string s, e;
			cin >> s >> e;

			tbl.push_back(timetable(depart, 'B', gettime(s)));
			tbl.push_back(timetable(arrive, 'A', gettime(e)+T));
		}
		
		sort(tbl.begin(), tbl.end());

		int ntbl = tbl.size();
		int res[2] = {0, };
		int carry[2] = {0, };
		REP(i, ntbl) {
			timetable t = tbl[i];
			if(t.type==arrive) {
				carry[t.station-'A']++;
			}
			else if(t.type==depart) {
				if(carry[t.station-'A']>0) {
					carry[t.station-'A']--;
				}
				else {
					res[t.station-'A']++;
				}
			}
		}

		printf("Case #%d: %d %d\n", tc, res[0], res[1]);
	}
	return 0;
}
