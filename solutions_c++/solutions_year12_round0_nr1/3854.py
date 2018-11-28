#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
FILE *fout;
FILE *fin;

int main(){
    int totVals;
    fin=fopen("helpdecodein.txt","r");
    fout=fopen("helpdecodeout.txt","w");
    char encoded[2000]="ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
    char decoded[2000]="our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
    char map[26];
    for(int i=0;i<strlen(encoded);i++){
        int a=(int)(encoded[i]-97);
        map[a]=decoded[i];
    }
    map[16]=(char)122;
    map[25]=(char)113;
    char store[150];
    fscanf(fin,"%d",&totVals);
    fgets(store,200,fin);
    for(int i=0;i<totVals;i++){
        fprintf(fout,"Case #%d: ",i+1);
        fgets(store,200,fin);
        for(int j=0;j<strlen(store)-1;j++){
            if(store[j]<97||store[j]>122){
                fprintf(fout,"%c",store[j]);
            }
            else{
                fprintf(fout,"%c",map[(int)(store[j]-97)]);
            }
        }
        fprintf(fout,"\n");
    }
}
    
