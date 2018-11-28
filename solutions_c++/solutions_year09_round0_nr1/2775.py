#include <stdio.h>
#include <string.h>

char **kamus;
int *mark,*cek;

int main () {
    int L,D,N,i,j,k,x,counter,nword;
    char input[1000];
    
    scanf("%d %d %d",&L,&D,&N);
    
    kamus = new char*[D];
    mark = new int[D];
    cek = new int[D];
    
    for(i=0;i<D;i++) {
         kamus[i] = new char[L+3];
         scanf("%s",kamus[i]);
    }
    
    for(counter = 1;counter<=N;counter++) {
         nword = 0;
         for(i=0;i<D;i++) {
            mark[i]=1;
         }
         scanf("%s",input);
         j = L;
         i=0;
         k=0;
         while (j>0) {
            if(input[i]=='(') {
               i++;
               for(x=0;x<D;x++) cek[x] = 0;
               while(input[i]!=')'){
                  for(x=0;x<D;x++) {
                     if(cek[x]!= 1 && input[i] == kamus[x][k])  cek[x] = 1;      
                  }
                  i++;
               }
               for(x=0;x<D;x++) {
                  if(mark[x]!=0) mark[x] = cek[x];
               }
            } else {
               for(x=0;x<D;x++) {
                  if(input[i] != kamus[x][k]) mark[x] = 0;
               }
            }
            i++;
            k++;
            j--;
         }
         for(i=0;i<D;i++) nword+=mark[i];
         printf ("Case #%d: %d\n",counter,nword);
    }
    
    while(getchar()!=EOF);
    return 0;
}
