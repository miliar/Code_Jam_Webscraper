#include <vector>
#include <iostream>
using namespace std;

int solve(vector<int> vals, vector<int> s, vector<int> p)
{
	if (vals.size() == 0) {
		if (s.size() == 0 || p.size() == 0)
			return -1;
		int sum1 = 0;
		int real = 0;
		for (int i = 0; i < s.size(); i++) {
			sum1 ^= s[i];
			real += s[i];
		}
		int sum2 = 0;
		for (int i = 0; i < p.size(); i++)
			sum2 ^= p[i];
		if (sum1 != sum2)
			return -1;
		else
			return real;
	}

	vector<int> newVals(vals);
	int n = newVals.back();
	newVals.pop_back();

	vector<int> newS(s);
	newS.push_back(n);
	int result1 = solve(newVals, newS, p);

	vector<int> newP(p);
	newP.push_back(n);
	int result2 = solve(newVals, s, newP);

	if (result1 == -1 && result2 == -1)
		return -1;
	return result1 > result2 ? result1 : result2;
}

int main()
{
	int c;

	cin >> c;
	for (int i = 0; i < c; i++) {
		int size;
		cin >> size;
		vector<int> vals;
		for (int j = 0; j < size; j++) {
			int n;
			cin >> n;
			vals.push_back(n);
		}
		int result = solve(vals, vector<int>(), vector<int>());
		cout << "Case #" << i+1 << ": ";
		if (result == -1)
			cout << "NO";
		else
			cout << result;
		cout << endl;
	}

	return 0;
}
