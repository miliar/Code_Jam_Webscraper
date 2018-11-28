#include <stdio.h>
#include <algorithm>
#include <string.h>
#include <stdlib.h>
#include <iostream>
#define unsigned long long uint_64

using namespace std;

const char input[] = "codejam31.in";
const char output[] = "codejam31.out";

int main()
{
	freopen(input, "r", stdin);
	freopen(output, "w", stdout);
	
	int t;
	scanf("%d\n", &t);
	
	int test;
	for(test = 1; test <= t; ++test)
	{
		int *use = new int['z'+1];
		int i;
		for(i = 0; i <= 'z'; ++i) use[i] = -1;
		
		char *numar = new char[64];
		scanf("%s", numar);
		
		int ndif = 0;
		use[numar[0]] = 1;
		for(i = 1; numar[i]; ++i)
			if(use[numar[i]] == -1)
			{	use[numar[i]] = 0, ++ndif; break;}
		
		if(numar[i])			
		for(++i; numar[i] != NULL; ++i)
			if(use[ numar[i] ] == -1)
				use[numar[i]] = ++ndif;
			
		long long rez = 0;
		if(ndif == 0) ndif = 1;
		for(i = 0; numar[i] != NULL; ++i)
			rez = (long long)rez * (ndif+1) + (long long)use[numar[i]];

		cout << "Case #" << test << ": " << rez << "\n";
	}
	return 0;
}
