#include <cstdio>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;



int main(int argc, char *argv[])
{
    FILE *inf = fopen("input.in","r");
    FILE *of = fopen("out.out","w");
    int N;
    fscanf(inf,"%d\n",&N);
    for(int i=0;i<N;i++){
        char result[100];
        int cont[26] = {0};
        char comb[26][26];
        bool opos[26][26];
        for(int j = 0; j < 26; j++){
            for(int k = 0; k < 26; k++){
                comb[j][k] = '0';
                opos[j][k] = false;
            }
            cont[j] = 0;
        }

        int a,b,c;
        fscanf(inf,"%d ", &a);
        char e1,e2,e3;
        int x1,x2,x3;
        int le = -1;
        for(int j=0; j<a; j++){
            fscanf(inf,"%c%c%c ",&e1,&e2,&e3);
            x1 = e1-'A';x3 = e3-'A';x2 = e2-'A';
            comb[x1][x2] = x3;
            comb[x2][x1] = x3;
        }
        fscanf(inf,"%d ", &b);
        for(int j = 0; j < b; j++){
            fscanf(inf, "%c%c ", &e1,&e2);
            x1 = e1-'A';x2 = e2-'A';
            opos[x1][x2]=true;opos[x2][x1]=true;
        }
        fscanf(inf,"%d ", &c);
        for(int j = 0; j < c; j++){
            fscanf(inf, "%c", &e1);
            
            x1 = e1-'A';
            if(le == -1){
                le = 0;
                cont[x1] ++;
                result[le] = x1;
            }else{
                if(comb[x1][result[le]] != '0' ){
                    cont[result[le]]--;
                    result[le] = comb[x1][result[le]];
                }else{
                    bool found = false;
                    for(int k = 0; k < 26; k++){
                        if(opos[x1][k] && cont[k] > 0){
                            le = -1;
                            for(int l = 0; l < 26; l++)cont[l]=0;
                            found = true;
                            break;
                        }
                    }
                    if(!found){le++;result[le] = x1;cont[x1]++;}
                }
            }
//            fprintf(of,"%c",e1);
            
        }
        fprintf(of,"Case #%d: [", i+1);
        for(int k = 0; k < le; k++){
            fprintf(of,"%c, ", result[k]+'A');
        }
        if(le >= 0)fprintf(of,"%c", result[le]+'A');
        fscanf(inf,"\n");
        fprintf(of,"]\n");
    }
    fclose(inf);fclose(of);
    return EXIT_SUCCESS;
}

