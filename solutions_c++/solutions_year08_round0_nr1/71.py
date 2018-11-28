#include <algorithm>
#include <iostream>
#include <map>
#include <string>
#include <vector>

using namespace std;

#define MAX_N 20
#define MAX_S 100
#define MAX_Q 1000
#define MAX_LEN 100

int solve(void)
{
	int s;
	cin >> s;
	cin.get(); // skip newline

	map<string,int> lookup;
	for(int i=0;i<s;i++)
	{
		string temp;
		getline(cin,temp);
		lookup[temp]=i;
	}

	vector<int> dp(s);

	int q;
	cin >> q;
	cin.get();

	for(int i=0;i<q;i++)
	{
		string temp;
		getline(cin,temp);

		if(lookup.count(temp) == 0)
			continue;

		int j=lookup[temp];

		int m=INT_MAX;
		for(int k=0;k<s;k++)
			if(k!=j)
				m=min(m,dp[k]);

		dp[j]=m+1;
	}

	return *min_element(dp.begin(),dp.end());
}

int main(void)
{
	int n;

	cin >> n;

	for(int i=0;i<n;i++)
		cout << "Case #" << i+1 << ": " << solve() << endl;

	return 0;
}
