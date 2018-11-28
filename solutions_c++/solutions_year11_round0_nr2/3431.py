/*
5
0 0 2 EA
1 QRI 0 4 RRQR
1 QFT 1 QF 7 FAQFDFQ
1 EEZ 1 QE 7 QEEEERA
0 1 QW 2 QW

Case #1: [E, A]
Case #2: [R, I, R]
Case #3: [F, D, T]
Case #4: [Z, E, R, A]
Case #5: []
*/

#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

int C;
char c1[40], c2[40], c3[40];
int D;
char d1[40], d2[40];
int N=0;
char e[120];
vector<char> v;

int combine(char in1, char in2, char* out)
{
	int find = 0;

	for(int i=0; i<C; i++)
	{
		if ( (in1 == c1[i] && in2 == c2[i])
		  || (in1 == c2[i] && in2 == c1[i]))
		{
			char combined = 0;
			*out = c3[i];
			return 1;
		}
	}

	return 0;
}

int oppose(char e)
{
	for(int j=0; j<v.size();j++)
	{
		for(int i=0; i<D; i++)
		{
			if ((e == d1[i] && v[j] == d2[i])
			  ||(e == d2[i] && v[j] == d1[i]))
			{
				return 1;
			}
		}
	}
	return 0;
}

int main()
{
	freopen("input.txt", "rt", stdin);
//	freopen("output.txt", "wt", stdout);

	int num;
	scanf("%d", &num);
//printf("num=%d\n", num);

	for (int ii=0; ii<num; ii++)
	{
		v.clear();
		scanf("%d", &C);
//printf("C=%d\n", C);

		for(int i = 0; i < C; i++)
		{
			scanf(" %c%c%c", &c1[i], &c2[i], &c3[i]);
//printf("%c %c -> %c\n", c1[i],c2[i],c3[i]);
		}

		scanf("%d", &D);
//printf("D=%d\n", D);
		for(int i = 0; i < D; i++)
		{
			scanf(" %c%c", &d1[i], &d2[i]);
//printf("%c %c\n", d1[i],d2[i]);
		}

		scanf("%d", &N);
//printf("N=%d\n", N);
		scanf("%s", e);
//printf("%s\n", e);

		int idx=0;
		while(idx < N)
		{
			if(oppose(e[idx])==1)
			{
//printf("%d: %c -> CLEAR\n", idx, e[idx]);
				v.clear();
				idx++;
				continue;
			}

			if(idx+1<N)
			{
				char a;
				if(combine(e[idx], e[idx+1],&a)==1)
				{
//printf("%d: %c,%c-> %c\n",idx,e[idx],e[idx+1],a);
					v.push_back(a);
					idx+=2;
					continue;
				}
			}

			v.push_back(e[idx]);
//printf("%d: %c\n",idx,e[idx]);
			idx++;
		}

		printf("Case #%d: [", ii+1);
		for(int i = 0; i < v.size(); i++)
		{
			if(i>0)
				printf(", ");
			printf("%c", v[i]);
		}
		printf("]\n");
	}

	return 0;
}

