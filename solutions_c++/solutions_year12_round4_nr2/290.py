#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    ofstream fout ("2B.out");
    ifstream fin ("2B.in");
	int T;
	fin >> T;
	for (int t = 1; t <= T; t++) {
		cout << "Working on Case #" << t << endl;
		int N,W,L;
		fin >> N >> W >> L;
		bool flipped = false;
		if (L < W) {
			int temp = L;
			L = W;
			W = temp;
			flipped = true;
		}
		pair<int,int> ans[1000];
		vector<pair<int,int> > circles;
		for (int i = 0; i < N; i++) {
			int r;
			fin >> r;
			circles.push_back(make_pair(r,i));
		}
		sort(circles.begin(),circles.end());
		reverse(circles.begin(),circles.end());
		int suml,maxr,curh;
		maxr = circles[0].first;
		curh = 0;
		suml = circles[0].first;
		ans[circles[0].second] = make_pair(0,0);
		for (int i = 1; i < N; i++) {
			if (suml + circles[i].first > L) {
				curh += maxr + circles[i].first;
				maxr = circles[i].first;
				suml = circles[i].first;
				ans[circles[i].second] = make_pair(curh,0);
			}
			else {
				suml += circles[i].first;
				ans[circles[i].second] = make_pair(curh,suml);
				suml += circles[i].first;
			}
		}
		fout << "Case #" << t << ":";
		for (int i = 0; i < N; i++) {
			if (flipped) fout << " " << ans[i].second;
			fout << " " << ans[i].first;
			if (!flipped) fout << " " << ans[i].second;
		}
		fout << endl;
	}
    return 0;
}