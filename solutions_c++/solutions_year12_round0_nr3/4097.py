#include<stdio.h>
#include<conio.h>

int main()
{    int pair;
int a,c,d,out,ctr=0;
    scanf("%d",&a);
    
    while(a--)
    {         
              ctr++;
              scanf("%d %d",&c,&d);
              pair=f(c,d);
              printf("Case #%d: %d",ctr,pair);
              
              
    }
    getch();
}

int f(int c,int d)
{   int e,f,g,h,i,j,k,l,pair;
    pair=0;
    if(c<10)
    { pair=0;
     return pair;  }
    else if(c<100&&c>=10)
    {  pair=0;
    //for(i=c;i<=d;i++)
    while(c<=d)
    {
           e=(int)c%10;
           f=(int)c/10;
           g=(10*e+f);
           if((g<=d)&&(g>c))
           {++pair;
           }
           c++;
    }
     return pair;  
    }
    else 
    { pair=0;
             //for(i=c;i<=d;i++)
             while(c<=d)
    {
           e=(c%10);
           f=(int)c/10;
           g=(f%10);
           h=(int)f/10;
           j=(100*e+10*h+g);
           l=(100*g+10*e+h);
           if((j<=d)&&(j>c))
           {++pair;
           }
            if((l<=d)&&(l>c))
           {++pair;
           }
           c++;
    }
     return pair;  
    }      
    
}
    
        
             
              
