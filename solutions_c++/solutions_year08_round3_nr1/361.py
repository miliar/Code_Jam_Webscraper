#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <list>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <complex>
#include <cstdio>
#include <cassert>
#include <cmath>

using namespace std;
typedef long long ll;


struct aaa
{
	int start;
        bool operator<(const aaa& o) const
        {
                return start<o.start;
        }
};

int freq_letters[10000];

int main()
{
	int numCase;
	int max_letters, keys, letters;
	cin >> numCase;
	int i, j, n;
	long long c;
	for (i = 0; i < numCase; i++)
	{
		long long ans = 0;
		long long tries = 1;
		long long keys = 1;
		cin >> max_letters >>  keys >>  letters;

		for(j=0;j<letters;j++) {
			cin >> freq_letters[j];
		}	
		sort(freq_letters, &freq_letters[letters]);
	
		tries = 1;
		for (j = 0; j <letters ; j++) {
			tries = j/keys+ 1;
			ans += freq_letters[letters-j-1]*tries;
//cout << freq_letters[letters-j-1] << " " << tries << endl;
		}
		cout << "Case #" << (i+1) << ": " << ans << endl;
	}
	return 0;
}
