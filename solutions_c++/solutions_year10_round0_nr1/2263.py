#include <stdio.h>
#include <stdlib.h>

#define INFILENAME "as.in"
#define OUTFILENAME "as.out"

class Data{
public:
    int device;
    int snap;
};

class Env{
public:
    int testcase;
    Data *data;
    char *inname, *outname;

    int init(char *, char *);
    int exec();
};

int Env::init(char *in, char *out){
    FILE *fin;

    inname = in;
    outname = out;

    fin = fopen(inname,"r");
    if(fin == NULL){
        printf("cant open\n");
        return 0;
    }

    fscanf(fin, "%d\n", &testcase);
    data = new Data[testcase];
    for(int i=0;i<testcase;i++){
        fscanf(fin, "%d %d\n", &data[i].device, &data[i].snap);
    }
    
    fclose(fin);
}

int Env::exec(){
    FILE *fout;
    int n, k;
    int tmp;

    fout = fopen(outname, "w");
    if(fout == NULL){
        printf("cant open\n");
        return 0;
    }

    for(int i=0;i<testcase;i++){
        n = data[i].device;
        k = data[i].snap;
        
        tmp = 2 << (n-1);
        if( (k % tmp) == (tmp -1)){
            fprintf(fout, "Case #%d: ON\n", i+1);
        }else{
            fprintf(fout, "Case #%d: OFF\n", i+1);
        }
        
    }
}

int main(void){
    
    Env *env;
    env = new Env;
    env->init((char *)INFILENAME, (char *)OUTFILENAME);
    env->exec();
    return 0;
}
