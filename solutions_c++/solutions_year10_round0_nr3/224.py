// Using libUtil from libGlov (Game Library of Victory) available at http://bigscreensmallgames.com/libGlov
#include "utilUtils.h"
#include "utilFile.h"
#include "utilString.h"
#include "assert.h"
#include "utilArray.h"
#include <string.h>
#include <stdio.h>
#include <stdarg.h>
#include <conio.h>
#include "utilRand.h"
#include <vector>
#include <set>
#include <map>
using namespace std;

char *doC(char **&toks)
{
	U64 R = atoi(*toks++);
	U64 k = atoi(*toks++);
	U64 N = atoi(*toks++);
	U64 g[1001];
	for (U64 i=0; i<N; i++)
	{
		g[i] = atoi(*toks++);
	}

	U64 income=0;
	U64 run=0;
	U64 head = 0;
	map<U64, pair<U64, U64>> heads;
	// first run-through until it loops
	do {
		U64 orig_head=head;
		bool bFirst=true;
		heads[head] = pair<U64,U64>(run, income);
		for (U64 room = k; g[head%N] <= room && (bFirst || ((head % N) != orig_head)); head++)
		{
			income += g[head%N];
			room -= g[head%N];
			bFirst = false;
		}
		head = head % N;
		run++;
	} while (heads.find(head) == heads.end() && run<R);
	pair<U64,U64> head_values = heads[head];
	U64 head_runs = head_values.first;
	U64 head_income = head_values.second;
	U64 num_runs_per_loop = run - head_runs;
	assert(num_runs_per_loop > 0);
	U64 income_per_loop = income - head_income;
	U64 loops = (R - run) / num_runs_per_loop;
	income += loops * income_per_loop;
	run += num_runs_per_loop * loops;
	// Finish up
	while (run < R)
	{
		U64 orig_head=head;
		bool bFirst=true;
		for (U64 room = k; g[head%N] <= room && (bFirst || ((head % N) != orig_head)); head++)
		{
			income += g[head%N];
			room -= g[head%N];
			bFirst = false;
		}
		head = head % N;
		run++;
	}

	static char buf[16384];
	sprintf(buf, "%I64d", income);
	return buf;
}
