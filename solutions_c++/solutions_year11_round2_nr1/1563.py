#include <iostream>
#include <iomanip>
#include <cstdlib>
#include <vector>
using namespace std;

vector<double> solve(vector< vector<int> > s);

int main(/*int argc, char** argv*/) {
    unsigned int T = 0;

    cin >> T;
    for (unsigned int t = 0; t < T; ++t) {
        unsigned int n;
        vector<vector <int> > schedule;

		cin >> n;
        schedule.resize(n);
        for (unsigned int i = 0; i < n; ++i) {
            schedule[i].resize(n);
			for (unsigned int j = 0; j < n; ++j) {
				char c;
				cin >> c;
				if (c == '.') schedule[i][j] = 0;
				else if (c == '1') schedule[i][j] = 1;
				else if (c == '0') schedule[i][j] = -1;
				else --j;
			}
        }

        vector<double> result = solve(schedule);
        cout << "Case #" << (t + 1) << ":" << endl;
		for (unsigned int i=0;i<result.size();++i) cout << result[i] << endl;
    }
    return 0;
}

vector<double> solve(vector<vector<int> > s) {
	unsigned int n = s.size();
	vector<int> total, wins;
	vector<double> wp, owp, oowp, result;
	total.resize(n);
	wins.resize(n);
	wp.resize(n);owp.resize(n);oowp.resize(n);result.resize(n);
	for(unsigned int i=0;i<n;++i) {
		total[i] = 0;
		wins[i] = 0;
		for (unsigned int j=0;j<n;++j) {
			if (s[i][j] != 0) ++total[i];
			if (s[i][j] == 1) ++wins[i];
		}
	}
	for(unsigned int i=0;i<n;++i) {
		wp[i] = wins[i]*1.0/total[i];
		owp[i] = 0;
		int k = 0;
		for (unsigned int j=0;j<n;++j) {
			if (s[i][j] != 0) {
				owp[i] += (wins[j] - (s[j][i] == 1?1:0))*1.0 / (total[j] - (s[j][i] != 0?1:0));
				++k;
			}
		}
		owp[i] = owp[i]*1.0/k;
	}
	for(unsigned int i=0;i<n;++i) {
		oowp[i] = 0;
		int k = 0;
		for (unsigned int j=0;j<n;++j) {
			if (s[i][j] != 0) {oowp[i] += owp[j];++k;}
		}
		oowp[i] = oowp[i]*1.0/k;
	}
	for(unsigned int i=0;i<n;++i) {
		result[i] = wp[i] *0.25 + owp[i] * 0.5 + oowp[i] * 0.25;
	}

	return result;
}
