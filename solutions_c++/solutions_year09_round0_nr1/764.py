#include <cstdio>
#include <iostream>
#include <set>
#include <map>
#include <sstream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <utility>

using namespace std;

#define FOR(i,n) for((i) = 0; (i) < (n); ++(i))
#define SFOR(i,m,n) for((i) = (m); (i) < (n); ++(i))

int main(void)
{
	FILE *fi, *fo;	
	fi = fopen("d:\\a.in", "rt");
	fo = fopen("a.out", "w");
	
	int t,tt;
	int l,d,n,i,j,k;

	string A[5002];
	set<char> C[20];

	fscanf(fi, "%d%d%d\n", &l, &d, &n);

	char buf[1000];
	FOR(i, d)
	{
		fgets(buf, 1000, fi);
		A[i] = string(buf);
	}

	FOR(i, n)
	{
		fgets(buf, 1000, fi);
		string s = string(buf);
		k = 0;
		FOR(j, s.length())
		{
			C[k].clear();
			if (s[j] == '(')
			{
				++j;
				while (s[j] != ')')
				{
					C[k].insert(s[j]);
					++j;
				}
			}
			else
			{
				C[k].insert(s[j]);
			}
			++k;
		}
		int res = 0;
		FOR(j, d)
		{
			int fl = 1;
			FOR(k, l) if (C[k].find(A[j][k]) == C[k].end()) {fl = 0; break;}
			res += fl;
		}
		fprintf(fo, "Case #%d: %d\n", i+1, res);
	}
	

	fclose(fi);
	fclose(fo);

	return 0;
}