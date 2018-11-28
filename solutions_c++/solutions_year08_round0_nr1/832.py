#include <iostream>
#include <map>

using namespace std;

int main()
{
	int n, t, q, i, j, flag[101], test, ans, num, idx;
	string s;
	map<string, int> m;
	scanf("%d", &t);
	for(test=1; test<=t; test++)
	{
		scanf("%d\n", &n);
		m.clear();
		for(i=0; i<n; i++)
		{
			getline(cin, s);
			m.insert(make_pair(s, i));
			flag[i]=0;
		}
		ans=num=0;
		scanf("%d\n", &q);
		for(i=0; i<q; i++)
		{
			getline(cin, s);
			idx=m[s];
			if(!flag[idx])
			{
				flag[idx]=1;
				num++;
				if(num==n)
				{
					ans++;
					num=1;
					for(j=0; j<n; j++)
						flag[j]=0;
					flag[idx]=1;
				}
			}
		}
		printf("Case #%d: %d\n", test, ans);
	}
}
