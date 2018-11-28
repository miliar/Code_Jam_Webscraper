#include <stdio.h>
#include <stdlib.h>
#include <math.h>


int C,N;
int*in,*cases,*great;



int gcd(int a,int b)
{
    int i,j;
    i=a; j=b;
    while (i>0 && j>0)
          if (i>j) i=i%j ;
          else j=j%i;
    return i+j;
}


/////////////////MALLOCS//////////////////
void mallocgreat()
{
    great=(int*)malloc(N*(N-1)/2*sizeof(int));
}

void mallocin()
{
    in=(int*)malloc(N*sizeof(int));
}


void CaseMAlloc()
{
	cases=(int*)malloc(C*sizeof(int));
}

/////////////END OF MALLOCS///////////////



void makeGreat()
{
     int cnt=0;
     int i,j;
     for(i=0;i<N-1;i++)
        for(j=i+1;j<N;j++)
        {
            great[cnt]=abs(in[i]-in[j]);
            cnt++;
        }
}

int findT()
{
     int T=gcd(great[0],great[0]);
     int i;
     for(i=1;i<(N-1)*N/2;i++)
         T=gcd(T,great[i]);
     return T;
}
     
int findY(int bound)
{
    int i=0;
    while(bound*i<in[0]) i++;
    return bound*i-in[0];
}






void printer()
{
     FILE*file;
     file=fopen("Output.txt","w");
     int helper;

     for(helper=0;helper<C;helper++)
         fprintf(file,"Case #%d: %d\n",(helper+1),cases[helper]);

     fclose(file);
}




int main()
{
    char c;
    int i,j;
    int T;


    
    FILE*file;
    file=fopen("B-small-attempt0.in","r");
    
    fscanf(file,"%d",&C);               //eisodos apo to arxeio twn diastasewn
    fscanf(file,"%c",&c);
    CaseMAlloc();
    
    
    for(i=0;i<C;i++)
    {
        fscanf(file,"%d",&N);
        fscanf(file,"%c",&c); 
        
        mallocin();
        mallocgreat();
        
        for(j=0;j<N;j++)
        {
            fscanf(file,"%d",&(in[j]));
            fscanf(file,"%c",&c);
        }
        makeGreat();
        T=findT();
        printf("%d\n",T);
        cases[i]=findY(T);
    }
 
    fclose(file);                       //kleisimo arxeiou

    printer();
    system("pause");
    return 0;
} 










