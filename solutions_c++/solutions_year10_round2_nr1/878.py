#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <algorithm>
#include <cmath>

using namespace std;

set<string> dirs;

int mkdir(const char *path, int len)
{
	if (len == 0) return 0;

	int num = 0;
	int i = len-1;
	for (; i > 0; --i) {
		if (path[i] == '/') {
			num += mkdir(path, i);
			break;
		}
	}

	bool b = dirs.insert(string(path, path+len)).second;
	if (b) num++;
	return num;
}

int main()
{
	int T;
	cin>>T;
	for (int i = 0;i<T;i++)
	{
		int N, M;
		cin>>N>>M;

		dirs.clear();
		for(int j=0;j<N;j++) {
			char buf[128];
			scanf("%s", buf);
			char *p = buf;
			if (p[0] == '/') ++p;
			dirs.insert(p);
		}

		int num = 0;
		for(int j=0;j<M;j++) {
			char buf[128];
			scanf("%s", buf);
			char *p = buf;
			if (p[0] == '/') ++p;
			int len = strlen(p);
			if (p[len-1] == '/') --len;
			num += mkdir(p, len);
		}

		printf("Case #%d: %d\n", i+1, num);
	}

	return 0;
}
