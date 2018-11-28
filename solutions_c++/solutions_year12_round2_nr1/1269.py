#include <sstream>
#include <fstream>
#include <iostream>
#include <iomanip>

#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>

using namespace std;


namespace {
const string& directory_path = "D:\\GCJ\\GoogleCodeJam\\";

const string& input_file_path = "A-large.in";
const string& output_file_path = "output.txt";

} //namespace {anonymous}

int main() {
	ifstream ifs(directory_path + input_file_path);
	ofstream ofs(directory_path + output_file_path);

	int T;
	ifs >> T;

	ofs.precision(8);

	for (int t = 1; t <= T; ++t) {
		int N;
		ifs >> N;

		double sum = 0.0;
		vector<int> s;
		for (int n = 0; n < N; ++n) {
			int score;
			ifs >> score;
			s.push_back(score);
			sum += score;
		}

		vector<double> results(N, -1.0);;

		double allocatable = sum;
		double check_N = N;

		bool check = true;
		while (check) {
			check = false;

			double lower_bound = (double)(allocatable + sum) / (double)check_N;

			double max_value = -1.0;
			int max_id = -1;

			for (int n = 0; n < N; ++n) {
				if (results[n] != -1.0) continue;

				if (lower_bound < s[n]) {
					check = true;

					if (max_value < s[n]) {
						max_value = s[n];
						max_id = n;
					}
				}
			}

			if (check) {
				results[max_id] = 0.0;
				allocatable -= s[max_id];
				check_N -= 1.0;
			}
		}

		{
			ofs << "Case #" << t << ": ";
			double lower_bound = (double)(allocatable + sum) / (double)check_N;
			for (int n = 0; n < N; ++n) {
				if (results[n] != -1.0) {
					ofs << results[n];
				} else {
					double ness = max(0.0, 100.0 * (lower_bound - (double)s[n]) / (double)sum);
					ofs << ness;
				}
				if (n != N-1) ofs << " ";
			}
			if (t != T) {
				ofs << endl;
			}
		}
	}

	return 0;
}