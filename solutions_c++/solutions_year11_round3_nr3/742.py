# include <iostream>
# include <string>
# include <fstream>
# include <vector>
using namespace std;

int main()
{
	ifstream cin("CC.in");
	ofstream cout("CC.out");
	int t = 0;
	cin >> t;
	int casenum = 0;
	while(t - casenum)
	{
		int n;
		long long l, h;
		cin >> n >> l >> h;
		vector<int> freqs(n);

		for(int i = 0; i < n; ++i)
			cin >> freqs[i];

		long long ans = -1;
		for(long long i = l; i <= h; ++i)
		{
			int j = 0;
			for(; j < n; ++j)
				if(freqs[j] % i && i % freqs[j])
					break;
			if(j == n)
			{
				ans = i;
				break;
			}
		}
		casenum++;
		cout << "Case #" << casenum << ": ";
		if(ans == -1)
			cout << "NO" << endl;
		else
			cout << ans << endl;
	}
	return 0;
}
