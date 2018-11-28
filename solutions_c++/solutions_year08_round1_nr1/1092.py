#include<iostream.h>
#include<cstdio>
#include<cmath>
#include<ctime>
#include<cstdlib>
#include<fstream.h>


#define PI 3.14159265

int main()

{
    fstream fin;
    int no_cases;
    fin.open("A-small-attempt0.in",ios::in);
    if(!fin)
    cout<<"error opening file";
    
    fin>>no_cases;
    
    for(int k=0;k<no_cases;k++)
    {
     int no_cor,i;
   
     fin>>no_cor;  
    int v1[no_cor],v2[no_cor];
    
    for(i=0;i<no_cor;i++)
    {
    
    fin>>v1[i];
    }
    
    for(i=0;i<no_cor;i++)
    {
    
    fin>>v2[i];
    }
    
    
    int max,index,temp;
    for(i=0;i<no_cor;i++)
    {
      max=v1[i]; 
      index=i;                  
      for(int j=i;j<no_cor;j++)
      {
              if(v1[j]>=max)
              {
                             
                             max=v1[j];
                             index=j;
              }
              
     }
     
     temp=v1[i];
     v1[i]=v1[index];
     v1[index]=temp;
     }
    
    
    
    
    
    
    int min;
    for(i=0;i<no_cor;i++)
    {
      min=v2[i]; 
      index=i;                  
      for(int j=i;j<no_cor;j++)
      {
              if(v2[j]<=min)
              {
                             
                             min=v2[j];
                             index=j;
              }
              
     }
     
     temp=v2[i];
     v2[i]=v2[index];
     v2[index]=temp;
     }
     
     
    
    
    int product=0;
        
     for(i=0;i<no_cor;i++)
    {
     product=product+v1[i]*v2[i];                     
                          
      }
      
      
      fstream fout;
      fout.open("A-smallout.txt",ios::out|ios::app);
      fout<<"Case #"<<k+1<<":"<<" "<<product<<endl;
      
      
      
         cout<<product<<endl;
  
    }
     
     getchar();
     return 0;

     }
                            
