#include <iostream>
#include <fstream>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <stdio.h>

using namespace std;

double prob[10000];

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);

	int nQuestion;

	cin >> nQuestion;

	for( int c=0; c<nQuestion; c++ ){
		int A;
		int B;
		cin >> A >> B;
		prob[0] = 1.0;

		for(int i=1; i<=A; i++){
			cin >> prob[i];
			prob[i] *= prob[i-1];
		}

		double max = -1;
		int right_typ = B-A+1;
		for(int i=0; i<=A; i++)
		{
			int index = A-i;
			int wrong_typ = right_typ+B+1;
			double now = prob[index] * right_typ  + ( 1 - prob[index] ) *wrong_typ;
			if(now < max || max < 0 ) { max = now;}
			//printf("r = %d ,%lf,w = %d , %lf\n",right_typ,prob[index], wrong_typ, ( 1 - prob[index] ));
			right_typ +=2;
		}

		int typ = B+2;
		if(typ < max) { max = typ; }

		printf("Case #%u: %.6f", c+1, max);
		printf("\n");
	}

}