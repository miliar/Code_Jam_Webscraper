#include<stdio.h>
#include<stdlib.h>


int main(){
    FILE* in;
    FILE* out;
    char outp[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
    in=fopen("d:/input.in","r");
    out=fopen("d:/output.out","w");
    int n;
    char temp;
    fscanf(in,"%d\n",&n);
    for(int i=1;i<=n;i++){
        fprintf(out,"Case #%d: ",i);
        fscanf(in,"%c",&temp);
        while((temp>='a' && temp<='z') || temp==' ') {
            if(temp!=' ')
            fprintf(out,"%c",outp[temp-'a']);
            else fprintf(out,"%c",temp);
            fscanf(in,"%c",&temp);
        }
        fprintf(out,"\n");
    }
    
    
    //system("pause");    
}
