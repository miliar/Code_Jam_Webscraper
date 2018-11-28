#include <iostream>
#include <stdio.h>
#include <conio.h>
#include <vector>
#include <string>
#include <math.h>




using namespace std;

int _sort(int[],int);
int _sum(int,int);
int main()
{
    FILE *_i,*_o;
    int N;
    int t,ad[100],aa[100],bd[100],ba[100],na,nb;
    
    int hd,md,ha,ma;
    
    _i=fopen("bl.in","r");
    _o=fopen("train_l.out","w+");
  
    fscanf(_i,"%d",&N);

for(int k=1;k<=N;k++)
{for(int i=0;i<100;i++){aa[i]=ad[i]=ba[i]=bd[i]=2500;}
   fscanf(_i,"%d",&t);
   fscanf(_i,"%d %d",&na,&nb);
   for(int i=0;i<na;i++){
           fscanf(_i,"%d:%d %d:%d",&hd,&md,&ha,&ma);
           ad[i]=hd*100+md;
           ba[i]=ha*100+ma;
           }
           
   for(int i=0;i<nb;i++){
           fscanf(_i,"%d:%d %d:%d",&hd,&md,&ha,&ma);
           bd[i]=hd*100+md;
           aa[i]=ha*100+ma;
           }
      
           
   _sort(ad,na);
   _sort(aa,nb);
   _sort(bd,nb);
   _sort(ba,na);
   
   for(int i=0;i<na;i++)
   cout<<ad[i]<<" "<<ba[i]<<endl;

   for(int i=0;i<nb;i++)
   cout<<bd[i]<<" "<<aa[i]<<endl;   
   //check for A
   int j=0,a=0;
   for( int i=0;i<na;i++){
        
        if(ad[i]<_sum(aa[j],t))
            {a++;cout<<ad[i]<<" "<<_sum(aa[j],t)<<endl;}
        else
            j++;
            
            }
    //check for B
   int b=0;
   j=0;
   for( int i=0;i<nb;i++){
        cout<<_sum(ba[j],t)<<endl;
        if(bd[i]<_sum(ba[j],t))
            b++;
        else
            j++;  
            
            }    
    cout<<"case "<<k<<": "<<a<<" "<<b<<endl;        
   fprintf(_o,"Case #%d: %d %d",k,a,b);
   fprintf(_o,"\n");  
}   
fclose(_o);
fclose(_i);	
getche();
return 0;
}

int _sort(int a[],int n)
{int b;
  for(int i=0;i<n-1;i++)
     for(int j=i+1;j<n;j++)
        if(a[i]>a[j])
        {
          b=a[i];a[i]=a[j];a[j]=b;           
        }
         
  
 return 0;   
}
int _sum(int a,int b)
{int s;
 if(((a%100)+b) >=60)
  s=(((a/100)+1)*100)+((a%100)+b-60);
 else
  s=a+b;
    
 return s;   
}
