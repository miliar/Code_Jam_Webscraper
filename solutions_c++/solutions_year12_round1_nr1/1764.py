#include <stdio.h>
#include <stdlib.h>
#include <conio.h>


void fa(int **,int ,int );
void faf(float **,int ,int );






//------------------------------------------------------------------------------
//------------------------------------------------------------------------------

int main()
{

FILE * f, * g;
f=fopen("A-small-attempt0.in","r");
//f=fopen("ema.in","r");
g=fopen("A-output.out","w");


int T,A,B,contor,i,j,doi,poz;

float total;

float p[100]; //schimb

fscanf (f,"%d",&T); 

for (contor=1;contor<=T;contor++)
    {
    total=0;
    
    fscanf(f,"%d",&A);
    fscanf(f,"%d",&B);
    
    
    
    
    
    for (i=1;i<=A;i++)
        {
        fscanf(f,"%f",&p[i]);
        printf("\n%f \n\n\n",p[i]);
        }
        
    int col=100,lin=100; //schimb!!!!!!!!!!!!!
    int **s;
    s=(int**)malloc(lin * sizeof(int*));

    for (i=0;i<=lin;i++)
        s[i]=(int*)malloc(col * sizeof(int));
    
    
    
    
    
    
    s[1][1]=0;    
    s[2][1]=1;
    
    doi=2;
    poz=2;
    int fin=2;

    while (poz<=A)
          {
          
          for (i=1;i<=doi;i++) //linii
              {
              fin++;
              s[i][poz]=0;
              s[i+doi][poz]=1;
              for (j=1;j<poz;j++)
                  s[i+doi][j]=s[i][j];
              }        
          
          doi=2*doi;
          poz++;
          
          }
   
    fa(s,fin,A);
    
    printf("\n%d %d\n\n\n",A,B);
    
    
    /*
    float **a;
    a=(float**)malloc(lin * sizeof(float*));

    for (i=0;i<=lin;i++)
        a[i]=(float*)malloc(col * sizeof(float));
    */
    
    float a[100];




    
    for (i=1;i<=fin;i++)
        {
        a[i]=1.0;
        
        for (j=1;j<=A;j++)
            {
            if (s[i][j]==0)
               a[i]=a[i]*(1-p[j]);             
            else               
               a[i]=a[i]*(p[j]);                
            }
        
        printf(" %f ",a[i]);
        }
    
    printf(" \n\n");
    
    //f(a,fin,A);

/*
    printf("\n\n\na ");
    for (i=1;i<=fin;i++)
        {
         printf("%f ",p[i]);               
               
                        
        }
printf("\n\n\n ");
*/
    
    
    int **t;
    t=(int**)malloc(lin * sizeof(int*));

    for (i=0;i<=lin;i++)
        t[i]=(int*)malloc(col * sizeof(int));

    
    int start;
    
    for (i=1;i<=fin;i++)
        {
        start=A+1;
        
        //type         
               
        
        for (j=1;j<=A;j++) 
            if (s[i][j]==0)
               {
               start=j;
               break;
               }
                 
        if (start>A)
           t[1][i]=B-A+1;
        else 
           t[1][i]=2*B-A+2;
           
        //bksp
        
        for (j=1;j<=A;j++)
            {
            if (A-j<start) //sterg bine
               t[j+2][i]=B-A+2*j+1;   //bk-2
            else 
               t[j+2][i]=B*2-A+2*j+2;              
            
            }
        
        
        //enter
        
        t[2][i]=2+B;    
                        
        }

    fa(t,A+2,fin);
    
    
    float ex[100];//schimb
    
    
    for (i=1;i<=A+2;i++)
        {
         ex[i]=0;               
         
         for (j=1;j<=fin;j++)
             {
             ex[i]=ex[i]+ a[j]*t[i][j] ;                
             }               
                        
        }
    
    printf("\n\n\nex ");
    for (i=1;i<=A+2;i++)
        {
         printf("%f ",ex[i]);               
               
                        
        }
    
    int min=1;
    
    for (i=2;i<A+2;i++)
        if (ex[i]<ex[min]) min=i;
        
    total=ex[min];
    
    printf("Case #%d: %f \n",contor,total);
    
    fprintf(g,"Case #%d: %f \n",contor,total);
    }

getch();
return 0;
}


//------------------------------------------------------------------------------
//------------------------------------------------------------------------------





//------------------------------------------------------------------------------
//------------------------------------------------------------------------------


void fa(int **a,int lin,int col){

int i,j;
     
for (i=1;i<=lin;i++)
    {
    for (j=1;j<=col;j++)
        printf("%d ",a[i][j]);  
    printf("\n"); 
    } 
printf("\n\n");
}


//------------------------------------------------------------------------------
//------------------------------------------------------------------------------


void faf(float **a,int lin,int col){

int i,j;
     
for (i=1;i<=lin;i++)
    {
    for (j=1;j<=col;j++)
        printf("%f\t",a[i][j]);  
    printf("\n"); 
    } 
printf("\n\n");
}
