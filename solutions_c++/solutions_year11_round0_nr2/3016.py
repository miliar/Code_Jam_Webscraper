
// (c) Alvaro Salmador 2010-2011

#pragma warning(disable : 4996)
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <algorithm>
/*#include <string>
#include <list>
#include <vector>
#include <map>*/

using namespace std;

//typedef long long ll;
//typedef unsigned long long ull;


int N=0,nC=0,D=0;
char C[32][32];
char O[32][32];
char S[128];

bool get_input()
{
	static int T = -1;
	
	if (T<0)
		scanf("%d", &T);
	
	if (T>0)
	{
		--T;

		memset(O, 0, sizeof(O));
		memset(C, 0, sizeof(C));

		if (scanf("%d", &nC)!=1)
			return false;

		int i;
		char k,a,b,c;
		for(i=0; i<nC; ++i)
		{
			if (scanf("%c%c%c%c", &k, &a, &b, &c)!=4)
				return false;
			a-=64;
			b-=64;
			C[a][b] = C[b][a] = c;
		}

		if (scanf("%d", &D)!=1)
			return false;
		
		for(i=0; i<D; ++i)
		{
			if (scanf("%c%c%c", &k, &a, &b)!=3)
				return false;
			a-=64;
			b-=64;
			O[a][b] = O[b][a] = 1;
		}

		if (scanf("%d", &N)!=1)
			return false;
		
		scanf("%c", &k);
		if (scanf("%s", &S)!=1)
			return false;

		//while(fgetc(stdin)!='\n') ;

		return true;
	}
	else
		return false;
}

inline bool opp(char a, char b)
{
	return O[a-64][b-64]!=0;
}

inline char cmb(char a, char b)
{
	return C[a-64][b-64];
}

int main()
{

	for(int ncase=1; get_input(); ++ncase)
	{
		printf("Case #%d: ", ncase);

		char r[100];
		int j=0;
		memset(r,0,sizeof(r));

		r[0] = S[0];
		for(int i=1; i<N; ++i)
		{
			const char c = S[i];

			if (cmb(c, r[j]))
				r[j] = cmb(c, r[j]);
			else
				r[++j] = c;
			
			for(int k=0; k<j; ++k)
			{
				if (opp(r[j],r[k]))
				{
					memset(r,0,sizeof(r));
					j=0;
					if (i<N-1)
						r[0] = S[++i];
				}
			}
		}

		printf("[");
		for(char*p=r; *p!=0; ++p)
		{
			if (p!=r) printf(", ");
			printf("%c", *p);
		}
		//printf("%s", r);
		printf("]\n");
	}

	return 0;
}

