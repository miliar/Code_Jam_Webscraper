#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <cmath>

using namespace std;

inline bool isValid(int a, int b, int c) {
	return abs((double)a - b) <= 2 && abs((double)b - c) <= 2 && abs((double)a - c) <= 2;
}

inline size_t getNormalScore(size_t n) {
	return (n+2)/3;
}

/**
 * Computes the best normal score for every possible total score in the [0...30] interval.
 */
map<size_t, size_t> getNormalScores() {
	map<size_t, size_t> result;

	for(size_t i = 0; i <= 30; i++) {
		result.insert(make_pair(i, getNormalScore(i)));
	}

	return result;
}

size_t getSurprisingScore(size_t n) {
	size_t m = n/3;

	size_t result = 0;
	//size_t aResult = 0;
	//size_t bResult = 0;
	//size_t cResult = 0;
	for(size_t a = (size_t)max(0, (int)m - 2); a <= (size_t)min(10, (int)m + 2); a++) {
		for(size_t b = a; b <= (size_t)min(10, (int)m + 2); b++) {
			for(size_t c = b; c <= (size_t)min(10, (int)m + 2); c++) {
				if(a + b + c == n && isValid(a, b, c) && max(max(a, b), c) > result){
					result = max(max(a, b), c);

					//aResult = a;
					//bResult = b;
					//cResult = c;
				}
			}
		}
	}

	//cout<<n<<"\t"<<result<<"\t"<<aResult<<"\t"<<bResult<<"\t"<<cResult<<endl;

	return result;
}

/**
 * Computes the best surprising score for every possible total score in the [0...30] interval.
 */
map<size_t, size_t> getSurprisingScores() {
	map<size_t, size_t> result;

	for(size_t i = 0; i <= 30; i++) {
		result.insert(make_pair(i, getSurprisingScore(i)));
	}

	return result;
}

map<size_t, size_t> normalScores = getNormalScores();
map<size_t, size_t> surprisingScores = getSurprisingScores();

size_t computeBestScores(size_t N, size_t S, size_t p, vector<size_t>& t) {
	vector<size_t> filteredT;

	size_t maximumBestScores = 0;

	for(size_t i = 0; i < t.size(); i++) {
		if(normalScores.at(t[i]) >= p) {
			// no matter the configuration, the score will be >= p
			maximumBestScores++;
		}
		else if(surprisingScores.at(t[i]) >= p) {
			// the surprising score allows best score to be >= p
			filteredT.push_back(t[i]);
		}
		// else
		// even with surprising score, the best score is < p
	}

	return maximumBestScores + min(S, filteredT.size());
}

int main(int argc, char** argv) {
	ifstream in("input.in");
	ofstream out("out.txt");

	size_t T;
	in >> T;

	/**
	for(size_t i = 0; i < normalScores.size(); i++) {
		cout<<i<<"\t"<<normalScores.at(i)<<"\t"<<surprisingScores.at(i)<<endl;
	}
	**/

	for (size_t i = 0; i < T; i++) {
		size_t N, S, p;
		in >> N >> S >> p;

		vector<size_t> t;
		for (size_t j = 0; j < N; j++) {
			size_t temp;
			in >> temp;
			t.push_back(temp);
		}

		size_t maxGooglers = computeBestScores(N, S, p, t);
		out << "Case #" << (i + 1) << ": " << maxGooglers << endl;
	}

	in.close();
	out.close();

	return 0;
}
