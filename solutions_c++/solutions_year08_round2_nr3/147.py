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

#define MAX 1000100

using namespace std;
FILE *in; FILE *out;

int k, n;
int a[MAX], b[MAX];


void doWork(int testNum)
{
	int i, c;
	int pos = 0, skip = 0;
	
	cout << "Test: " << testNum << endl;
	fscanf(in, "%d %d", &k, &n);
	for (i=0; i<n; i++) fscanf(in, "%d", &b[i]);
	
	memset(a, 0, sizeof(a));
	for (i=0; i<k; i++)
	{
		int curSkip = skip;
		while (a[pos%k] != 0) pos++;
		
		int cnt = 0;
		for (c=0; c<k; c++) cnt += (int)(a[(pos+c)%k] == 0);
		curSkip %= cnt;
		
		for (c=0; c<curSkip; c++)
		{
			pos++;
			while (a[pos%k] != 0) pos++;
		}
		a[pos%k] = i + 1;
		skip++;
	}
	
	for (i=0; i<n; i++) fprintf(out, " %d", a[b[i]-1]);
	fprintf(out, "\n");	
	return;
}

int main(void)
{
	int tests, i;
	
	in = fopen("mousetrap.in", "rt");
	out = fopen("mousetrap.out", "wt");
	
	fscanf(in, "%d", &tests);
	for (i=0; i<tests; i++)
	{
		fprintf(out, "Case #%d:", i+1);
		doWork(i + 1);
	}
	
	return 0;
}
