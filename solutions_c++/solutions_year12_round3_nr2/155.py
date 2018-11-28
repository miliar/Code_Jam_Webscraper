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

const string& input_file_path = "B-small-attempt2.in";
ifstream ifs(directory_path + input_file_path);
const string& output_file_path = "output.txt";
ofstream ofs(directory_path + output_file_path);

void WriteResult(int t, vector<double> result) {
	ofs << "Case #" << t << ":" << endl;
	for (size_t n = 0; n < result.size(); ++n) {
		ofs << result[n] << endl;
	}
}
} //namespace {anonymous}

int main() {
	ofs.precision(20);

	int T;
	ifs >> T;

	for (int t = 1; t <= T; ++t) {
		double distance;
		int N, A;
		ifs >> distance >> N >> A;

		vector<pair<double, double> > t_and_p;
		for (int n = 0; n < N; ++n) {
			double time, position;
			ifs >> time >> position;
			t_and_p.push_back(make_pair(time, position));
		}

		vector<double> result;
		for (int a_ = 0; a_ < A; ++a_) {
			double acceleration;
			ifs >> acceleration;

			if (N == 1) {
				double alpha =  2.0 * distance / acceleration;
				double res = sqrt(alpha);
				result.push_back(res);
				continue;
			}

			double goal_time = 0.0;
			for (int id = 0; id < N; ++id) {
				if (t_and_p[id].second >= distance) {
					if (id != 0) {
						double last_velocity = (t_and_p[id].second - t_and_p[id-1].second)
							/ (t_and_p[id].first - t_and_p[id-1].first);
						goal_time = t_and_p[id-1].first + (distance - t_and_p[id-1].second) / last_velocity;
					}
					break;
				}
			}

			double prev_time = 0.0;
			double prev_position = 0.0;
			double prev_velocity = 0.0;
			for (int id = 1; id < N; ++id) {
				if (distance > t_and_p[id].second) {
					double available_time = t_and_p[id].first - prev_time;
					double reachable_position = prev_position
						+ prev_velocity * available_time
						+ 0.5 * acceleration * available_time * available_time;
					if (reachable_position >= t_and_p[id].second) {
						prev_position = t_and_p[id].second;
						prev_velocity = sqrt((2.0 * prev_position) / acceleration);
					} else {
						prev_position = reachable_position;
						prev_velocity += available_time * acceleration;
					}
					prev_time = t_and_p[id].first;
				} else {
					break;
				}
			}

			cout << prev_time << endl;

			double reachable_position = prev_position
						+ prev_velocity * (goal_time - prev_time)
						+ 0.5 * acceleration * (goal_time - prev_time) * (goal_time - prev_time);

			if (reachable_position >= distance) {
				result.push_back(goal_time);
			} else {
				double alpha = ((prev_velocity * prev_velocity / (2.0 * acceleration)) + (distance - prev_position)) * 2.0 / acceleration;
				double res = - (prev_velocity / acceleration) + sqrt(alpha);
				result.push_back(prev_time + res);
			}
		}

		WriteResult(t, result);
	}

	return 0;
}