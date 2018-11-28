#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <string>
#include <cstdio>
#include <cmath>

using namespace std;

int main() {
	int T;

	cin >> T;

	for (int t=1;t<=T;t++) {
		vector<pair<double, double> > walk;

		cout << "Case #" << t << ": ";
		double X, R, S, time, rt, N;
		cin >> X >> S >> R >> rt >> N;
		double len=X;
		for (int n=0;n<N;n++) {
			double B, E, w;
			cin >> B >> E >> w;
			walk.push_back(pair<double,double>(w,E-B));
			len=len-(E-B);
		}
		walk.push_back(pair<double,double>(0,len));
		sort(walk.begin(),walk.end());

		time=0;
		for (int i=0;i<walk.size();i++) {
			double timerun=walk[i].second/(walk[i].first+R);
			double timewalk=walk[i].second/(walk[i].first+S);
			if (timerun<=rt) { // run it
				time+=timerun;
				rt-=timerun;
			}
			else if (rt==0) { // walk it
				time+=timewalk;
			}
			else {
				time+=rt;
				double pdone=rt/timerun;
				time+=(1-pdone)*timewalk;
				rt=0;
			}

		}
		//cout << time;
		printf("%lf",time);
		cout << endl;
	}
	return 0;
}