#include <string>
#include <iostream>
#include <sstream>
using namespace std;

int main() {
	string line;
	istringstream line_stream;

	int T;
	getline(cin, line);
	line_stream.str(line);
	line_stream >> T;

	for (int case_num = 1; case_num <= T; ++case_num) {
		long long R, k, N;
		getline(cin, line);
		line_stream.clear();
		line_stream.str(line);
		line_stream >> R >> k >> N;

		//R = 1000*1000*100; // uncomment to time large cases

		long long gs[N], rot[N][N], limit[N], tots[N];
		getline(cin, line);
		line_stream.clear();
		line_stream.str(line);
		for (int i = 0; i < N; ++i) {
			line_stream >> gs[i];
			for (int j = 0; j < N; ++j)
				rot[j][(i-j+N)%N] = gs[i];
		}

		for (int r = 0; r < N; ++r) {
			tots[r] = 0;
			limit[r] = N;
			for (int c = 0; c < N; ++c) {
				tots[r] += rot[r][c];
				if (tots[r] > k) {
					limit[r] = c;
					tots[r] -= rot[r][c];
					break;
				}
			}
		}

		int pos = 0;
		long long revenue = 0;
		for (int i = 0; i < R; ++i) {
			/*
			cout << pos << " " << limit[pos] << " " << tots[pos] << endl;
			cout << " ";
			for (int j = 0; j < N; ++j)
				cout << rot[pos][j] << " ";
			cout << endl;
			*/
			revenue += tots[pos];
			pos = (pos + limit[pos]) % N;
		}

		cout << "Case #" << case_num << ": " << revenue << endl;
	}
}
