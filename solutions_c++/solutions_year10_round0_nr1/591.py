#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <algorithm>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <iterator>
#include <iostream>
#include <functional>
#include <sstream>
#include <numeric>

#define CLR( x , y ) ( memset( (x) , (y) , sizeof( (x) ) ) )
#define EPS 1e-9

using namespace std;

FILE *in=fopen("QA.in","r");
FILE *out=fopen("QA.out","w");

int main()
{
	int i,j,n,k;
	int tests;
	fscanf(in,"%d",&tests);
	for(int test=0;test<tests;test++){
		fscanf(in,"%d%d",&n,&k);
		int on[40];
		CLR(on,0);
		k%=(1<<n);
		if((1<<n)-1!=k)fprintf(out,"Case #%d: OFF\n",test+1);
		else fprintf(out,"Case #%d: ON\n",test+1);
	}
	return 0;
}