#include<iostream>
#include<string>
#include<math.h>
using namespace std;
int main()
{   char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");
	int T;
	int i,j;

	fscanf(fp, "%d", &T);

	int L[T][2];
	char Y[T][4];

    for(i=1;i<=T;i++)
    {   j=0;
        while(j<2){
            fscanf(fp, "%d", &L[i][j]);
            j++;
        }
	}
	for(i=1;i<=T;i++)
	{   int nk1 = 0;
	    j=0;
        while(j <= L[i][0] - 1)
        {   nk1+=pow(2,j);
            j++;
        }
        if(L[i][1]==nk1) strcpy(&Y[i][0],"ON");
        else
        {   int nk2=nk1;
            do
            {   nk2+=nk1 + 1;
            }while((nk2!=L[i][1])&&(nk2<=100000000));
            if(nk2==L[i][1]) strcpy(&Y[i][0],"ON");
            else strcpy(&Y[i][0],"OFF");
        }
	}

    for(i=1;i<=T;i++)
    {   fprintf(ofp, "Case #%d: %s \n", i,&Y[i][0]);
    }

    return 0;
}
