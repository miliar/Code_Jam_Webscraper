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

//FILE *fin=fopen("B-sample.in", "r");
//FILE *fout=fopen("B-sample.out", "w");

//FILE *fin=fopen("B-small-attempt0.in","r");
//FILE *fout=fopen("B-small-attempt0.out","w");

FILE *fin=fopen("B-large.in","r");
FILE *fout=fopen("B-large.out","w");

#define MAXN 10011

int n, s, p, t[101];
int b1;
int b2;

void init()
{
	fscanf(fin, "%d %d %d", &n, &s, &p);
	for (int i = 0; i < (int)n; i++)
		fscanf(fin, "%d", t + i);
	b1 = INF32;
	b2 = INF32;
	for (int s1 = 0; s1 <= 10; s1++)
		for (int s2 = s1; s2 <= 10; s2++)
			for (int s3 = s2; s3 <= 10; s3++)
				if (s1 + 2 < s3)
					continue;
				else if (s1 + 2 == s3 && s3 >= p)
					b1 = min(b1, s1 + s2 + s3);
				else if (s1 + 2 >  s3 && s3 >= p)
					b2 = min(b2, s1 + s2 + s3);
}

void search()
{
	int ret = 0;

	for (int i = 0; i < (int)n; i++)
		if (t[i] >= b2)
			ret++;
		else if (t[i] >= b1)
		{
			if (s > 0)
			{
				s--;
				ret++;
			}
		}
	fprintf(fout, "%d\n", ret);
}

int main()
{
	int testdata, i;

	fscanf(fin, "%d", &testdata);
	for (i = 0; i < testdata; i++)
	{
		fprintf(fout, "Case #%d: ", i+1);
		init();
		search();
	}
	return 0;
}
