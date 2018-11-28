#include <stdio.h>
#include <stdlib.h>
#include <math.h>


int T,N,K;
int *cases;

void CaseMAlloc()            //synarthsh gia thn apo8hkeush twn cases
{
	cases=(int*)malloc(T*sizeof(int));
}

    
int calculate()
{
    int x;
    
    if((K+1)%((int)pow(2,N))==0)
        x=1;
    else
        x=0;
    return x;
}
    
    
    

void printer()
{
     FILE*file;
     file=fopen("Output.txt","w");
     int helper;
     char *on="ON";
     char *off="OFF";
     
     for(helper=0;helper<T;helper++)
     {
         if(cases[helper]==0)
              fprintf(file,"Case #%d: %s\n",(helper+1),off);
         else
              fprintf(file,"Case #%d: %s\n",(helper+1),on);
     }
     fclose(file);
}




int main()
{
    char c;
    int i,j,k;

    
    FILE*file;
    file=fopen("A-large.in","r");
    
    fscanf(file,"%d",&T);               //eisodos apo to arxeio twn diastasewn
    fscanf(file,"%c",&c);

    CaseMAlloc();
    
    for(i=0;i<T;i++)
    {
        fscanf(file,"%d",&N);
        fscanf(file,"%c",&c); 
        fscanf(file,"%d",&K);
        fscanf(file,"%c",&c);   
        cases[i]=calculate();
    }
 
    fclose(file);                       //kleisimo arxeiou

    printer();
    return 0;
} 
