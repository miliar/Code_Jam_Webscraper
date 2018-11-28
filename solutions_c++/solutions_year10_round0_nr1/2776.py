/*******************************************\
*                                           *
*   Snapper Chain                           *
*   CodeJam 2010                            *
*   Rafael Medina (MedinaSoft)              *
*                                           *
\*******************************************/

#include <iostream>
#include <cmath>

//Globals
#define MYSIZE 500
FILE *infile,*outfile;
char line[MYSIZE],tmp[MYSIZE];
void snapper_chain() {
    int num=0,totlines,t[2];
    int K,N;
    int s,r;
    while ( fgets( line, MYSIZE, infile ) != NULL ) {
        if (num == 0) {
            totlines = atoi(line);
            //printf("Total Number of Lines (with data) :: %s",line);
        }
        else if (num <= totlines) {
            strcpy(tmp,line);
            N = atoi(strtok(tmp," "));
            K = atoi(strtok(NULL,"\n"));
            if (num > 1) { printf("\n"); fprintf(outfile,"\n"); }
            //i like binary.. so this should be -easy- fun :S..
            /*
                Reading the problem i noticed it has something to do with binary
                so poking around i found out a formula that (hopefully) can solve this problem

                Times of snaps to ON
                    s = (2^N) - 1

                And to calculate if after K times we manage to turn ON the bulb

                (for N=1)
                    K times has to be an odd number

                (for N>1)
                    r = (K % (2^N)) - s

                    if (r == 0) ON
                    else OFF

            */
            if (K==0) {
                printf("Case #%d: OFF",num);
                fprintf(outfile,"Case #%d: OFF",num);
            }
            else if (N == 1) {
                if ((K % 2) == 0){
                    printf("Case #%d: OFF",num);
                    fprintf(outfile,"Case #%d: OFF",num);
                }
                else {
                    printf("Case #%d: ON",num);
                    fprintf(outfile,"Case #%d: ON",num);
                }
            }
            else {
                s = (int)(pow(2,N) - 1);
                if (s == K) {
                    printf("Case #%d: ON",num);
                    fprintf(outfile,"Case #%d: ON",num);
                }
                else if (K < s) {
                    printf("Case #%d: OFF",num);
                    fprintf(outfile,"Case #%d: OFF",num);
                }
                else {
                    r = ((K % (int)pow(2,N)) - s);
                    if (r == 0) {
                        printf("Case #%d: ON",num);
                        fprintf(outfile,"Case #%d: ON",num);
                    }
                    else {
                        printf("Case #%d: OFF",num);
                        fprintf(outfile,"Case #%d: OFF",num);
                    }
                }
            }
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
            snapper_chain();
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
