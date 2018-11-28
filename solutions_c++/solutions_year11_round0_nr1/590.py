#include <iostream>
#include <fstream>
#include <vector>

using namespace std;


int n;


vector <int> seq[2];
vector <int> who;

int pos[2];
int nxt[2];

void Load()
{
	cin >> n;
	seq[0].clear(); seq[1].clear(); who.clear();
	for (int i = 0; i < n; i++) {
		int x;
		char w;
		int rw;
		cin >> w >> x;
//		cout << x << ' ' << w << "\n";
		if (w == 'O') {
			rw = 0;
		} else {
			rw = 1;
		}
		seq[rw].push_back(x);
		who.push_back(rw);
	}
	pos[0] = pos[1] = 1;
	nxt[0] = nxt[1] = 0;
}

void Solve()
{
	int cur, time;
	time = 0;
	cur = 0;

/*	for (int i = 0; i < who.size(); i++) cout << who[i] << ' ';
	cout << "\n";
	for (int j = 0; j < 2; j++) {
		for (int i = 0; i < seq[j].size(); i++)
			cout << seq[j][i] <<" ";
	   	cout << "\n";
	}
*/
	while (true) {
		int r = who[cur];
		bool waspressed = false;
//		cout << "pos: " << pos[0] << ' ' << pos[1] << "\n";
//		cout << "nextid: " << nxt[0] << ' ' << nxt[1] << "\n";
//		cout << "nextpos: " << seq[0][nxt[0]] << ' ' << seq[1][nxt[1]] << "\n";
//		cout << "time = " << time << "\n";
		for (r = 0; r < 2; r++) {
//			cout << "robo " << r << " ";
			if (cur == who.size() || nxt[r] == seq[r].size()) {
//				cout << "\n";
				continue;
			}
			if (seq[r][nxt[r]] == pos[r] && who[cur] == r && !waspressed) {//press the botton
//				cout << "button";
				waspressed = true;
				cur++;
				nxt[r]++;
			} else { // move is necessary
				if (pos[r] < seq[r][nxt[r]]) {
//					cout << "++";
					pos[r]++;
				} else if (pos[r] > seq[r][nxt[r]]) {
//					cout << "--";
					pos[r]--;
				}
			}
//			cout << "\n";
		}
		time++;
		if (cur == who.size()) break;
	}
	cout << time << "\n";

}

int main()
{
	int nt, tt;
	cin >> nt;
	for (tt = 1; tt <= nt; tt++)
	{
		Load();
		cout << "Case #" << tt << ": ";
		Solve();
	}
	return 0;
}
