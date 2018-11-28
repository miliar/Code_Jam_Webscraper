#include <iostream>
#include <string.h>
#include <stdlib.h>
using namespace std;

int main()
{
	FILE *in = fopen("C:\\Users\\acer\\Desktop\\B-large.in", "r");
	FILE *out = fopen("C:\\Users\\acer\\Desktop\\A-small-attempt0.out", "w");
//	/in = stdin;
	//out = stdout;
	int T;
	fscanf(in, "%d", &T);
	int n,s,p;
	for (int k = 1; k <= T; k++)
	{
		fscanf(in, "%d", &n);
		fscanf(in, "%d", &s);
		fscanf(in, "%d", &p);
		int res = 0;
		for (int i = 0; i < n; i++)
		{
			int temp;
			fscanf(in, "%d", &temp);
			if (temp == 30 || temp == 29 || temp == 28)
				res++;
			else if (temp == 0)
			{
				if (p == 0)
					res++;
			}
			else if (temp == 1)
			{
				if (p == 0 || p == 1)
					res++;
			}
			else if (temp % 3 == 0)
			{
				if (temp / 3 >= p)
					res++;
				if (s > 0 && temp/3 == p-1)
				{
					res++;
					s--;
				}
			}
			else if (temp % 3 == 1)
			{
				if (temp/3 + 1 >= p)
					res++;
			}
			else if (temp % 3 == 2)
			{
				if (temp/3 +1 >= p)
					res++;
				else if (s>0 && temp/3 == p-2)
				{
					res++;
					s--;
				}
			}
		}
		fprintf(out, "Case #%d: %d\n", k, res);
	}
}
