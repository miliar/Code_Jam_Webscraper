#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include<time.h>
#include<iostream>
#include<string>
#include<sstream>
#include<vector>
#include<queue>
#include<set>
#include<map>
#include<algorithm>
#define MIN(a,b) ((a)>(b)?(b):(a))
#define MAX(a,b) ((a)<(b)?(b):(a))
#define INF INF32
#define NA (-1)

#define uint64 unsigned __int64
#define _1 ((uint64)1)
#define int64 __int64

const int64 INF64 = (_1<<63) - 1;
const int INF32 = (_1<<31) - 1;

using namespace std;

//FILE *fin=fopen("C-sample.in", "r");
//FILE *fout=fopen("C-sample.out", "w");

//FILE *fin=fopen("C-small-attempt0.in","r");
//FILE *fout=fopen("C-small-attempt0.out","w");

FILE *fin=fopen("C-large.in","r");
FILE *fout=fopen("C-large.out","w");

#define MAXN 10011

int A, B;
int ret;

void init()
{
	fscanf(fin, "%d %d", &A, &B);
}

void gen(int n)
{
	set<int> f;
	int bmax = 1;
	while (n / bmax)
		bmax *= 10;
	for (int b = 10; b < bmax; b *= 10)
	{
		int l = n / b;
		int r = n % b;
		int m = l + r * (bmax / b);
		if (m > n && m <= B)
			f.insert(m);
	}
	ret += (int)f.size();
}

void search()
{
	ret = 0;
	for (int n = A; n < B; n++)
		gen(n);
	fprintf(fout, "%d\n", ret);

}

int main()
{
	int testdata, i;

	fscanf(fin, "%d", &testdata);
	for (i = 0; i < testdata; i++)
	{
		printf("%d\n", i);
		fprintf(fout, "Case #%d: ", i+1);
		init();
		search();
	}
	return 0;
}
