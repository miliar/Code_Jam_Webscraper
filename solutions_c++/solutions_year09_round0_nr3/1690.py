#include<iostream>
#include<string>
using namespace std;
int main()
{
	freopen("next.txt", "r", stdin);
	freopen("test.txt", "w", stdout);
	int test;
	cin>>test;
	char w[1024];
	gets(w);
	char a[30] = "welcome to code jam";
	int n = strlen(a);
	for(int t = 0;t<test;t++)
	{
		int ans[30] = {0};
		gets(w);
		int s = strlen(w);
		for(int i = s-1;i>=0;i--)
		{
			for(int j = 0;j<n;j++)
				if(w[i] == a[j])
				{
					if(j == n-1)
						ans[j]++;
					else
						ans[j] = (ans[j] + ans[j+1])%1000;
				}
		}
		printf("Case #%d: %04d\n",t+1, ans[0]);
	}
	return 0;
}
