#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cmath>
#include <set>
#include <map>

const long double eps = 1e-9;

using namespace std;



int T, na, nb;
vector <pair <int, int> > A;
vector <pair <int, int> > B;



int GetTime()
{
	char c;
	c = getchar();
	while (c < '0' || c > '9') c = getchar();
	int res = 0, t = 0;
	while (c >= '0' && c <= '9') {
		t = t * 10 + c - '0';
		c = getchar();
	}
	res = t * 60;
	t = 0;
	c = getchar();
	while (c < '0' || c > '9') c = getchar();
	while (c >= '0' && c <= '9') {
		t = t * 10 + c - '0';
		c = getchar();
	}
	res += t;
	return res;
}

void Load()
{
	cin >> T;
	cin >> na >> nb;
	A.clear();
	B.clear();
	int i, j, k;
	for (i = 1; i <= na; i++) {
		j = GetTime();
		k = GetTime();
		A.push_back(make_pair(j, 1));
		B.push_back(make_pair(k + T, -1));
	}
	for (i = 1; i <= nb; i++) {
		j = GetTime();
		k = GetTime();
		A.push_back(make_pair(k + T, -1));
		B.push_back(make_pair(j, 1));
	}

}


void Solve()
{
	int i, j, resa, resb;
	resa = resb = 0;
	std::sort(A.begin(), A.end());
	std::sort(B.begin(), B.end());
	j = 0;
	for (i = 0; i < A.size(); i++) {
		if (A[i].second == -1) j++;
		else {
			if (j > 0) j--;
			else resa++;
		}
	}
	j = 0;
	for (i = 0; i < B.size(); i++) {
		if (B[i].second == -1) j++;
		else {
			if (j > 0) j--;
			else resb++;
		}
	}
	cout << resa << " " << resb << "\n";	
}

void Save()
{
}

int main(){
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int nt, tt;
	cin >> nt;
	for (tt = 1; tt <= nt; tt++) {
		printf("Case #%d: ", tt);
		Load();
		Solve();
		Save();
	}
	return 0;
}