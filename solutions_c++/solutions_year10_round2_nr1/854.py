#include <iostream>
#include <string>
#include <algorithm>
#include <set>

using namespace std;

int main()
{
	freopen("data.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int t=1; t<=T; t++)
	{
		int N, M;
		scanf("%d%d", &N, &M);
		set <string> dir;
		for(int i=0; i<N; i++)
		{
			string s, a="";
			cin >> s;
			for(int j=0; j<s.length(); j++)
			{
				if(s[j]=='/' && a!="")
					dir.insert(a);
				a+=s[j];
			}
			dir.insert(a);
		}
		int cur=dir.size();

		for(int i=0; i<M; i++)
		{
			string s, a="";
			cin >> s;
			for(int j=0; j<s.length(); j++)
			{
				if(s[j]=='/' && a!="")
					dir.insert(a);
				a+=s[j];
			}
			dir.insert(a);
		}
		int final=dir.size();

		printf("Case #%d: %d\n", t, final-cur);
	}
	return 0;
}