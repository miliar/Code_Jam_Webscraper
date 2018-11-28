
// (c) Alvaro Salmador 2010-2011

#pragma warning(disable : 4996)
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
//#include <math.h>
#include <algorithm>
/*#include <string>
#include <list>
#include <vector>
#include <map>*/

using namespace std;


//typedef long long ll;
//typedef unsigned long long ull;


int N=0,M=0;

int moves[100];
int cost[100];

bool get_input()
{
	static int T = -1;
	
	if (T<0)
		scanf("%d", &T);
	
	if (T>0)
	{
		--T;

		if (scanf("%d", &N)!=1)
			return false;

		int i;
		for(i=0; i<N; ++i)
		{
			char bot=0,k;
			if (scanf("%c%c %d", &k, &bot, &moves[i])!=3)
				return false;

			if (bot=='B')
				moves[i] = -moves[i];
		}

		return true;
	}
	else
		return false;
}


int sign(int a)
{
	return (a<0)?1:0;
}

int main()
{

	for(int ncase=1; get_input(); ++ncase)
	{
		//fprintf(stderr, "\nCase #%d\n", ncase); fflush(stderr);
		printf("Case #%d: ", ncase);

		int i, t=0, last=0, p[]={1,1}, lastb=sign(moves[0]);
		for(i=0; i<N; ++i)
		{
			const int b=sign(moves[i]), m=abs(moves[i]);
			int c=abs(p[b]-m);
			
			if (lastb!=b) {
				c = (c>last) ? (c-last) : 0;
				//fprintf(stderr, "b=%d t=%d: c0=%d c=%d last=%d-\n", b, t, abs(p[b]-m), c, last);
				last = c+1;
			} else 
				last += c+1;
			
			t += c+1;

 			p[b] = m;
			lastb = b;
		}

		printf("%d\n", t);
	}

	return 0;
}


