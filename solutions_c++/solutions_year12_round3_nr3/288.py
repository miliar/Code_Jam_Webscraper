#include <sstream>
#include <fstream>
#include <iostream>
#include <iomanip>

#include <cmath>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>

using namespace std;

namespace {
typedef long long ll;
struct hogehoge {
	ll score;
	int pos;
	ll consume;

	hogehoge(ll scor, int po, ll consu) {
		score = scor; pos = po; consume = consu;
	}
};

const string& directory_path = "D:\\GCJ\\GoogleCodeJam\\";

const string& input_file_path = "C-small-attempt0.in";
ifstream ifs(directory_path + input_file_path);
const string& output_file_path = "output.txt";
ofstream ofs(directory_path + output_file_path);

void WriteResult(int t, ll result) {
	ofs << "Case #" << t << ": " << result << endl;
}
} //namespace {anonymous}

int main() {
	int T;
	ifs >> T;

	for (int t = 1; t <= T; ++t) {
		int N, M;
		ifs >> N >> M;

		vector<ll> a_size;
		vector<ll> a_type;
		for (int i = 0; i < N; ++i) {
			ll a, A;
			ifs >> a >> A;
			a_size.push_back(a);
			a_type.push_back(A);
		}

		vector<ll> b_size;
		vector<ll> b_type;
		for (int i = 0; i < M; ++i) {
			ll b, B;
			ifs >> b >> B;
			b_size.push_back(b);
			b_type.push_back(B);
		}

		vector<hogehoge> cand;
		cand.push_back(hogehoge(0LL, 0, 0LL));
		for (int i = 0; i < N; ++i) {
			int size = cand.size();
			for (int k = 0; k < size; ++k) {
				ll addition = 0LL;
				hogehoge hoge = cand[k];
				int j = hoge.pos;

				if (hoge.consume > 0LL && a_type[i] == b_type[j]) {
					ll add = b_size[hoge.pos] - hoge.consume;
					if (a_size[i] >= add) {
						addition = add;
						cand.push_back(hogehoge(hoge.score + add, j + 1, 0LL)); 
					} else {
						cand.push_back(hogehoge(hoge.score + a_size[i], j, hoge.consume + a_size[i])); 
						continue;
					}
					++j;
				}

				for (; addition < a_size[i] && j < M; ++j) {
					if (a_type[i] == b_type[j]) {
						if (addition + b_size[j] <= a_size[i]) {
							addition += b_size[j];
							cand.push_back(hogehoge(hoge.score + addition, j + 1, 0LL));
						} else {
							ll consume = a_size[i] - addition;
							addition = a_size[i];
							cand.push_back(hogehoge(hoge.score + addition, j, consume));
						}
					}
				}
			}
		}

		ll result = 0LL;
		for (size_t i = 0; i < cand.size(); ++i) {
			if (result < cand[i].score) {
				result = cand[i].score;
			}
		}

		WriteResult(t, result);
	}

	return 0;
}