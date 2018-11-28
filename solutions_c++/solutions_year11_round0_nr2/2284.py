#include <cstdlib>
#include <iostream>

using namespace std;
char c1[35],c2[35],c3[35],op1[35],op2[35],ex[35];
int vcount[35];
char result[200];

int main(int argc, char *argv[])
{
    int t;
    int n1,n2,n3,validatepos;
    int n,firstdata;
    char rb;
    scanf("%d", &t);
    for (int i=1; i<=t; i++){
        for (int j = 0; j < 35; j++) {
             c1[j] = c2[j] = c3[j] = '.';
             op1[j]=op2[j]=ex[j]='.';
             vcount[j] = 0;
        }
        scanf("%d", &n1);
        for(int j=0; j<n1 ; j++){
            scanf(" %c%c%c", &c1[j],&c2[j],&c3[j]);
        }
        scanf("%d", &n2);
        for(int j=0; j<n2 ; j++){
            scanf(" %c%c", &op1[j],&op2[j]);
        }
        
        scanf("%d", &n3);
        scanf("%c",&result[0]);
        for (int j = 0 ; j<n3; j++) {
            scanf("%c",&result[j]);
        }
        validatepos = 0;
        for  (int j = 0 ; j<n3; j++) {

            for (int k = 0; k < n1; k++) {
                if (j == 0) break;
                if (c1[k] == result[j] && c2[k] == result[j-1]) {
                    if (vcount[result[j-1]-'A']>0) vcount[result[j-1]-'A']--;
                    result[j-1]='.';
                    result[j] = c3[k];
                    break;
                }
                if (c1[k] == result[j-1] && c2[k] == result[j]) {
                    if (vcount[result[j-1]-'A']>0) vcount[result[j-1]-'A']--;
                    result[j-1]='.';
                    result[j] = c3[k];
                    break;
                }
            }
            for (int k = 0; k<n2; k++) {
                if (op1[k] == result[j]) {
                    if (vcount[op2[k]-'A'] > 0 ) {result[j]='.';   for (int ii = 0; ii<26; ii++){ vcount[ii]=0;} validatepos = j+1 ; break;}
                }
                if (op2[k] == result[j]) {
                    if (vcount[op1[k]-'A'] > 0 ) {result[j]='.'; for (int ii = 0; ii<26; ii++){vcount[ii]=0;} validatepos = j+1 ; break;}
                }
            }
           if(result[j] != '.') vcount[result[j]-'A']++;
        }
        firstdata = 0;
        printf("Case #%d: [",i);
        for (int k = validatepos; k<n3; k++) {
            if (result[k] == '.') continue;
            if (firstdata != 0) printf(", ");
            printf("%c",result[k]);
            firstdata = 1;
        }
        printf("]\n");
    }
 //   system("PAUSE");
    return EXIT_SUCCESS;
}
