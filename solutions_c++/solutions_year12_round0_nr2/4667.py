#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <iostream>
#include <fstream>
#include <vector>


int main(int argc, char** argv) {
    if (argc<3) {
        printf("not enough parameters: %d\n", argc);
        return 0;
    }
    FILE *fp;
    printf("%s\n", argv[1]);

    if ( (fp = fopen( (const char*) argv[1], "r" )) == NULL ) {
        printf("Open Input File ERROR!\n"); 
        return 0;
    }

    std::ofstream ofs(argv[2]);

    int nT;
    fscanf(fp, "%d\n", &nT);
    printf("#T: %d\n", nT);

    int rv, score;
    char ch[1000];
    memset(ch, 0, sizeof(char)*1000);
    std::vector<int> line;
    for (int i=0; i<nT; ++i) {
        printf("Case #%d: \n", i+1);

        rv = fscanf(fp, "%[ 0-9]\n", ch);
//        printf("%s\n", ch);
        if (rv>0) {
            line.clear();
            char* pch = strtok(ch, " ");
            line.reserve(atoi(pch)+3);
            while( pch!=NULL) {
                int val = atoi(pch);
                line.push_back(val);
                pch = strtok(NULL, " ");
            }
            if (line.size()<line[0]+3) {
                printf("Case broken\n");
                continue;
            }
            //
            int sizecase = line[0], ns = line[1], pbar = line[2];
            int nlive = 0, ndead = 0, nmargin = 0;
            printf("#ns: %d  #pbar: %d  \n", ns, pbar);
            for ( int j=0; j<sizecase; ++j) {
                int score = line[j+3];
                printf("#score: %d\n", score);

                int avg = score/3, res = score%3;
                printf("#avg: %d  #res: %d \n", avg, res);

                if ( avg>=pbar ) ++nlive;
                else if ( res>0 and (avg+1>=pbar) ) ++nlive;
                else if ( (avg>0) and res==0 and (avg+1>=pbar) ) ++nmargin;
                else if ( ( avg+res ) < pbar) ++ndead;
                else ++nmargin;
            }

            printf("#nlive: %d,  #ndead: %d,  #nmargin: %d\n", nlive, ndead, nmargin);
            printf("Result: %d\n", nlive + std::min(nmargin, ns));
            int result = nlive + std::min(nmargin, ns);

            ofs<<"Case #"<<i+1<<": "<<result;

            if (i+1!=nT) ofs<<std::endl;

        }
        else printf("#rv: %d\n", rv);
            
    }




    ofs.close();

    fclose(fp);
}

