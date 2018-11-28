#include<iostream.h>
#include<conio.h>
int count=0;
int main()
{
    int A,B;
    int t,n;

    int a,b,c;
     
    FILE *fr,*fw;
    fr = fopen("C-small-attempt1.in","r");
    fw= fopen("C-small-attempt1.out","w");
    fscanf(fr,"%d",&t);
    for(int i=1;i<=t;i++)
    {
            count=0;
           fscanf(fr,"%d",&A);
           
           fscanf(fr,"%d",&B);
           if(B==1000)
           B=999;
           for(int s=A;s<B;s++)
           {
            c=s%10;
            b=(s/10)%10;
            a=s/100;
            if(a==0)
            {
                if(b!=0)
                {
                n = c*10+b;
                if(n!=s)
                {
                 if(s<n&&n<=B)
                   count++;
                   }
                }    
                
           }    
           else 
           {
             n = b*100+c*10+a;
             if(n!=s)
             {
             if(s<n&&n<=B)
              count++;
              }
             n= c*100+a*10+b;
             if(n!=s)
             {
              if(s<n&&n<=B)
              count++;
              }
           }
                
         }
          fprintf(fw,"\nCase #%d: ",i);
          fprintf(fw,"%d",count);
           cout<<"count="<<count;  
    }
        
         
         fclose(fr);
         fclose(fw);
        
    getch();
    return 0;
           
    }
               
