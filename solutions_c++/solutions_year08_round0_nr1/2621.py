#include<stdio.h>
#include<stdlib.h>
#include<string.h>

FILE *fin, *fout;

typedef struct search{
        char name[101];
        bool taken;
};
/*
int compare(const void* p1, const void* p2){
    search* e1= (search*) p1;
    search* e2= (search*) p2;
    return e1->count - e2->count;
} */
int main(){
    fin = fopen("saveUniv.in","r");
    fout = fopen("saveUniv.out","w");
    int testNum=0;
    fscanf(fin,"%d\n",&testNum);
    int counter = 0;
    int s,q;
    int i,j;
    char tempChar;
    search engine[100];
    char temp[100];
//    char query[1000][100];
    int index;
    int all;
    int switches=0;
    for( counter = 0 ; counter < testNum ; counter ++)
    {
        switches=0;
         fscanf(fin,"%d\n",&s);
         all=s;
         for(i = 0 ; i < s ; i ++)
         {
             index=0;
             engine[i].taken = false;
             fscanf(fin,"%c",&tempChar);
             while(tempChar != '\n'){
                   engine[i].name[index++]=tempChar;
                   fscanf(fin,"%c",&tempChar);
             }
             engine[i].name[index]='\0';
         }
         fscanf(fin,"%d\n",&q);
         for( j = 0 ; j < q ; j ++){
              index = 0;
              fscanf(fin,"%c",&tempChar);
              while(tempChar != '\n'){
                    temp[index++]=tempChar;
                    fscanf(fin,"%c",&tempChar);
              }
              temp[index]='\0';
              for( i = 0 ; i < s ; i ++){
                   if(strcmp(temp,engine[i].name)==0 && !engine[i].taken){
                      engine[i].taken = true;
                      all--;
                      if( all == 0){
                          all = i ;
                          for( i = 0 ; i < s ; i ++)
                               engine[i].taken = false;
                          engine[all].taken = true;
                          all = s-1;
                          switches++;
                      }
                   }
              }
         }
    //     qsort(engine,s,sizeof(search),compare);
       fprintf(fout,"Case #%d: %d\n",counter+1,switches);
         /*
         for( j = 0 ; j < q ; j ++)
         {
              index=0;
              fscanf(fin,"%c",&tempChar);
              while(tempChar != '\n'){
                    query[j][index++] = tempChar;
                    fscanf(fin,"%c",&tempChar);
              }
         }
         */
    }
    fclose(fin);
    fclose(fout);
    return 0;
}
