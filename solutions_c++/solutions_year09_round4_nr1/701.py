#define _CRT_SECURE_NO_DEPRECATE

#include <iostream>
#include <algorithm>
#include <cassert>
#include <string>
#include <map>
#include <set>

using namespace std;

int main()
{
	int test_cnt;
	scanf("%d", &test_cnt);
	for (int test_id = 1; test_id <= test_cnt; ++test_id)
	{
		int n;
		cin >> n;
        int * x = new int[n];
        string s;
        for (int i = 0; i < n; ++i)
        {
        	cin >> s;
            x[i] = n;
            for (int j = (int)s.length() - 1; j >= 0; --j, --x[i])
            	if (s[j] == '1') break;
        }
        int r = 0;
        for (int i = 0; i < n; ++i)
        {
        	int j;
        	for (j = i; j < n; ++j)
        		if (x[j] <= i + 1) break;
        	assert(j < n);
            while (i < j) swap(x[j], x[j - 1]), j--, r++;
        }

        cout << "Case #" << test_id << ": " << r << endl;
    }

	return 0;
}
