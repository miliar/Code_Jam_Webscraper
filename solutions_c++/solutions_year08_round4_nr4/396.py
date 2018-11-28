#include <iostream>
#include <iomanip>
#include <sstream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>

#define MAX 1024

using namespace std;
FILE *in; FILE *out;

int n, k;
char a[MAX], b[MAX];
vector <int> perm;

void createString()
{
	int i;
	int pos = 0;

	while (pos < n)
	{
		for (i=0; i<k; i++) b[pos+i] = a[pos+perm[i]];
		pos += k;
	}
	
	return;
}

int getLength()
{
	int i, ans = 0;
	char last = 0;
	
	for (i=0; i<n; i++)
	{
		if (last != b[i])
		{
			ans++;
			last = b[i];
		}
	}
	
	return ans;
}

void doWork(int testNum)
{
	int i;
	int tmp, ans = MAX;
	
	fscanf(in, "%d %s", &k, a);
	n = (int)strlen(a);
	
	perm.clear();
	for (i=0; i<k; i++) perm.push_back(i);
	
	do
	{
		createString();
		tmp = getLength();
		ans = min(ans, tmp);
		
	} while (next_permutation(perm.begin(), perm.end()));
	
	fprintf(out, "%d\n", ans);	
	return;
}

int main(void)
{
	int tests, i;
	
	in = fopen("permRLE.in", "rt");
	out = fopen("permRLE.out", "wt");
	
	fscanf(in, "%d", &tests);
	for (i=0; i<tests; i++)
	{
		fprintf(out, "Case #%d: ", i+1);
		doWork(i + 1);
	}
	
	return 0;
}
