/*******************************************\
*                                           *
*   Roller Coaster                          *
*   CodeJam 2010                            *
*   Rafael Medina (MedinaSoft)              *
*                                           *
\*******************************************/

#include <iostream>
#include <cmath>

//Globals
#define MYSIZE 10000
FILE *infile,*outfile;
char line[MYSIZE],tmp[MYSIZE];


void roller_coaster() {
    int num=0,totlines;


    int R,k,N,ng,G[1000],p,z;
    double money;

    while ( fgets( line, MYSIZE, infile ) != NULL ) {
        if (num == 0) {
            totlines = atoi(line);
            //printf("Total Number of Lines (with data) :: %d",totlines);
            //fprintf(outfile,"Case #%d: ",num);
        }
        else if (num <= (totlines * 2)) {
            if (num > 1) { printf("\n"); fprintf(outfile,"\n"); }
            strcpy(tmp,line);
            R = atoi(strtok(tmp," "));
            k = atoi(strtok(NULL," "));
            N = atoi(strtok(NULL," "));
            num++;
            fgets( line, MYSIZE, infile );
            strcpy(tmp,line);
            G[0] = atoi(strtok(tmp," "));
            for(int i=1; i<N;i++) { G[i] = atoi(strtok(NULL," ")); }
            money=0;
            //Roller Coaster Time..
            for(int i=0; i<R;i++) {
                p=0; ng=0;
                while(((G[0] + p) <= k) && ng < N) {
                    ng++;
                    money += G[0];
                    p += G[0];
                    z = G[0];
                    for(int j=1; j<N; j++) { G[j-1] = G[j]; }
                    G[N-1] = z;
                }
            }
            //results
            printf("Case #%d: %.f",(num/2),money);
            fprintf(outfile,"Case #%d: %.f",(num/2),money);

        }
        num++;
    }
}

int main (int argc, char *argv[]) {
    if (argc >= 2) {
        infile = fopen(argv[1],"r");
        if (infile == NULL) {
            printf("Error Opening File \"%s\"\n",argv[1]);
            return 2;
        }
        else {
            char myoutfile[255];
            sprintf(myoutfile,"%s.out",argv[1]);
            outfile = fopen(myoutfile,"w");
            if (outfile == NULL) {
                fclose(infile);
                printf("Error: Cannot Create Output File \"%s\"\n",myoutfile);
                return 3;
            }
            //time to work...
            roller_coaster();
            //...phew i finished :D
            fclose(infile);
            fclose(outfile);
            //printf("\n\n(: Finished :)\n");
            return 0;
        }
    }
    else {
        printf("Usage: %s input.in",argv[0]);
        return 1;
    }
}
