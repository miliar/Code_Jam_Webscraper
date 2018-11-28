#include <iostream>
#include <cmath>
#include <vector>
#include <set>

using namespace std;

vector<long long int> mas;
int m;
set<int> temp;


long long int f(long long sumC, long long int sum, long long int rsum, int j) {
	long long int maxx = 0;
	//int j;
	//set<int> copy;
	/*
	for (j = 0; j < m; j++) {
		if (was.find(j) == was.end())
			if (sum ^ mas[j] == sumC ^ mas[j]) 
				maxx = max(maxx, rsum - mas[j]);
	}
	*/
	if (j > 0)//if (fl && sum == sumC)
		maxx = rsum;

	if (j < (m - 1)) {
		maxx = max(maxx, f(sumC ^ mas[j], sum ^ mas[j], rsum - mas[j], j + 1));
	}
    if (j < (m))
	maxx = max(maxx, f(sumC, sum, rsum, j + 1));

		/*
	for (j = 0; j < m; j++) {
		if (was.find(j) == was.end()) {
			//copy = was;
			//copy.insert(j);
			was.insert(j);
			maxx = max(maxx, f(sumC ^ mas[j], sum ^ mas[j], rsum - mas[j], was, true));
			was.erase(was.find(j));
		}
	}
	*/
	return maxx;
}

void main() {
	
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int n, j;
	long long int x, sum, rsum, maximum, minn;
	
	cin >> n;
	for (int i = 0; i < n; i++) {
		sum = 0;
		rsum = 0;
		mas.clear();
		minn = INT_MAX;

		cin >> m;
		for (j = 0; j < m; j++) {
			cin >> x;
			mas.push_back(x);
			sum ^= x;
			rsum += x;
			minn = min(minn, x);
		}

		cout << "Case #" << (i + 1) << ": ";
		if (sum) cout << "NO";
		else cout << (rsum - minn);
		cout << endl;
	}
}
