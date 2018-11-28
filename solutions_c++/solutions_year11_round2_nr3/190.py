#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <set>

using namespace std;

#define REP(a,b) for (int a=0; a<b; ++a)

int color[2000];
int nVert, nColor, nRooms;
vector <int> rm[2001];

bool check()
{
	REP(i,nRooms) {
		int msk = 0;
		REP(j,rm[i].size()) {
			msk = msk | (1<<color[rm[i][j]-1]);
		}
		if ( msk != ( (1<<(nColor)) - 1 ) ) return false;
	}
	return true;
}

bool bf(int pos) {
	if (pos == nVert) {
		return check();
	} else {
		REP(i,nColor) {
			color[pos] = i;
			if (bf(pos+1)) return true;
		}
	}

	return false;
}

int main() 
{
	ifstream fin("c.in");
	ofstream fout("c.out");

	int tc, n, m, nc;
	int u[2001], v[2001];

	fin >> tc;

	REP(t,tc) {
		fin >> n >> m;

		REP(i,m) fin >> u[i];
		REP(i,m) fin >> v[i];


		vector <set<int> > rooms;
		set <int> room;

		REP(i,n) room.insert(i+1);
		rooms.push_back(room);

		REP(i,m) {
			REP(j,rooms.size()) if (rooms[j].find(u[i]) != rooms[j].end() && rooms[j].find(v[i]) != rooms[j].end()) {
				set <int> newroom1, newroom2;
				for (set<int>::iterator it = rooms[j].begin(); it!=rooms[j].end(); ++it) {
					if (*it >= u[i] && *it <= v[i]) newroom1.insert(*it);
					if (*it <=u [i] || *it >= v[i]) newroom2.insert(*it);
				}
				rooms[j] = newroom1;
				rooms.push_back(newroom2);
				break;
			}
		}

		nRooms = rooms.size();
		REP (i,nRooms) {
			rm[i].clear();
			for (set<int>::iterator it = rooms[i].begin(); it!=rooms[i].end(); ++it) {
				rm[i].push_back(*it);
			}
		}
		nVert = n;

		for (nc = 5; nc > 0; --nc) {
			nColor = nc;
			if (bf(0)) break;
		}

		cout << t << endl;
		fout << "Case #" << t+1 << ": " << nc << endl;
		fout << color[0]+1;
		for (int i = 1; i < n; ++i) fout << " " << color[i]+1;
		fout << endl;
	}

	fout.close();

	return 0;
}