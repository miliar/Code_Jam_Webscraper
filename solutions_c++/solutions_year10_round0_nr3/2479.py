#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

using namespace std;
FILE* foutput;
    FILE *    fp;
char line[40960];
int group[1000]={0,};

void figure(int t,int r,int k,int n)
{
	if(fgets(line, sizeof(line), fp) == NULL) 
	{
		printf("fgets() fail\n");
		exit (1);
	}
	char* pToken=strtok(line," ");
	int i=0;
	while(pToken)
	{
		group[i]=atoi(pToken);
		pToken=strtok(NULL," ");
		i++;
	}
	int nAmount=0;
	int nProfit=0;
	int nPos=0;
	int nStart=0;


	for(int i=0;i<r;++i)
	{
		nStart=nPos;
		nProfit=0;
		while(1)
		{
			nProfit+=group[nPos];
			if(nProfit > k)
			{
				nAmount+=nProfit-group[nPos];
				break;
			}
			if(nPos+1 == n)
				nPos=0;
			else
				++nPos;
			if(nPos==nStart)
			{
				nAmount+=nProfit;
				break;
			}
		}
	}



	fprintf(foutput,"Case #%d: %d\n",t,nAmount);

}

int main(int argc, char **argv)
{

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

	int r,k,n;

    for(i=0;i<N;i++) 
	{
        if(fgets(line, sizeof(line), fp) == NULL) 
		{
            printf("fgets() fail\n");
            exit (1);
        }
		if(sscanf(line,"%d %d %d",&r,&k,&n)!=3)
		{
			printf("invalid format\n");
			exit (1);
		}
		figure(i+1,r,k,n);
    }


    fclose(fp);
	fclose(foutput);
    return 0;
}
