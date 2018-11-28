#include <stdio.h>
#include <iostream>
#include <memory.h>
#include <assert.h>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <set>
#include <deque>
#include <math.h>

using namespace std;


int CalculNbDigit(int a)
{
	int nbdigit=0;
	while(a>=1)
	{
		a/=10;
		nbdigit++;
	}
	return nbdigit;
}

int main( )
{
	set<int> save_deleted;
	int t,tt=0, nbpair, m;
	int A,B, last_digit;
	int tab_m[7];
	int nbdigit;
	FILE * INPUT = NULL;
	INPUT = fopen( "input.txt", "r");
	FILE * OUTPUT = NULL;
	OUTPUT = fopen( "output.txt", "w");

	fscanf(INPUT,"%d\n", &tt);
	for( t = 1; t <= tt;  ++t )
	{
		nbpair=0;
		fprintf(OUTPUT, "Case #%d: ", t);
		fscanf(INPUT,"%d",&A);
		fscanf(INPUT,"%d",&B);
		
		for(int n=A; n<=B ; n++)
		{
				nbdigit = CalculNbDigit(n);
				m = n;
				for(int perm = 1 ; perm <= nbdigit ; ++perm)
				{
					last_digit = m%10;
					m = (m - last_digit)/10 + last_digit*((int) powf(10,nbdigit-1));
					//fprintf(OUTPUT,"\nlast_digit = %d\nn actuel = %d\nm actuel = %d\n", last_digit, n, m);
					if(m > n && m <= B && (save_deleted.find(m) == save_deleted.end()))
					{
						save_deleted.insert(m);
						nbpair++;
					}
				}
				//fprintf(OUTPUT,"nbdigit = %d\n", nbdigit);
				save_deleted.clear();

		}

		fprintf(OUTPUT,"%d\n", nbpair);

		if(!feof(INPUT))
			fprintf(OUTPUT,"\n");
	}

}
