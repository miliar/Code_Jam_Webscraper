#define _CRT_SECURE_NO_DEPRECATE
#include<iostream>
#include<string>
#include<sstream>
#include<vector>
#include<deque>
#include<queue>
#include<stack>
#include<numeric>
#include<math.h>
#include<set>
#include<map>
#include<fstream>
#define epsilon 0.000000001
#define cosinusa(a, b, c) ((a * a + b * b - c * c) / (2.0 * a * b));
#define infi 1000000000
using namespace std;

struct elem
{
	int l;
	int p;
	bool operator < (const elem& rhs) const
	{
		return l * rhs.p < p * rhs.l; 
	}
};

int main()
{
	freopen("google.in", "r", stdin);
	freopen("google.out", "w", stdout);
	int numTests;
	cin >> numTests;
	for(int testCounter = 0; testCounter < numTests; ++testCounter)
	{
		printf("Case #%d:", testCounter + 1);
		int n;
		cin >> n;
		vector<pair<elem, int> > elements(n);
		for (int i = 0; i < n; i++)
		{
			cin >> elements[i].first.l;
		}
		for (int i = 0; i < n; i++)
		{
			cin >> elements[i].first.p;
			elements[i].second = i;
			
		}
		sort(elements.begin(), elements.end());
		for (int i = 0; i < n; i++)
		{
			cout << " " << elements[i].second;
		}
		cout << endl;
	}
	return 0;
}
