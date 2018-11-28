//consider using a set, or Python
#include <iostream>
#include <cstdio>
#include <cmath>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;

int T, A, B;
bool checked[2000001];

int recycle(int num)
{
	stringstream ss;
	ss << num;	
	string s = ss.str();
	int digits = s.size(), pwr = (int) pow(10.0, digits-1), rnum = num, recs = 0;
	checked[rnum] = 1;
	for (int i = 0; i < digits-1; i++) {
		int run = pwr*(rnum%10);
		rnum = run + rnum/10;
		stringstream ss2;
		ss2 << rnum;
		if (ss2.str().size() == digits && rnum <= B && rnum >= A && !checked[rnum]) {
			checked[rnum] = 1;
			recs++;
		}
	}
	return recs*(recs+1)/2;
}

int main()
{
	freopen("rnum.out", "w", stdout);
	freopen("rnum.in", "r", stdin);
	
	cin >> T;
	for (int i = 1; i <= T; i++) {
		cin >> A >> B;
		cout << "Case #" << i << ": ";
		int ans = 0;
		for (int j = A; j <= B; j++) 
			ans += recycle(j);
		cout << ans << endl;	
		fill(checked, checked+2000001, 0);
	}
}
