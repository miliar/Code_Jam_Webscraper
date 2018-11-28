#include <stdio.h>
#include <string.h>
#include <time.h>

char* scanfar(FILE *stream,char* str) {
    int c=0;
    int count=0;    
    do {
        c=fgetc(stream);
        str[count]=c;
        count++;
    }
    while(c!='\n' && c!=EOF);
    str[count-1]='\0';
    return str;
}
        
        


main ()
{
    FILE *fin  = fopen ("A-small.in", "r");
    FILE *fout = fopen ("A-small.out", "w");
    int n,i,j,k;
    fscanf(fin,"%d",&n);
    for(i=1;i<=n;i++) {
        int changes=0;
        int seng;
        fscanf(fin,"%d",&seng);
        fgetc(fin);
        char names[seng][200];
        int check[seng];
        for(j=0;j<seng;j++) {
            check[j]=0;
        }
        int checker=0;
        for(j=0;j<seng;j++) {
            scanfar(fin,names[j]);
            }
        int num;
        fscanf(fin,"%d",&num);
        fgetc(fin);
        for(j=1;j<=num;j++) {
            char name[200];
            scanfar(fin,name);
            k=0;            
            while(strcmp(names[k],name)!=0) {
                k++;
            }             
            if (check[k]==0) {
                check[k]=1;
                checker++;
                if (checker==seng) {
                    changes++;
                    checker=1;
                    int cucu=k;
                    for(k=0;k<=seng;k++) {
                        check[k]=0;
                    }
                    check[cucu]=1;
                }
            }
        }
        fprintf(fout, "Case #%d: %d\n", i, changes);
    }
}
                        
            
        
            
        
        
