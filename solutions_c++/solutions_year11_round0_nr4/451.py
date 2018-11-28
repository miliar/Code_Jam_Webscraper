#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#include <vector>
#include <deque>
#include <list>
#include <map>
#include <set>
#include <algorithm>

#include <iostream>
#include <sstream>

typedef char s8;
typedef unsigned char u8;
typedef short s16;
typedef unsigned short u16;
typedef int s32;
typedef unsigned int u32;
typedef long long s64;
typedef unsigned long long u64;

using namespace std;

#define SAFE_AVERAGE(x, y) ((x&y)+((x^y)>>1))
#define MP(x, y) make_pair(x, y)
#define LEN(x) ((s32)x.length())
#define SIZE(x) ((s32)x.size())

template<class T>
T& Max(T a, T b) { return b > a?b:a; }

int main()
{
//	freopen("D.in","r",stdin);
//	freopen("D-small-attempt0.in","r",stdin);freopen("D-small-attempt0.out","w",stdout);
//	freopen("D-small-attempt1.in","r",stdin);freopen("D-small-attempt1.out","w",stdout);
//	freopen("D-small-attempt2.in","r",stdin);freopen("D-small-attempt2.out","w",stdout);
	freopen("D-large.in","r",stdin);freopen("D-large.ans","w",stdout);

	s32 caseNum;
	scanf("%d",&caseNum);

	s32 num;

	for(s32 caseId=1; caseId <= caseNum; caseId++)
	{
		printf("Case #%d: ",caseId);

		scanf("%d", &num);

		deque<s32> v;

		for(s32 i = 0; i < num; i++)
		{
			s32 n;
			scanf("%d", &n);

			v.push_back(n);
		}

		s32 tot = SIZE(v);

		for(int i = 0; i < SIZE(v); i++)
		{
			if(i + 1 == v[i])
			{
				tot--;
			}
		}

		printf("%d.000000", tot);

		printf("\n");
		fflush(stdout);
	}

	return 0;
}