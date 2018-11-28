/*
 *  File: ProblemA.cpp
 *  ------------------
 *
 *  Created by Elina Robeva on 6/4/11.
 *
 */

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <vector>
#include <math.h>
#include <iomanip>

using namespace std;


int main() {
	freopen("/Users/erobeva/Downloads/A-large (1).in","r",stdin);
	freopen("/Users/erobeva/Downloads/A-large.txt", "w", stdout);
	
	int T;
	cin >> T;
	for (int i = 0; i < T; ++i) {
		int N;
		int X, S, R, t;
		cin >> X >> S >> R >> t;
		cin >> N;
		vector<int> B(N);
		vector<int> E(N);
		vector<int> w(N);
		for(int j = 0; j < N; ++j) {
			cin >> B[j] >> E[j] >> w[j];
		}
		vector<int> speeds(X);
		double result = 0;
		
		int cur = 0;
		
		for(int s = 0; s < X; ++s) {
			while(E[cur] <= s && cur < N-1) {
				cur++;
			}
			if(B[cur] <= s && E[cur] > s) {
				speeds[s] = S + w[cur];
			} else {
				speeds[s] = S;
			}
			//cout << speeds[s] << endl;
		}
		
		sort(speeds.begin(), speeds.end());
		cur = 0;
		double time = t;
		double distance = 0;
		
		while(time > 0.000001 && cur < X) {
			int sp = speeds[cur] + R - S;
			//cout << "speed = " << sp << " time_remaining = " << time << " cur = " << cur << endl;
			if(time * sp >= 1) {
				distance += 1;
				time -= 1.0 / ((double) sp);
				cur++;
			} else {
				distance += time * sp;
				time = 0;
				cur++;
				break;
			}
		}
		
		//cout << "time = " << time << endl;
		result += t - time;
		
		if(ceil(distance) - distance > 0.000001 && cur > 0) {
			result += (ceil(distance) - distance) / ((double) speeds[cur-1]);
		}
		
		//cout << result << endl;
		//cout << "cur = " << cur << endl;
		
		for(int s = cur; s < X; ++s) {
			result += 1.0 / ((double) speeds[s]);
			//cout << result << endl;
		}

		cout << "Case #" << i + 1 << ": "<< setprecision(15) <<setiosflags(ios::showpoint) << (double) result << endl; 
	} 
	
	return 0;
}