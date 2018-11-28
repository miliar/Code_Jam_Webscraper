#include <cstdio>
#include <string>
#include <iostream>
#include <vector>

using namespace std;

vector<int> opposed[30];
int combine[30][30];

void print(vector<int> &r) {
	printf("[");
	if(!r.empty()) printf("%c", r[0]+'A');
	for(int i = 1; i < r.size(); i++) printf(", %c", r[i]+'A');
	printf("]\n");
}

void solve(int caseNumber) {
	for(int i = 0; i < 30; i++)
		for(int j = 0; j < 30; j++)
			combine[i][j] = -1;

	int c, d;
	cin >> c;
	for(int i = 0; i < c; i++) {
		string s;
		cin >> s;
		for(int j = 0; j < s.size(); j++) s[j] -= 'A';
		combine[s[0]][s[1]] = s[2];
		combine[s[1]][s[0]] = s[2];
	}
	cin >> d;
	for(int i = 0; i < d; i++) {
		string s;
		cin >> s;		
		for(int j = 0; j < s.size(); j++) s[j] -= 'A';
		opposed[s[0]].push_back(s[1]);
		opposed[s[1]].push_back(s[0]);
	}


	vector<int> r;

	int n;
	cin >> n;
	string s;
	cin >> s;

	for(int i = 0; i < s.size(); i++) {
		s[i] -= 'A';
		r.push_back(s[i]);
		if(r.size() < 2) continue;
		int y = combine[r.back()][r[r.size()-2]];
		if(y != -1) {
			r.pop_back();
			r.back() = y;
		}

		for(int i = 0; (!r.empty()) && i < opposed[r.back()].size(); i++) {
			for(int j = 0; j < r.size(); j++) {
				if(r[j] == opposed[r.back()][i]) {
					r.clear();
					break;
				}
			}
		}


	//	print(r);


	}

	for(int i = 0; i < 30; i++) opposed[i].clear();


	printf("Case #%d: ", caseNumber);
	print(r);



}

int main() {
	//freopen("in.txt", "r", stdin);
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; i++) solve(i);

}