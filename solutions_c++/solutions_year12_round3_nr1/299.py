#include <sstream>
#include <fstream>
#include <iostream>
#include <iomanip>

#include <queue>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>

using namespace std;

namespace {
const string& directory_path = "D:\\GCJ\\GoogleCodeJam\\";

const string& input_file_path = "A-large.in";
ifstream ifs(directory_path + input_file_path);
const string& output_file_path = "output.txt";
ofstream ofs(directory_path + output_file_path);

void WriteResult(int t, bool result) {
	if (result) {
		ofs << "Case #" << t << ": Yes" << endl;
	} else {
		ofs << "Case #" << t << ": No" << endl;
	}
}
} //namespace {anonymous}

int main() {
	int T;
	ifs >> T;

	for (int t = 1; t <= T; ++t) {
		int N;
		ifs >> N;

		vector<vector<int> > inheritance;
		for (int n = 0; n < N; ++n) {
			int num;
			ifs >> num;

			vector<int> inh;
			for (int q = 0; q < num; ++q) {
				int in;
				ifs >> in;
				inh.push_back(in-1);
			}

			inheritance.push_back(inh);
		}

		bool result = false;
		for (int i = 0; !result && i < N; ++i) {
			queue<int> que;
			que.push(i);

			vector<int> counts(N, 0);
			while (!result && !que.empty()) {
				int id = que.front();
				que.pop();

				for (size_t l = 0; l < inheritance[id].size(); ++l) {
					int next_id = inheritance[id][l];
					++counts[next_id];
					if (counts[next_id] == 2) {
						result = true;
						break;
					}
					que.push(next_id);
				}
			}
		}
		WriteResult(t, result);
	}

	return 0;
}