#include <iostream>
#include <cstdio>
using namespace std;

int main(int argc, char** argv)
{
	int T;
	FILE* fp = fopen("D:\\B-small-attempt1.in", "r");
	FILE* fo = fopen("D:\\output.txt", "w");
	fscanf(fp, "%d", &T);
	for(int kase = 1; kase <= T; kase ++)
	{
		int N;
		int S;
		int p;
		int t[31];
		fscanf(fp, "%d%d%d", &N, &S, &p);
		
		int ns = 0;
		int s = 0;
		for (int i = 0; i < N; i ++)
		{
			int tmp;
			fscanf(fp, "%d", &tmp);
			int av = tmp / 3;
			int ar = tmp % 3;
			if (ar == 0)
			{
				if (av == 0 && av >= p)
					ns ++;
				else if (av >= p)
					ns ++;
				else if (av + 1 >= p && av != 0)
					s ++;
			}
			else if (ar == 1)
			{
				if (av + 1 >= p)
					ns ++;
			}
			else if (ar == 2)
			{
				if (av + 1 >= p)
					ns ++;
				else if (av + 2 >= p)
					s ++;
			}
		
		}
		int res = ns + min(s, S);
		fprintf(fo, "Case #%d: %d\n", kase, res);
		
	}
	return 0;
}

