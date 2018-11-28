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
//	freopen("B.in","r",stdin);
//	freopen("B-small-attempt0.in","r",stdin);freopen("B-small-attempt0.out","w",stdout);
//	freopen("B-small-attempt1.in","r",stdin);freopen("B-small-attempt1.out","w",stdout);
//	freopen("B-small-attempt2.in","r",stdin);freopen("B-small-attempt2.out","w",stdout);
	freopen("B-large.in","r",stdin);freopen("B-large.ans","w",stdout);

	s32 caseNum;
	scanf("%d",&caseNum);

	s32 num;

	for(s32 caseId=1; caseId <= caseNum; caseId++)
	{
		printf("Case #%d: ",caseId);

		scanf("%d", &num);

		vector<string> comb;
		vector<string> opp;

		for(s32 i = 0; i < num; i++)
		{
			char c[4];
			scanf("%s", c);

			comb.push_back(string(c));
		}

		scanf("%d", &num);

		for(s32 i = 0; i < num; i++)
		{
			char c[4];
			scanf("%s", c);

			opp.push_back(string(c));
		}

		scanf("%d", &num);
		char *s = new char[num + 1];
		scanf("%s", s);
		string q(s);
		delete s;

		string result;

		for(int i = 0; i < LEN(q); i++)
		{
			result.append(1, q[i]);

			s32 len = LEN(result);

			bool change = true;

			while(len > 1 && change)
			{
				change = false;

				for(int j = 0; j < SIZE(comb); j++)
				{
					string &str = comb[j];

					if(str[0] == result[len - 1])
					{
						if(str[1] == result[len - 2])
						{
							result[len - 2] = str[2];
							result.erase(len - 1);
							len--;
							change = true;
							break;
						}
					}

					if(str[1] == result[len - 1])
					{
						if(str[0] == result[len - 2])
						{
							result[len - 2] = str[2];
							result.erase(len - 1);
							len--;
							change = true;
							break;
						}
					}
				}
			}
			
			len = LEN(result);

			if(len > 1)
			{
				for(int x = 0; x < len; x++)
				{
					char a = result[x];

					for(int y = x + 1; y < len; y++)
					{
						char b = result[y];

						for(int j = 0; j < SIZE(opp); j++)
						{
							string &str = opp[j];

							if(str[0] == a)
							{
								if(str[1] == b)
								{
									result.clear();
									len = 0;
									break;
								}
							}

							if(str[0] == b)
							{
								if(str[1] == a)
								{
									result.clear();
									len = 0;
									break;
								}
							}
						}
					}
				}
			}
		}

		printf("[");

		for(int i = 0; i < LEN(result); i++)
		{
			printf("%c", result[i]);

			if(i < LEN(result) - 1)
			{
				printf(", ");
			}
		}

		printf("]\n");

		fflush(stdout);
	}

	return 0;
}