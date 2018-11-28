#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<string>
#include<cstring>
#include<cmath>
#include<vector>
#include<map>
#include<queue>
#include<stack>
#include<sstream>
#include<algorithm>
#include<complex>
#include<set>
using namespace std;
#define MP make_pair
#define F first
#define S second
#define PB push_back
int f[31][2];
void init() {
	memset(f, 0, sizeof(f));
	for(int score1 = 0; score1 <= 10; score1 ++)
		for(int score2 = 0; score2 <= 10; score2 ++)
			for(int score3 = 0; score3 <= 10; score3 ++) {
				bool Dif3 = false;
				bool Dif2 = false;
				int Max = score1;
				Max = max(Max, score2);
				Max = max(Max, score3);
				if (abs(score2 - score1) > 2 || abs(score3 - score2) > 2 || abs(score1 - score3) > 2) Dif3 = true;
				if (abs(score2 - score1) > 1 || abs(score3 - score2) > 1 || abs(score1 - score3) > 1) Dif2 = true;
				if (Dif3) continue;
				if (!Dif2) f[score1 + score2 + score3][0] >?= max(Max, f[score1 + score2 + score3][0]);				
				f[score1 + score2 + score3][1] = max(Max, f[score1 + score2 + score3][1]);
//				cout << Max << endl;
			}
}
int n, s, p;
void process(int test) {
	scanf("%d%d%d", &n, &s, &p);
	int CountNonSur = 0;
	int CountSur = 0;
	for(int i = 0; i < n; i ++) {
		int score;
		scanf("%d", &score);
		if (f[score][0] >= p) CountNonSur ++;
		else if (f[score][1] >= p) CountSur ++;
	}
//	cout << CountNonSur << " " << CountSur << endl;
	printf("Case #%d: %d\n", test, CountNonSur + min(s, CountSur));
}
int main() {
	freopen("B.inp", "r", stdin);
	freopen("B.out", "w", stdout);
	init();
//	cout << f[8][1] << endl;
	int t;
	scanf("%d", &t);
	for(int test = 0; test < t; test ++) process(test + 1);
	return 0;
}
