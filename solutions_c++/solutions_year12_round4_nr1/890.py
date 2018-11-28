#include <iostream>
#include <fstream>
#include <vector>
#include <math.h>
#include <queue>

using namespace std;

int main(int argc, const char * argv[])
{
	ifstream ifs( "input.txt" );
    int T = 0;
    ifs >> T;
    for (int i = 0; i < T; i++) {
		int N;
		ifs >> N;
		vector<pair<int, int > > ledges;
		for (int j = 0; j < N; j++) {
			int d, l;
			ifs >> d >> l;
			ledges.push_back(make_pair(d, l));
		}
		int D;
		ifs >> D;
		bool suc = false;
		ledges.push_back(make_pair(D, 0));
		queue<pair<int, int> > q;
		q.push(make_pair(0, ledges[0].first));
		while (q.size()) {
			pair<int, int> now = q.front();
			q.pop();
			for (int j = now.first+1; j < ledges.size(); j++) {
				if (ledges[j].first-ledges[now.first].first <= now.second) {
					if (j == ledges.size()-1) {
						suc = true;
						goto PRINT;
					}
					int h = min(ledges[j].second, ledges[j].first-ledges[now.first].first);
					q.push(make_pair(j, h));
				}
			}
		}
	PRINT:
		cout << "Case #" << i+1 << ": " << (suc?"YES":"NO") << endl;
	}
}
