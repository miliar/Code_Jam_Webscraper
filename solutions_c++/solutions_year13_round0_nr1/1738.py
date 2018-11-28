#include <stdio.h>
#include <stdlib.h>
#include <conio.h>


//------------------------------------------------------------------------------
//------------------------------------------------------------------------------

int main()
{

FILE * f, * g;
f=fopen("A-large.in","r");
g=fopen("OUT.out","w");
int T,contor;

int i,j,t_i,t_j;
int a[10][10],suma;
char temp,trash;
bool t_flag,win,winX,winO,completed;


fscanf (f,"%d",&T); 
fscanf(f,"%c",&trash);

for (contor=1;contor<=T;contor++)
    {
    
    t_i=-1;t_j=-1;t_flag=false;completed=true;win=false,winX=false,winO=false;
    
    for (i=0;i<4;i++)
        {
        for (j=0;j<4;j++)
            {
            fscanf(f,"%c",&temp);
            
            if (temp=='X') a[i][j]=1;
            else if (temp=='O') a[i][j]=-1;
            else if (temp=='.') 
                 {
                 a[i][j]=0;
                 completed=false;
                 }
            else 
                 {
                 a[i][j]=1;
                 t_i=i;
                 t_j=j;
                 t_flag=true;
                 }
            }
        fscanf(f,"%c",&trash);        
        }
    fscanf(f,"%c",&trash);
    
    for (i=0;i<4;i++)
        {
        suma=0;
        for (j=0;j<4;j++)
            {
            suma+=a[i][j];
            }
        if (suma==4 || suma==-4)
           {
           win=true;
           break;         
           }
        }
    
    if (win==false)
        {
        for (j=0;j<4;j++)
            {
            suma=0;
            for (i=0;i<4;i++)
                {
                suma+=a[i][j];
                }
            if (suma==4 || suma==-4)
               {
               win=true;
               break;        
               }
            }
        }
        
    
    if (win==false)
        {
        suma=0;
        for (i=0;i<4;i++)
            {
            suma+=a[i][i];
            }
        if (suma==4 || suma==-4)
               {
               win=true;        
               }
        }
        
    
    if (win==false)
        {
        suma=0;
        for (i=0;i<4;i++)
            {
            suma+=a[i][3-i];
            }
        if (suma==4 || suma==-4)
               {
               win=true;         
               }
        }
    
    if (win==false && t_flag==true)
       {
       a[t_i][t_j]=-1;            
       
       for (i=0;i<4;i++)
        {
        suma=0;
        for (j=0;j<4;j++)
            {
            suma+=a[i][j];
            }
        if (suma==4 || suma==-4)
           {
           win=true;     
           break;    
           }
        }
    
    if (win==false)
        {
        for (j=0;j<4;j++)
            {
            suma=0;
            for (i=0;i<4;i++)
                {
                suma+=a[i][j];
                }
            if (suma==4 || suma==-4)
               {
               win=true;  
               break;       
               }
            }
        }
        
    
    if (win==false)
        {
        suma=0;
        for (i=0;i<4;i++)
            {
            suma+=a[i][i];
            }
        if (suma==4 || suma==-4)
               {
               win=true;         
               }
        }
        
    
    if (win==false)
        {
        suma=0;
        for (i=0;i<4;i++)
            {
            suma+=a[i][3-i];
            }
        if (suma==4 || suma==-4)
               {
               win=true;         
               }
        }            
         
       }

     
    
    fprintf(g,"Case #%d: ",contor);
    
    if (suma==4) fprintf(g,"X won");
    else if (suma==-4) fprintf(g,"O won");
    else if (completed==true) fprintf(g,"Draw");
    else fprintf(g,"Game has not completed");
    
    if (contor<T) fprintf(g,"\n");  
    
    
    
    
    }

return 0;
}


//------------------------------------------------------------------------------
//------------------------------------------------------------------------------





//------------------------------------------------------------------------------
//------------------------------------------------------------------------------





//------------------------------------------------------------------------------
//------------------------------------------------------------------------------
