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
		string s;
		cin >> s;
		map < char, int > u;
        u[s[0]] = 1;
        int cur = 0;
        for (int i = 1; i < (int)s.length(); ++i)
        	if (u.count(s[i]) == 0)
        	{
        		u[s[i]] = cur++;
                if (cur == 1) cur++;
        	}
        int base = max(cur, 2);
        long long r = 0;
        for (int i = 0; i < (int)s.length(); ++i)
        	r = r * base + u[s[i]];
        cout << "Case #" << test_id << ": " << r << endl;
    }

	return 0;
}
