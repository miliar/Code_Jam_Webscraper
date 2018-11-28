#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int recurse(int P, vector<int> rel){
	bool b[101];
	memset(b, true, 100);
	int ret = 0;
	for (int r = 0; r < rel.size(); r++){
		b[rel[r]] = false;
		int g1 = 0, g2 = 0;
		for (int x = rel[r]-1; x >= 1; x--){
			if (b[x] == false) break;
			g1++;
		}
		for (int x = rel[r]+1; x <= P; x++){
			if (b[x] == false) break;
			g2++;
		}
		ret += g1+g2;
	}
	return ret;
}

int main(){
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int N;
	cin >> N;
	for (int r = 0; r < N; r++){
		int P, R;
		vector<int> rel;
		cin >> P >> R;
		for (int p = 0; p < R; p++){
			int tmp;
			cin >> tmp;
			rel.push_back(tmp);
		}
		sort(rel.begin(), rel.end());
		vector<int> res;
		res.push_back(recurse(P, rel));
		while(next_permutation(rel.begin(), rel.end())) res.push_back(recurse(P, rel));
		int size = res[0];
		for (int m = 0; m < res.size(); m++) if (size > res[m]) size = res[m];
		cout << "Case #" << r+1 << ": " << size << endl;
	}
	return 0;
}