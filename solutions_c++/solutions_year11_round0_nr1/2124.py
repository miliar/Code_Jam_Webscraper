#include <iostream>
#include <string>


using namespace std;


string s;


int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	scanf("%d", &t);
	for(int _ = 0; _ < t; _++)
	{
		int n;
		scanf("%d", &n);
		int o = 1;
		int b = 1;
		int lastO = 0;
		int lastB = 0;
		int cur = 0;
		for(int i = 0; i < n; i++)
		{
			int p;
			cin >> s >> p;
			if(s == "O")
			{
				cur = max(cur + 1, lastO + abs(o - p) + 1);
				lastO = cur;
				o = p;
			}
			else
			{
				cur = max(cur + 1, lastB + abs(b - p) + 1);
				lastB = cur;
				b = p;
			}
		}
		printf("Case #%d: %d\n", _ + 1, cur);
	}
}