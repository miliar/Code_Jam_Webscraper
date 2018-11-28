#include <iostream>
#include <algorithm>
#include <utility>
#include <vector>
using namespace std;

typedef pair<int,int> PII;

int count_inv(const vector<int> &v)
{
	int ret = 0;
	int n = v.size();
	for(int i=0; i < n; i++)
		for(int j=i+1; j < n; j++)
			ret += (v[i] > v[j]);

	return ret;
}

void solve()
{
	int N; cin >> N;
	vector<PII> vec(N);
	for(int i=0; i < N; i++)
		cin >> vec[i].first >> vec[i].second;

	sort(vec.begin(), vec.end());
	vector<int> vsnd(N);
	for(int i=0; i < N; i++)
		vsnd[i] = vec[i].second;
	int ninv = count_inv(vsnd);
	cout << ninv << endl;
}

int main()
{
	int ncase; cin >> ncase;
	for(int icase=0; icase < ncase; icase++)
	{
		cout << "Case #" << (icase+1) << ": ";
		solve();
	}
}
