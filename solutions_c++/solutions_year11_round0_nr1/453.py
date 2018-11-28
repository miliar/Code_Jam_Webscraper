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
//	freopen("A.in","r",stdin);
//	freopen("A-small-attempt0.in","r",stdin);freopen("A-small-attempt0.out","w",stdout);
//	freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
//	freopen("A-small-attempt2.in","r",stdin);freopen("A-small-attempt2.out","w",stdout);
	freopen("A-large.in","r",stdin);freopen("A-large.ans","w",stdout);

	s32 caseNum;
	scanf("%d",&caseNum);

	s32 num;
	deque<pair<s32, s32>> v[2];

	for(s32 caseId=1; caseId <= caseNum; caseId++)
	{
		printf("Case #%d: ",caseId);
		scanf("%d",&num);

		for(s32 i = 0; i < num; i++)
		{
			char c[2];
			s32 x;
			scanf("%s", c);
			scanf("%d", &x);

			c[0] = (c[0] == 'O'?0:1);

			v[c[0]].push_back(MP(i, x));
		}

		s32 pos[2] = {1, 1};
		s32 but = 0;
		s32 count = 0;

		bool should_increase = false;

		while(but < num)
		{
			count++;

			for(int j = 0; j < 2; j++)
			{
				if(SIZE(v[j]) < 1)
				{
					continue;
				}

				pair<s32, s32> p = v[j].front();
				s32 tnum = p.first;
				s32 tpos = p.second;

				if(tpos != pos[j])
				{
					if(tpos > pos[j])
					{
						pos[j]++;
					}
					else
					{
						pos[j]--;
					}
				}
				else
				{
					if(tnum == but)
					{
						should_increase = true;
						v[j].pop_front();
					}
				}
			}

			if(should_increase)
			{
				should_increase = false;
				but++;
			}
		}

		printf("%d\n", count);

		fflush(stdout);
	}

	return 0;
}