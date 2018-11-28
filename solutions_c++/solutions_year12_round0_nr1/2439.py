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

const int64 INF64=(_1<<63)-1;
const int INF32=(_1<<31)-1;

using namespace std;

//FILE *fin=fopen("A-sample.in","r");
//FILE *fout=fopen("A-sample.out","w");

FILE *fin=fopen("A-small-attempt3.in","r");
FILE *fout=fopen("A-small-attempt3.out","w");

//FILE *fin=fopen("A-large.in","r");
//FILE *fout=fopen("A-large.out","w");

#define MAXN 10011

char dict[26];
string s1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
string s2 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
string s3 = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
string d1 = "our language is impossible to understand";
string d2 = "there are twenty six factorial possibilities";
string d3 = "so it is okay if you want to just give up";

void getDict(string ss, string dd)
{
	for (int i = 0; i < (int)ss.length(); i++)
		if (ss[i] != ' ')
			dict[ss[i] - 'a'] = dd[i];
}

void search()
{
	char inp[1000];
	fgets(inp, 1000, fin);
	for (int i = 0; i < (int)strlen(inp); i++)
		if (inp[i] == '\n')
			break;
		else if (inp[i] == ' ')
			fprintf(fout, " ");
		else
			fprintf(fout, "%c", dict[inp[i] - 'a']);
	fprintf(fout, "\n");
}

int main()
{
	int testdata ,i;

	for (i = 0; i < 26; i++)
		dict[i] = -1;
	getDict(s1, d1);
	getDict(s2, d2);
	getDict(s3, d3);

	dict[16] = 'z';
	dict[25] = 'q';

	fscanf(fin,"%d\n",&testdata);
	for (i = 0; i < testdata; i++)
	{
		fprintf(fout, "Case #%d: ", i+1);
		search();
	}
	return 0;
}
