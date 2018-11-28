#include <stdio.h>
#include <string.h>


int masc[2000], o4er[2000], N, kol, kol2, rez, k, i, j;
char serv[110][110], ins[2000];
int main()
{

    scanf("%d\n", &N);
    for(k = 0; k < N; k++) {
        scanf("%d\n", &kol);
        for(i = 0; i < kol; i++) {
                gets(serv[i]);
                o4er[i] = 1;
        }
        o4er[1999] = kol;                
        scanf("%d\n", &kol2);
        for(i = 0; i < kol2; i++) {
                gets(ins);
                for(j = 0; j < kol; j++)
					if(!strcmp(ins, serv[j])) {
                      masc[i] = j; 
					  break;
					}   
		}		
     for (i = 0; i < kol2; ++i) {
             if (o4er[masc[i]]) {
                    o4er[masc[i]] = 0;
                    --o4er[1999];
                    if (o4er[1999] == 0) {
                         o4er[1999] = kol - 1;
                         rez++;
                         for (j = 0; j < kol; ++j) o4er[j] = 1;
                         o4er[masc[i]] = 0;
                    }
             }
        
      }                 
      printf("Case #%d: %d\n", k + 1, rez);
      rez = 0; 
   }          
    return 0;
}