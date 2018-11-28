#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;


int N, k;
string S, S1;
vector<int> perm, firstperm;


int test() {
	S1 = "";
	for (int i=0; i<(int)S.length(); i+=k) {
		for (int j=1; j<=k; ++j) S1 += S[i + perm[j] - 1];
	}
	int size = 0;
	for (int i=1; i<(int)S1.length(); ++i) {
		if (S1[i] != S1[i-1]) ++size;
	}
	return size + 1;
}


int main()
{
	cin >> N;
	for (int testCase=1; testCase<=N; ++testCase) {
		cin >> k >> skipws;
		getline(cin, S);
		getline(cin, S);
		perm.assign(k+1, 0);
		for (int i=1; i<=k; ++i) perm[i] = i;
		firstperm = perm;
		int minSize = -1;
		while (1) {
			int size = test();
			if (minSize == -1 || (size < minSize)) minSize = size;

			vector<int>::iterator vit = perm.begin();
			next_permutation(++vit, perm.end());
			if (perm == firstperm) break;
		}
		cout << "Case #" << testCase << ": " << minSize << endl;
	}
}
