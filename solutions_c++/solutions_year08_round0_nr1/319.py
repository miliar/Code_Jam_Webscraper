#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string.h>
using namespace std;

struct point
{
	char s[100];
	int b;
};

point A[100];
int S;

int main()
{
	FILE * f;
	fopen_s(&f, "A.in", "r");
//	ifstream f("A.in");
	ofstream ff("A.out");
	int i, j, k, N, Ni, Q;

	fscanf(f, "%d", &N);

	for(Ni = 1; Ni <= N; ++Ni)
	{
		char s[100];
		int n = 0, d = 0;

		fscanf(f, "%d", &S);
		fgets(s, 100, f);
		for(i = 0; i < S; ++i)
		{
			fgets(A[i].s, 100, f);
			A[i].b = 0;
		}

		fscanf(f, "%d", &Q);
		fgets(s, 100, f);
		for(i = 0; i < Q; ++i)
		{
			fgets(s, 100, f);
			for(j = 0; j < S; ++j)
			{
				char * s1 = A[j].s;

				k = 0;
				while((s[k]) && (s1[k]) && (s[k] == s1[k])) ++k;
				if((!s[k]) && (!s1[k]))
				{
					if(!A[j].b)
					{
						++d;
						A[j].b = 1;
					}
					break;
				}
			}
			if(d == S)
			{
				d = 1;
				for(k = 0; k < S; ++k)
					A[k].b = 0;
				A[j].b = 1;
				++n;
			}
		}
		ff << "Case #" << Ni << ": " << n << endl;
	}

	return 0;
}