#include <iostream>
#include <string>
using namespace std;

const int MAXN = 200;
int na, nb;
struct line_t {
	int s, t;
	bool isAToB;
	bool ok;
};
line_t line[MAXN];
int turnAroundTime;

int HHMMtoMinute(string str) {
	string s1 = str.substr(0,2);
	string s2 = str.substr(3,2);
	int h = atoi(s1.c_str());
	int m = atoi(s2.c_str());
	return h*60+m;
}

bool compareLine(const line_t &l, const line_t &r) {
	return l.s < r.s;
}

void putTrain(int i) {
	line[i].ok = 1;
	for (int j = i+1; j < na+nb; j++)
		if (!line[j].ok && line[j].isAToB != line[i].isAToB && line[j].s >= line[i].t) {
			putTrain(j);
			break;
		}
}

void process() {
	int resA = 0, resB = 0;
	cin >> turnAroundTime;
	cin >> na >> nb;
	for (int i = 0; i < na+nb; i++) {
		string tmp1, tmp2;
		cin >> tmp1 >> tmp2;
		line[i].s = HHMMtoMinute(tmp1);
		line[i].t = HHMMtoMinute(tmp2) + turnAroundTime;
		line[i].isAToB = (i < na);
		line[i].ok = 0;
	}

	sort(line, line+na+nb, compareLine);
	for (int i = 0; i < na+nb; i++)
		if (!line[i].ok) {
			if (line[i].isAToB)
				resA++;
			else
				resB++;
			putTrain(i);
		}

	cout << resA << " " << resB << endl;
}

int main() {
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		cout << "Case #" << i+1 << ": ";
		process();
	}
}

