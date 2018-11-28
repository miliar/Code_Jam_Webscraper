#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <queue>
using namespace std;

string getString(int x)
{
	string res = "";
	while(x)
	{
		char t = (x % 10) + '0';
		x /= 10;

		res = t + res;
	}
	return res;
}

int go(int A, int B)
{
	string strA = getString(A);

	int res = 0;
	for(int i = A; i <= B; i++)
	{
		string t = getString(i);
		string tt = t + t;
		string com = "";

		for(int j = 1; j < t.length(); j++)
		{
			string sub = tt.substr(j, t.length());
			if(sub[0] == '0')  continue;
			if(sub < t && sub >= strA) 
			{
				if(com == "")
				{
					com = sub;
					res++;
				}
				else 
				{
					if(com != sub)
					{
						res++;
					}
				}
				//cout << t << " " << 
			}
		}
	}
	return res;
}

int main()
{
	freopen("C:\\Users\\litstrong\\Desktop\\GCJ\\C-small-attempt0.in", "r", stdin);
	freopen("C:\\Users\\litstrong\\Desktop\\GCJ\\C-small-attempt0.out", "w", stdout);

	int T, c = 0;
	scanf("%d", &T);
	while(T--)
	{
		int A, B;
		scanf("%d%d", &A, &B);

		printf("Case #%d: ", ++c);

		int ans = go(A, B);

		printf("%d\n", ans);
	}
}