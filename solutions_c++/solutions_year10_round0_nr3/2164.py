#include <stdio.h>
#include <stdlib.h>
#include <math.h>


int T,N,k,R;
int *cases;
int *groups;



void CaseMAlloc()            //synarthsh gia thn apo8hkeush twn cases
{
	cases=(int*)malloc(T*sizeof(int));
}



void mallocgroups()
{
    groups=(int*)malloc(N*sizeof(int));
}



void printer()
{
     FILE*file;
     file=fopen("Output.txt","w");
     int helper;

     for(helper=0;helper<T;helper++)
         fprintf(file,"Case #%d: %d\n",(helper+1),cases[helper]);

     fclose(file);
}

int incri(int i)
{
    if(i<N-1)
        return (i+1);
    else
        return 0;
}

int calculate()
{
    int j,i,whole,start,a,sum;
    
    whole=0;
    i=0;

    
    for(j=0;j<R;j++)
    {
        sum=0;
        start=i;
        for(;;)
        {
             a=sum+groups[i];
             if(a<=k)
             {
                  sum+=groups[i];
                  i=incri(i);
             }
             else
                  break;
             if(i==start) break;
        }
        whole+=sum;
    }

    return whole;
}
             
        


int main()
{
    char c;
    int i,j;

    
    FILE*file;
    file=fopen("C-small-attempt2.in","r");
    
    fscanf(file,"%d",&T);               //eisodos apo to arxeio twn diastasewn
    fscanf(file,"%c",&c);
    CaseMAlloc();
    
    
    for(i=0;i<T;i++)
    {
        fscanf(file,"%d",&R);
        fscanf(file,"%c",&c); 
        fscanf(file,"%d",&k);
        fscanf(file,"%c",&c);   
        fscanf(file,"%d",&N);
        fscanf(file,"%c",&c);
        
        mallocgroups();
        for(j=0;j<N;j++)
        {
            fscanf(file,"%d",&(groups[j]));
            fscanf(file,"%c",&c);
        }
        cases[i]=calculate();

    }
 
    fclose(file);                       //kleisimo arxeiou

    printer();
    return 0;
} 
