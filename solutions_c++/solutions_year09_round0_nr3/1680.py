#include <iostream>
#include <vector>
#include <string>
using namespace std;
string s = "welcome to code jam";
int ans[30];
int main ()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int n;
	int kkk = 1;
	cin >> n;
	getchar();
	while (n--)
	{
		char a[505];
		gets(a);
		memset (ans, 0, sizeof (ans));
		int len = strlen(a);
		int len2 = s.size();
		for (int i = 0; i < len; i++)
		{
			if (a[i] == 'w')ans[0]++;
			for (int j = 1; j < len2; j++)
			{
				if (a[i] != s[j] && ans[j] == 0)
					break;
				if (a[i] == s[j])ans[j] += ans[j-1];
			}
		}
	//	for (int i = 0; i < len2; i++)
		printf("Case #%d: %04d\n", kkk++, ans[len2-1]);
	}
}