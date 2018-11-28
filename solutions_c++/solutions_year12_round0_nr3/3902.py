#include<iostream>
#include<vector>
#include<fstream>
#include<map>
#include<string>
#include<set>

using namespace std;

void digits(int k, vector<int> * digits) {
	while(k > 0) {
		digits->push_back(k % 10);
		k /= 10;
	}

}

int mylog(int k) {
	int res = 0;
	while(k > 0) {
		++res;
		k /= 10;
	}
	return res - 1;
}

int pow10(int k) {
	int res = 1;
	for (int i = 0; i < k; ++i) {
		res *= 10;
	}
	return res;
}

int countCycles(int k, int a, int b, int log, int st) {
	int cycle = k;
	int count = 1;
	for (int i = 0; i < log; ++i) {
		cycle = (cycle % st) * 10 + cycle / st;
		if (cycle == k) {
			break;
		}
		if (cycle >= max(a, st) && cycle <= b) {
			++count;
			if (cycle < k) {
				return 0;
			}
		}
	}
	return count * (count - 1) / 2;
}



int main() {
	ifstream inp;
	ofstream out;
	inp.open("input.txt");
	out.open("output.txt");
	int t;
	inp >> t;
	for (int test = 0; test < t; ++test) {
		int a, b;
		inp >> a;
		inp >> b;
		long long res = 0;
		int log = mylog(a);
		int st = pow10(log);
		for (int i = a; i <= b; ++i) {
			if (i == st * 10) {
				st *= 10;
				log += 1;
			}
			res += countCycles(i, a, b, log, st);
		}
		out << "Case #" << test + 1 << ": " << res << endl;
	}

	return 0;
}