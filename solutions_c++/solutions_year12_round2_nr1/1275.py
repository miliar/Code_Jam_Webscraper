#include <stdio.h>
#include <stdlib.h>
#include <conio.h>









//------------------------------------------------------------------------------
//------------------------------------------------------------------------------

int main()
{

FILE * f, * g;
f=fopen("A-large.in","r");
g=fopen("A-output.out","w");


int T,contor,suma,N,i,zero,cont;
float suma2;

int s[300];
float X,nr,p[300];

fscanf (f,"%d",&T); 

for (contor=1;contor<=T;contor++)
    {
    suma=0,zero=0,suma2=0,cont=0;
    
    fscanf(f,"%d",&N);
    printf("%d %d\n",contor,N);
    
    for (i=0;i<N;i++) 
        {
        fscanf(f,"%d",&s[i]);
        //printf("** %d",s[i]);
        
        suma=suma+s[i];
        if (s[i]==0) zero++;
        }     
    
    X=2.0*suma/N;
    
    //printf("\n%f %d\n\n",X,suma);

    
    fprintf(g,"Case #%d: ",contor);
    
    
    
    
    for (i=0;i<N;i++)
        {
        //if (zero==0) 
        p[i]=(X-s[i])*100.0/suma;
        
        //else if (zero!=0) 
          //      {
            //    if (s[i]!=0) nr=;
              //  else if (s[i]==0) nr=100.0/zero; //////////////////////////////
                //}
        
        //fprintf(g,"%f ",nr);       
        //printf("%f %d\n",p[i], s[i]);      
        }
        
    for (i=0;i<N;i++)
        {
        if (p[i]<0) {
                    suma2=suma2-p[i]; 
                    cont++;
                    
                    }
        }
        
        
    //printf("\nEMA %d %f \n", cont,suma2);
    
    while (cont!=0)
       {
       suma2=0;
       cont=0;
       
       for (i=0;i<N;i++)
            {
            if (p[i]<0) 
               {
               suma2=suma2-p[i]; 
               cont++;
               }
                    
            //printf("%f %d\n",p[i], s[i]);   
            }
            
       for (i=0;i<N;i++)
           {
           if (p[i]<0) p[i]=0;
           
           else p[i]=p[i]-(suma2/(N-cont));  
           }     
            
       }
        
        


    for (i=0;i<N;i++)
           {
           fprintf(g,"%f ",p[i]);   

           }
    
    fprintf(g,"\n"); 
    }

//getch();
return 0;
}


//------------------------------------------------------------------------------
//------------------------------------------------------------------------------





//------------------------------------------------------------------------------
//------------------------------------------------------------------------------





//------------------------------------------------------------------------------
//------------------------------------------------------------------------------
