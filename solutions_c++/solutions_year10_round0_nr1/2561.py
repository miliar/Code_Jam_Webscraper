#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

using namespace std;
FILE* foutput;

void snapper(int t,int n,int k)
{
	fprintf(foutput,"Case #%d: %s\n",t,(k+1)%(int)pow((double)2,n)==0?"ON":"OFF");
}

int main(int argc, char **argv)
{
	char line[4096];
    FILE *    fp;

    int        i, N;

    size_t    len;

    if(argc!=2) {
        printf("usage: %s input_file\n", argv[0]);
        exit (1);
    }

	cout << argv[1] <<endl;
    if((fp = fopen(argv[1], "r")) == NULL) {
        printf("fopen() fail %d\n",errno);
        exit (1);
    }
	if((foutput=fopen("output.out","w+"))==NULL){
        printf("output fopen() fail %d\n",errno);
        exit (1);
	}

    if(fgets(line, sizeof(line), fp) == NULL) {
        printf("fgets() fail\n");
        exit (1);
    }
    if(sscanf(line, "%d", &N)!=1) {
        printf("invalid format\n");
        exit (1);
    }

	int n,k;

    for(i=0;i<N;i++) 
	{
        if(fgets(line, sizeof(line), fp) == NULL) 
		{
            printf("fgets() fail\n");
            exit (1);
        }
		if(sscanf(line,"%d %d",&n,&k)!=2)
		{
			printf("invalid format\n");
			exit (1);
		}
		snapper(i+1,n,k);
    }


    fclose(fp);
	fclose(foutput);
    return 0;
}