#include <iostream>
#include <sstream>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <list>
#include <stack>
#include <algorithm>
#include <string>
#include <cmath>
#include <cstdio>
#define eps (1e-5)
#define infinite ((1<<31)-1)

using namespace std;


int main(int argc, char *argv[]){

	FILE *fp = fopen(argv[1],"r");
	FILE *out = fopen("output.txt","w+");
	if(fp == NULL)
		printf("file error.\n");

	int T,n,k;
	fscanf(fp,"%d",&T);

	for(int i = 1;i <= T;++i){
		fscanf(fp,"%d %d",&n,&k);
		if(1 == n){
			if(k % 2 == 0)
				fprintf(out,"Case #%d: OFF\n",i);
			else
				fprintf(out,"Case #%d: ON\n",i);

		}
		
		else{
			unsigned int number = (unsigned int)pow(2.0,n) - 1;
			if( (k - number) % (number + 1) == 0)
				fprintf(out,"Case #%d: ON\n",i);
			else
				fprintf(out,"Case #%d: OFF\n",i);
		}
	}

	return 0;
}