#include <stdio.h>
#include <stdlib.h>
#include <conio.h>


int nr_cifre(int);

int cifre_distincte(int,int);

int pow10(int);

int recycle(int,int);

int combinari(int);

int check(int,int);


int main()
{

FILE * f, * g;
f=fopen("C-large.in","r");
g=fopen("output.out","w");


int T,min,max,i,j,x,n,nrc,ch,p10,total=0,partial=0,fals=0;

fscanf (f,"%d",&T); 

for (i=1;i<=T;i++)
    {
    total=0;
    
    fscanf(f,"%d",&min);     
    
    fscanf(f,"%d",&max);         
    
    for (x=min;x<=max;x++)
        {
        partial=0;
        fals=0;
        n=x;

        nrc=nr_cifre(n);
        
        if (cifre_distincte(n,nrc)==1)
           {
           for (j=1;j<nrc;j++)
               {
               p10=pow10(nrc);      
               n=recycle(n,p10);
               if (n<=max && n>=min && n!=x) { 
                                             partial++;
                                             if (n<x) fals=1;
                                             }     
               } 
           
           if (nrc==4 || nrc==6) {
                                     ch=check(x,nrc);
                                     partial=partial/ch;
                                     }
           }         
         
        if (fals==1) partial=0;   
        
        if (partial>0) 
           {
           partial++; 
           partial=combinari(partial); 
           total=total+partial; 
           }
        }
    
    fprintf(g,"Case #%d: %d \n",i,total);
    }
    
return 0;
}





int check(int n, int nrc)
{    

if (nrc==4 && n%101==0) return 2;   
if (nrc==6 && n%10101==0) return 3;
if (nrc==6 && n%1001==0) return 2;

return 1;
}





int combinari(int n)
{
int r;

r=(n-1)*n/2;

return r;
    
}





int pow10(int p){

int i,r=1;

for (i=1;i<p;i++) r=r*10;     
    
return r;
}





int recycle(int n,int power){

int c;

c=n/power;

n=(n%power)*10+c;
    
return n;
} 





int cifre_distincte(int x, int n){
    
switch (n)
       {
       case 1: return 0;       
       case 2: if (x%11==0) return 0;
               else return 1;
       case 3: if (x%111==0) return 0;
               else return 1;
       case 4: if (x%1111==0) return 0;
               else return 1;
       case 5: if (x%11111==0) return 0;
               else return 1;
       case 6: if (x%111111==0) return 0;
               else return 1;
       case 7: if (x%1111111==0) return 0;
               else return 1;
       }    
    
}





int nr_cifre(int x){

int i=0;

if (x==0) return 1;

while(x>0)             
     {
     x=x/10;                  
     i++;
     }        
return i;
}
