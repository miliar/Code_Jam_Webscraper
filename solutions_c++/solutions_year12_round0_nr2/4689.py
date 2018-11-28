#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int process()
{
	int n, s, p;
	cin >> n >> s >> p;
	vector<int> t(n);
	for(int i = 0; i < n; i++)
		cin >> t[i];
	sort(t.begin(), t.end(), greater<int>());
	int cnt = 0;
	for(int i = 0; i < n; i++)
	{
		if(t[i] >= p*3-2)
		{
			cnt++;
			continue;
		}
		if(p*3 - t[i] <= 4 && s && t[i] >= 2)
		{
			s--;
			cnt++;
		}
	}
	return cnt;
}

int main()
{
	int t;
	cin >> t;
	for(int i = 0; i < t; i++)
		cout << "Case #" << i+1 << ": " << process() << endl;
}
