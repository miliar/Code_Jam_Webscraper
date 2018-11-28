#include <iostream>
//#include <set>
#include <algorithm>
#include <cstdio>
#include <string>
#include <vector>

using namespace std;

int main()
{
	string line;
	getline(cin, line);
	int num = atoi(line.c_str());
	int cases = 0;
	int num_req = 0;
	
	while(cases < num)
	{
		num_req = 0;
		int P, K, L;
//		cout << "Current input string is " << line << endl;
		scanf_s("%d %d %d", &P, &K, &L);
//		cout << P << "\t" << K << "\t" << L << endl;
		vector<int> freq(L);
		for(int j=0; j < L ; ++j)
		{
			scanf_s("%d", &freq[j]);
//			cout << "freq[" << j << "] = " << freq[j] << endl;
		}

		sort(freq.begin(), freq.end());
		reverse(freq.begin(), freq.end());
		int i = 0, j = 1;
		while(i < L)
		{
			num_req += j * freq[i];
			++i;
			if((i % K) == 0) ++j;
		}

		++cases;
		cout << "Case #" << cases << ": " << num_req << endl;
	}

	return 0;
}