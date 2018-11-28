#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>

using namespace std;


int main(int argc, char * argv[])
{
	/*if (argc != 3)
	{
		printf("Usage:command.exe infile outfile\n");
		exit(1);
	}*/
	FILE* in = fopen("in.in", "r");
	if (!in)
	{
		printf("cannot open infile\n");
		exit(1);
	}
	FILE* out = fopen("out.out", "w");
	if (!out)
	{
		printf("cannot open outfile\n");
		exit(1);
	}
	char buf[512];
	fgets(buf, 512, in);
	int cas = 0;
	while (fgets(buf, 512, in))
	{
		char* toke = strtok(buf, " \n");
		int l = atoi(toke);
		toke = strtok(NULL, " \n");
		int p = atoi(toke);
		toke = strtok(NULL, " \n");
		int c = atoi(toke);
		int t = -1;
		unsigned long long multi = l;
		while (true)
		{
			t++;
			double k = pow(double(c), pow(double(2),t));
			if (multi*k >= p)
			{
				break;
			}
		}
		cout << t << endl;
		fprintf(out, "Case #%d: %d\n", ++cas, t);
	}
	return 0;
}

