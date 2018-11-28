// DancingStars.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>
#include <algorithm>

using namespace std;

int count(int N, int S, int P, int points[])
{
	int result = 0;

	for (int i=1; i<=N; ++i)
	{
		int modus = points[i] %3;
		int a = (int) points[i]/3;

		if (modus ==0){
			if ( a >=P)
				++result;
			else if ( (a>=1) && (S>=1) && ( a+1 >=P))
			{
				--S;
				++result;
			}
		} 
		else if (modus == 1) {
			if ( (a+1) >=P)
				++result;
			else if ( (S>=1) && ( a+1 >=P))
			{
				--S;
				++result;
			}
		}
		else if (modus == 2) {
			if ( a+1 >= P)
				++result;
			else if ( (S>=1) && (a+2 >=P) )
			{
				--S;
				++result;
			}
		}
	};

	return result;
}

int main(int argc, char* argv[])
{
	int T,N, surprise, P;
	int points[101];
	
	freopen("c://temp//in.txt","r+", stdin);
	freopen("c://temp//out.txt","w+", stdout);

	scanf("%i", &T);

	for (int i=1; i<=T; ++i)
	{
		scanf("%i", &N);
		scanf("%i", &surprise);
		scanf("%i", &P);
		for (int j=1; j<=N; ++j)
			scanf("%i", &(points[j]) );

		printf("Case #%i: %i\n", i, count(N,surprise,P,points) );
	};

	return 0;
}

