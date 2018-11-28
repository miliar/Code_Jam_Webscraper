#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>

using namespace std;

struct Move {
	char c;
	int num;
};

vector<char> calc(vector<char> &seq, vector<string> &comb, vector<string> &opp) {
	vector<char> s;

	char c_[26][26];
	char o_[26][26];
	for (int i = 0; i < 26; ++i) {
		for (int j = 0; j < 26; ++j) {
			c_[i][j] = 0;
			o_[i][j] = 0;
		}
	}
//cout << "---------------\n";
	for (unsigned int i = 0; i < comb.size(); ++i) {
		string str = comb[i];
		c_[str[0]-'A'][str[1]-'A'] = str[2];
//		cout << static_cast<int>(str[0]-'A') << "," << static_cast<int>(str[1]-'A')
//				<< " -> " << str[2] << "\n";
		c_[str[1]-'A'][str[0]-'A'] = str[2];
	}
	for (unsigned int i = 0; i < opp.size(); ++i) {
		string str = opp[i];
		o_[str[0]-'A'][str[1]-'A'] = 1;
		o_[str[1]-'A'][str[0]-'A'] = 1;
	}

	for (unsigned int i = 0; i < seq.size(); ++i) {
		bool stop = false;

		if (!s.empty()) {
			int last = s[s.size()-1] - 'A';
			// is composed
			if (c_[last][seq[i]-'A'] > 0) {
				s[s.size()-1] = c_[last][seq[i]-'A'];
				stop = true;
			}
			if (!stop) {
				// is opposed
				for (unsigned int j = 0; j < s.size(); ++j) {
					if (o_[s[j]-'A'][seq[i]-'A'] > 0) {
						s.clear();
						stop = true;
						break;
					}
				}
			}
		}
		if (!stop)
			s.push_back(seq[i]);
	}


	return s;
}

int main(int argc, char **argv) {
	string ifilename = "B.in";
	string ofilename = "B.out";
	ifstream ifs(ifilename.c_str());
	ofstream ofs(ofilename.c_str());

	int t;
	ifs >> t;

	for (int i = 0; i < t; ++i) {
		int c, d, n;

		char z;
		string s;
		vector<string> comb;
		vector<string> opp;
		vector<char> seq;
		ifs >> c;
		for (int j = 0; j < c; ++j) {
			ifs >> s;
			comb.push_back(s);
		}

		ifs >> d;
		for (int j = 0; j < d; ++j) {
			ifs >> s;
			opp.push_back(s);
		}

		ifs >> n;
		for (int j = 0; j < n; ++j) {
			ifs >> z;
			seq.push_back(z);
		}

		vector<char> res = calc(seq, comb, opp);
		ofs << "Case #" << (i+1) << ": [";
		for (unsigned int j = 0; j < res.size(); ++j) {
			ofs << res[j];
			if (j < res.size() - 1)
				ofs << ", ";
		}
		ofs << "]" << endl;
	}



	ifs.close();
	ofs.close();
	return 0;
}
