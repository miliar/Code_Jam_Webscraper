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

FILE *in=fopen("D.in","r");
FILE *outt=fopen("D.out","w");

char ar[1100];

int main()
{
	int i,j,k,test,tests;
	int n,ret;
	fscanf(in,"%d",&tests);
	for(test=1;test<=tests;test++){
		ret=1<<20;
		fscanf(in,"%d",&k);
		fscanf(in,"%s",ar);
		string x=ar;
		string y;
		n=x.size();
		int perm[6];
		for(i=0;i<k;i++)perm[i]=i;
		do{
			y="";
			for(i=0;i<n/k;i++){
				for(j=i*k;j<(i+1)*k;j++){
					y+=x[perm[j-i*k]+i*k];
				}
			}
			int Q=0;
			for(i=0;i<n;i++){
				while(i+1<n && y[i]==y[i+1])i++;
				Q++;
			}
			ret=min(ret,Q);
		}while(next_permutation(perm,perm+k));
		fprintf(outt,"Case #%d: %d\n",test,ret);
	}
	return 0;
}
