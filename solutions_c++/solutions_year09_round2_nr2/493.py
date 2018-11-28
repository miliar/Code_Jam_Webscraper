#include <cstdio>
#include <cstdlib>
#include <vector>
#include <cmath>
#include <queue>
#include <cstring>
#include <string>
#include <algorithm>
#include <map>

using namespace std;


int main()
{
	int n;
	scanf("%d\n", &n);
	for(int i = 0; i < n; i++)
	{
		char buf[100];
		scanf("%s\n", buf);
		string s = buf;
		string ss = s;
		if(!next_permutation(s.begin(), s.end()))
		{
			s = ss + '0';
			sort(s.begin(), s.end());
			int j = 1;
			while(s[0] == '0')
				swap(s[0], s[j++]);
		}
		printf("Case #%d: %s\n", i+1, s.c_str());
	}
	return 0;
}
