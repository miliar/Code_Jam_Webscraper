#include <cstdio>
#include <iostream>
#include <string>
#include <utility>
#include <vector>
#include <map>
#include <sstream>

using namespace std;

typedef pair<int, int> pii;
typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<int> vll;
typedef vector<string> vs;

#define FORITER(i, x) for (typeof((x).begin()) i = (x).begin(); i != (x).end(); i++)
#define FOR(i, a, b) for (int i = a; i < b; ++i)
#define FORI(n) FOR(i,0,n)
#define FORJ(n) FOR(j,0,n)
#define FORK(n) FOR(k,0,n)
#define MEM(var, v) memset(var, v, sizeof(var))
#define GETINT(row,col,q) FORI(row) FORJ(col) cin >> q[i][j]
#define GETCHAR(row,col,q) FORI(row) {string line; cin >> line; FORJ(col) q[i][j]=line.at(j);}
#define TESTOUT FORI(T) cout << "Case #" << i+1 << ": "
#define DBG(mi,mj,q) FORI(mi){FORJ(mj){ cout << q[i][j];} cout << endl;}

int T = 0;

string addZero(string str)
{
	return "NEXT";
}

void sort(string& line, int idx)
{
	int num[10];
	MEM(num, 0);

	for(int i = idx; i < line.length(); i++)
		num[line[i] - '0']++;

	FORI(10) {
		FORJ(num[i]) {
			line[idx] = i + '0';
			idx++;
		}
	}
}

void nextBig(string& line)
{
	int minIdx = 0;
	FOR (i, 1, line.length()) {
		if (line[i] != '0' && line[minIdx] >= line[i])
			minIdx = i;
	}

	if(minIdx != 0) {
		char temp = line[0];
		line[0] = line[minIdx];
		line[minIdx] = temp;
	}

	sort(line, 1);

	stringstream ss;
	ss << line[0] << "0" << line.substr(1);

	line = ss.str();

}

string play()
{
	string line;
	getline(cin, line);

	const int END = line.length();

	bool isSwaped = false;

	int firstIdx[10];
	MEM(firstIdx, -1);
	firstIdx[line[END-1]-'0'] = END-1;

	for(int i = END - 2; i >= 0; i--) {
		for(int j  = line[i] - '0' + 1; j < 10; j++) {
			if(firstIdx[j] != -1) {
				char temp = line[firstIdx[j]];
				line[firstIdx[j]] = line[i];
				line[i] = temp;
				isSwaped = true;
				break;
			}
		}
		if(isSwaped) {
			sort(line, i+1);
			break;
		}
		else {
			firstIdx[line[i] - '0'] = i;
		}
	}

	if(!isSwaped)
		nextBig(line);

	return line;
}

int main() {
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	cin >> T;
	string line;
	getline(cin, line);

	TESTOUT << play() << endl;
	return 0;
}
