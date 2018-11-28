#include <iostream>
#include <algorithm>
#include <string>
#include <sstream>
#include <set>

using namespace std;

// Google Code Jame 2012 Qualification Round

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int t=1; t<=T; t++)
	{
		int A, B, cnt=0;

		set < pair<string,string> > recycled_pairs;

		scanf("%d %d", &A, &B);
		for(int n=A; n<=B; n++)
		{
			string a, b, c;
			stringstream ss;
			ss << A << " " << B << " " << n;
			ss >> a >> b >> c;
			for(int j=1; j<c.length(); j++)
			{
				string m = c.substr(j)+c.substr(0, j);
				cnt+=m>c && m<=b;
				if(m>c && m<=b)
					recycled_pairs.insert(make_pair(c, m));
			}
		}
		printf("Case #%d: %d\n", t, recycled_pairs.size());
	}
	return 0;
}