 #include <iostream>
 #include <vector>
 #include <algorithm>
 #include <stdio.h>
 //i generate eache one and after this i look in the files and I choose;
 //using namespace std;
 FILE *f,*g;
 char v[100];
 int T;
 double v2[100];
 
long int convfrom(int x,int nr[],int lung)
  {long int putere=1;
  long int numar=0;
  for(int i=1;i<=lung;i++)
          {numar+=nr[i]*putere;
          putere=putere*x;
                         }
      
    return numar;  }
     
 
 
 
 
 
 
 int main() {
     f=fopen("date.in","r");
     g=fopen("date.out","w");
int okk;
int lungime;
 fscanf(f,"%d \n",&T);
int contor;
int i;
long int nr;
for(int y=1;y<=T;y++)
        {okk=1;
        i=1;
        while(okk)
                  {fscanf(f,"%c",&v[i]);
                  
                   if(v[i]=='\n') okk=0;
                   else i++;
                             }
            lungime=i-1;                
      
      contor=1;
                             char aux=v[1];
                             v[1]=1;
                             for(i=2;i<=lungime;i++)
                             if(v[i]==aux) v[i]=1;
      
        
        okk=1;
        int poz=2;
        while(okk)
        if(v[poz]==1) poz++;
        else okk=0;
        aux=v[poz];
                 if(poz<=lungime){
                             v[poz]=0;
                             for(i=poz;i<=lungime;i++)
                             if(v[i]==aux) v[i]=0;}
          contor=2;
          
          for(i=poz;i<=lungime;i++)
                      { if(v[i]>=contor)   
                                        {aux=v[i];
                                        v[i]=contor;
                                        for(int j=i+1;j<=lungime;j++)
                                         if(v[j]==aux) v[j]=contor;
                                          contor++;        
                                                  }  
                         }                           
            for(i=1;i<=lungime;i++)
            v2[i]=v[i];
           //nr= convfrom(contor, v2,lungime);                             
       double putere=1;
        double numar=0;
       double contor2=contor;
      for(int i=lungime;i>=1;i--)
          {numar+=v2[i]*putere;
           putere=putere*contor2;}
                         
      
      
      
      
                 fprintf(g,"Case #%d: %.0lf \n",y,numar); 
          
                  
          
           /*for(i=1;i<=lungime;i++)
           fprintf(g,"%c",v[i]); 
         
           fprintf(g,"\n");    */       
           }
                     
                     
                     
                     

 
 
  return 0;
 }
