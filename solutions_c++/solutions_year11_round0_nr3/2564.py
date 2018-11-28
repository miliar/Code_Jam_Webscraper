#include <iostream>
#include <vector>
#include <algorithm>
#include <stdlib.h>
#include <math.h>
#include <stdio.h>

using namespace std;

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C.out","w",stdout);
	int T;
	cin>>T;
	for(int test = 1; test <= T; ++test)
	{
		int n;
		cin >> n;
		unsigned long long sum = 0;
		int c = 0;
		int min = 1000001;
		int res = 0;
		for (int i = 0; i < n; ++i)
		{
			cin >> c;
			if (c < min) min = c;
			res ^= c;
			sum += c;
		}

		cout << "Case #"<<test<<": ";
		if (res == 0)
			cout <<sum - min;
		else cout <<"NO";
		cout<<endl;
	}
	fclose(stdout);
	return 0;
}