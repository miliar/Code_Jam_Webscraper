#include <set>
#include <map>
#include <cmath>
#include <vector>
#include <string>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <utility>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <functional>

using namespace std;

string input = "D-small-attempt2.in", output = input + "___.out";
ifstream ifs(input.c_str());
ofstream ofs(output.c_str());

static char buf[1024], buff[1024];

void gen(int k, vector<int>& p)
{
	for (int i = 0; buf[i] != '\0'; i += k) {
		for (int j = 0; j < k; j++) {
			buff[i + j] = buf[i + p[j]];
		}
	}
}

int cnt(int l)
{
	int ret = 1;

	for (int i = 1; i < l; i++) {
		if (buff[i] != buff[i - 1]) {
			++ret;
		}
	}

	return ret;
}

int main(void)
{
	int re;
	int k, l;

	ifs >> re;
	for (int ri = 1; ri <= re; ri++) {
		cerr << ri;
		ifs >> k >> buf;
		int ans = l = strlen(buf);
		vector<int> p;
		for (int i = 0; i < k; i++) {
			p.push_back(i);
		}
		do {
			gen(k, p);
			ans = min(ans, cnt(l));
		} while (next_permutation(p.begin(), p.end()));
		// output
		ofs << "Case #" << ri << ": " << ans << endl;
	}

	return 0;
}
