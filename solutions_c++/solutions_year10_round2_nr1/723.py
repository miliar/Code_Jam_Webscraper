#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cstdlib>
#include <cstdio>
#include <cstring>
using namespace std;
int main()
{
	FILE *in = fopen("A-large.in", "r");
	FILE *out = fopen("out.txt", "w");
	int ts, tc, N, M, res;
	int i, j, k, len;
	char s[111];
	set <string> ds[111];
	string temp, parent;
	fscanf(in, "%d", &ts); fgetc(in);
	for (tc = 1; tc <= ts; ++tc)
	{
		res = 0;
		for (i = 0; i < 111; ++i)
			ds[i].clear();
		fscanf(in, "%d %d", &N, &M);
		for (i = 0; i < N; ++i)
		{
			parent = string("root:");
			fscanf(in, "%s", s);
			len = strlen(s);
			for (j = 1, k = 0; j < len; ++j, ++k)
			{
				for (temp = ""; j < len && s[j] != '/'; ++j)
					temp += s[j];
				ds[k].insert(parent + temp);
				parent += temp + ":";
				if (j >= len) break;
			}
		}
		for (i = 0; i < M; ++i)
		{
			parent = string("root:");
			fscanf(in, "%s", s);
			len = strlen(s);
			for (j = 1, k = 0; j < len; ++j, ++k)
			{
				for (temp = ""; j < len && s[j] != '/'; ++j)
					temp += s[j];
				if (ds[k].find(parent + temp) == ds[k].end())
				{
					printf("%s\n", (parent + temp).c_str());
					ds[k].insert(parent + temp);
					++res;
				}
				parent += temp + ":";
				if (j >= len) break;
			}
		}
		fprintf(out, "Case #%d: %d\n", tc, res);
	}
	fclose(in);
	fclose(out);
	return 0;
}
