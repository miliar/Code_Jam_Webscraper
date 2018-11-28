#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <deque>
#include <bigint.h>
#include <set>
#include "general.h"
using namespace std;

#define Max(a, b) (a > b ? a : b)
#define Min(a, b) (a < b ? a : b)
/*
class Num
{
public:
	int num_;
	int *p_;

	Num(int num, int *p)
	{
		num_ = num;
		p_ = p;
	}

	Num(Num & n)
	{
		num_ = n.num_;
		p_ = n.p_;

	}

};

bool operator<(Num &n1, Num &n2)
{
	return n1.num_ < n2.num_;
}

void MergeSet(set<int> *s1, set<int>* s2, Num * num)
{
	int base = num[0].num_;
	set<int>::iterator iter;
	for(iter = s2->begin(); iter != s2->end(); iter++)
	{
		num[*iter - base] .p_ = s1;
		s1->insert(*iter);

	
void Merge(Queue< set<int> >& qset, int n, Num * num, int ni, int nj, int P)
{
	if(IsTrue(ni, nj, P))
	{

*/

int IsPrime(int x)
{

	for(int i = 2; i < (int)sqrt((double)x) + 1; i++)
		if(x % i == 0)
		{

			return 0;
		}

	return 1;
}

int Do(int a, int b, int P)
{
	int * flag = new int[b - a + 1];
	int n = b - a + 1;
	memset(flag, 0, n * sizeof(int));
	int count = 0;
	int f;
	int g;

	for(int x = P; x <= b; x++)
	{
		if(IsPrime(x))
		{
			f = 1;
			g = 0;
			for(int i = 0; i < n; i++)
			{
				if((a + i) % x == 0)
				{
					g = 1;
					if(flag[i])
					{
						f = 0;
						
					}
					flag[i] = 1;
				}
			}
			if(f && g)
				count ++;
		}
	}
	for(int i = 0; i < n; i++)
		if(!flag[i])
			count++;

	delete[] flag;

	return count;
}




int main(int argc, char ** argv)
{
	int ncases;

	FILE* fpin, * fpout;


	int a, b, P;

	if(argc < 3)
	{
		printf("Requires in and out filename!\n");
		return 0;
	}

	int re;
	fpin = fopen(argv[1], "r");
	fpout = fopen(argv[2], "w");

	fscanf(fpin, "%d", &ncases);
	for(int k = 0; k < ncases; k++)
	{
		fscanf(fpin, "%d%d%d", &a, &b, &P);
		re = Do(a, b, P);
		fprintf(fpout, "Case #%d: %d\n", k + 1, re);

		
	}



	fclose(fpin);
	fclose(fpout);


	return 0;
}

