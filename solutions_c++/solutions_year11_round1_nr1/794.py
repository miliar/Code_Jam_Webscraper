// r1_1.cpp : Defines the entry point for the console application.
//


#include<stdio.h>
#include<memory.h>
#include<string.h>

int gcd(int a,int b){
    int c;
    while(1)
    {
  	c = a%b;
  	if(c==0)
  	  return b;
  	a = b;
  	b = c;
    }
  }

void main(){

	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");

	int tc;
	int i, n, pd, pg, g, t;
	bool poss;

	fscanf(fp, "%d", &tc);

	for(i=0; i<tc; i++){
		fscanf(fp, "%d %d %d", &n, &pd, &pg);
		if(n<0) n = 200;
		if(pd != 0)	g = gcd(100, pd);
		else g=100;
		t = 100 / g;
		if(t<=n){
			if(pd<100 && pg==100) poss = false;
			else if(pd>0 && pg==0) poss = false;
			else poss = true;
		}
		else poss = false;
		if(pd == 0 && pg != 100) poss = true;
		if(poss) fprintf(ofp, "Case #%d: Possible\n", i+1);
		else fprintf(ofp, "Case #%d: Broken\n", i+1);
		printf("n = %d\n", n);
	}

	i=2;

}

