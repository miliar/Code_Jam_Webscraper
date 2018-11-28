#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <set>
#include <queue>
#include <vector>

using namespace std;

int main(void)
{
	FILE *in, *out;
	in = fopen("A.in", "r");
	out = fopen("A.out", "w");

	char str[100];
	int tc, t;
	int n, q;
	int i, j;
	int cnt, ans;
	string eg;
	bool chk[1000];
	
	fscanf(in, "%d", &tc);

	for(t=1; t<=tc; t++)
	{
		vector<string> se;
		memset(chk, false, sizeof(chk));
		fscanf(in, "%d", &n);
		
		fgets(str, 100, in);
		for(i=0; i<n; i++)
		{
			fgets(str, 100, in);
			eg = str;
			se.push_back(eg);
		}
		cnt = 0;
		ans = 0;
		fscanf(in, "%d", &q);

		fgets(str, 100, in);
		bool flag = false;
		for(i=0; i<q; i++)
		{
			if(!flag) fgets(str, 100, in);
			eg = str;
			for(j=0; j<n; j++)
			{
				string tmp = se[j];
				if(!chk[j] && tmp == eg)
				{
					chk[j] = true;
					cnt++;
					break;
				}
			}
			if(cnt == n) 
			{
				memset(chk, false, sizeof(chk));
				cnt = 0;
				ans++;
				i--;
				flag = true;
			}
			else flag = false;

		}
		
		fprintf(out, "Case #%d: %d\n", t, ans);
	}
	return 0;
}