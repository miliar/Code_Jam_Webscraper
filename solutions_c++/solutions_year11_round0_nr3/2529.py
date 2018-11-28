#include<iostream>
#include<algorithm>
#include<map>
#include<vector>
#include<set>
#include<cstdio>
#include<string>
#include<list>
using namespace std;



int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("out", "w", stdout);
	
	int t;
	cin >> t;
	for(int cs = 1; cs <= t; cs++)
	{
		int n;
		cin >> n;
		vector<int> v(n);
		for(int i = 0; i < n; i++)
			scanf("%d", &v[i]);

		int xor = 0;
		for(int i = 0; i < n; i++)
			xor ^= v[i];
		if(xor)
		{
			cout << "Case #" << cs << ": " << "NO" << endl;
			continue;
		}

		int all = 0;
		for(int i = 0; i < n; i++)
			all += v[i];


		int mini = v[0];
		for(int i = 0; i < n; i++)
			mini = min(mini, v[i]);


		cout << "Case #" << cs << ": " << all-mini << endl;
	}





	return 0;
}