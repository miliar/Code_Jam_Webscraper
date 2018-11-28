#include <vector>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <map>
#include <utility>
#include <string>
#include <cstring>
using namespace std;

bool compFunc(const pair<int,int> &t1, const pair<int,int> &t2)
{
	int len1 = t1.second-t1.first;
	if (len1 > 4) len1 = 8-len1;
	int len2 = t2.second-t2.first;
	if (len2 > 4) len2 = 8-len2;

	if (len1 < len2) return true;
	if (len1 > len2) return false;
	return t1 < t2;
}

int getPart(string &points, int start, int end)
{
	int pos1, pos2;
	int i;
	for (i=0; i<points.size(); ++i) {
		if (points[i]-'0' == start) pos1 = i;
		else if (points[i]-'0' == end) pos2 = i;
	}

	int ans = 0;
	if (end-start <= 4) {
		for (i=pos1; i<=pos2; ++i) {
			ans |= 1<<(points[i]-'0');
		}

		string s = points.substr(pos2, points.length()-pos2);
		points = points.substr(0, pos1+1) + s;

		return ans;
	}

	for (i=0; i<=pos1; ++i) {
		ans |= 1<<(points[i]-'0');
	}
	for (i=pos2; i<points.length(); ++i) {
		ans |= 1<<(points[i]-'0');
	}

	points = points.substr(pos1, pos2-pos1+1);
	return ans;
}

int bitnum(int a)
{
	int ans = 0;
	while (a) {
		ans++;
		a &= a-1;
	}
	return ans;
}

int color[10];
int colorNum;
vector<int> parts;
int N, M;

bool tryColor(int pos)
{
	if (pos == N+1) return true;

	int i, j;
	vector<int> relParts;
	for (j=0; j<parts.size(); ++j) {
		int a = parts[j];
		if (!(a&(1<<pos))) continue;
		for (i=pos+1; i<=N; ++i) if (a&(1<<i)) {
			break;
		}
		if (i <= N) continue;
		relParts.push_back(a);
	}

	for (i=1; i<=colorNum; ++i) {
		color[pos] = i;
		for (j=0; j<relParts.size(); ++j) {
			int a = 0;
			for (int k=1; k<=pos; ++k) if (relParts[j] & (1<<k)) {
				a |= 1<<color[k];
			}
			if (bitnum(a) < colorNum) break;
		}
		if (j < relParts.size()) continue;

		if (tryColor(pos+1)) return true;
	}

	return false;
}

string calc()
{
	stringstream S;
	int i, j;
	cin >> N >> M;

	vector<int> starts(M);
	for (i=0; i<M; ++i) {
		cin >> starts[i];
	}

	vector<pair<int,int> > lines(M);
	for (i=0; i<M; ++i) {
		lines[i].first = starts[i];
		cin >> lines[i].second;
	}

	sort(lines.begin(), lines.end(), compFunc);

	string points;
	for (i=0; i<N; ++i) {
		points += '1'+i;
	}

	parts.clear();

	for (i=0; i<lines.size(); ++i) {
		int start = lines[i].first;
		int end = lines[i].second;
		parts.push_back(getPart(points, start, end));
	}

	int a = 0;
	for (i=0; i<points.length(); ++i) {
		a |= 1<<(points[i]-'0');
	}
	parts.push_back(a);

	if (parts.size() != M+1) {
		//cerr << "parts.size() != M+1 " << parts.size() << ' ' << M+1 << endl;
	}

	for (i=0; i<parts.size(); ++i) {
		//cerr << parts[i] << endl;
	}
	//cerr << endl;

	int minPartSize = N;
	for (i=0; i<parts.size(); ++i) {
		int n = bitnum(parts[i]);
		if (n < minPartSize) minPartSize = n;
	}

	color[1] = 1;

	for (colorNum = minPartSize; colorNum>=1; colorNum--) {
		for (i=2; i<10; ++i) color[i] = -1;

		if (tryColor(2)) {
			S << colorNum << endl;
			for (i=1; i<=N; ++i) {
				S << color[i];
				if (i < N) S << ' ';
			}
			return S.str();
		}
	}

	return S.str();
}

int main(void)
{
	int caseNum;
	cin >> caseNum;
	//string line;
	//getline(cin, line);
	for (int c=1; c<=caseNum; ++c) {
		cout << "Case #" << c << ": " << calc() << endl;
	}

	return 0;
}

