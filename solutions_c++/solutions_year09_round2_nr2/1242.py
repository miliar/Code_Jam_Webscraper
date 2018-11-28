 #include <iostream>
 #include <vector>
 #include <algorithm>
 #include <stdio.h>
 //i generate eache one and after this i look in the files and I choose;
 //using namespace std;
 FILE *f,*g;
 
 int T;
 int okk;
 char v[30];    
 int lungime;
 char aux;
 /*void ordonare(int pozitie)
 {
       for( int i = pozitie; i< lungime; i++)
            {
                for (int j = i + 1; j < lungime; j++)
                {
                    if (v[i] > v[j])
                    {
                        char auxx = v[i];
                        v[i] = v[j];
                        v[j] = auxx;
                    }
                }
            }
      
      }
 */
 
 int  gasit=0;  
     int poz=0 ;
     int poznou;
 
 int main() {
     f=fopen("date.in","r");
     g=fopen("date.out","w");

 fscanf(f,"%d \n",&T);
int i;
char max;
v[0]=0;
for(int y=1;y<=T;y++)
        {okk=1;
        i=1;
        while(okk)
                  {fscanf(f,"%c",&v[i]);
                   if(v[i]=='\n') okk=0;
                   else i++;
                             }
            lungime=i-1;                
      //   for(i=1;i<=lungime;i++)
      //   fprintf(g,"%c",v[i]); 
     gasit=0;  
     poz=0 ;
     poznou;
     char min;
         for(i=lungime;i>1;i--)
                       if(v[i]>v[i-1])  {gasit=1;poz=i-1;i=0;}                                         
         if(gasit==1) 
                      {max=100;
                      for(i=poz+1;i<=lungime;i++)
                                                  if(v[i]<max&&v[i]>v[poz]){ max=v[i];poznou=i;}
                      aux=v[poznou];
                      v[poznou]=v[poz];
                      v[poz]=aux;
                 poz++;
                     for(i=poz;i<=lungime;i++)
                                          for(int j=i+1;j<=lungime;j++)
                                          if(v[i]>v[j])
                                                 {     aux=v[i];
                                                      v[i]=v[j];
                                                        v[j]=aux;
                                                       }     
                
            

                                        }
         else 
              {min=100;
              for(i=1;i<=lungime;i++)
              if(v[i]<min&&v[i]!='0') {min=v[i];poz=i;}
              aux=v[poz];
                      v[poz]=v[1];
                      v[1]=aux;
                for(i=lungime;i>1;i--)  
                 v[i+1]=v[i]  ;
                 v[2]=0;
                 lungime++;
                 poz=3;
                     for(i=poz;i<=lungime;i++)
                                          for(int j=i+1;j<=lungime;j++)
                                          if(v[i]>v[j])
                                                 {     aux=v[i];
                                                      v[i]=v[j];
                                                        v[j]=aux;
                                                       }
                 }
                 fprintf(g,"Case #%d: ",y); 
           for(i=1;i<=lungime;i++)
          if(v[i]>'9'||v[i]<'0')fprintf(g,"0");
           else fprintf(g,"%c",v[i]); 
         
           fprintf(g,"\n");           
           }
                     
                     
                     
                     

 
 
  return 0;
 }
