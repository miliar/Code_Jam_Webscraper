#include <iostream>
#include <conio.h>
#include <string>
#include <math.h>

using namespace std;

int sortarry(int[],int);
int add(int,int);
int main()
{//declare files
    FILE *infile,*outfile;
    int N;
    int t,ad[100],aa[100],bd[100],ba[100],na,nb;
    
    int hd,md,ha,ma;
  //open file  
    infile=fopen("sbl.in","r");
    outfile=fopen("train_l.out","w+");
  
    fscanf(infile,"%d",&N);

for(int k=1;k<=N;k++)
{for(int i=0;i<100;i++){aa[i]=ad[i]=ba[i]=bd[i]=2500;}
   fscanf(infile,"%d",&t);
   fscanf(infile,"%d %d",&na,&nb);
   for(int i=0;i<na;i++){
           fscanf(infile,"%d:%d %d:%d",&hd,&md,&ha,&ma);
           ad[i]=hd*100+md;
           ba[i]=ha*100+ma;
           }
           
   for(int i=0;i<nb;i++){
           fscanf(infile,"%d:%d %d:%d",&hd,&md,&ha,&ma);
           bd[i]=hd*100+md;
           aa[i]=ha*100+ma;
           }
      
           
   sortarry(ad,na);
   sortarry(aa,nb);
   sortarry(bd,nb);
   sortarry(ba,na);
   
   for(int i=0;i<na;i++)
   cout<<ad[i]<<" "<<ba[i]<<endl;

   for(int i=0;i<nb;i++)
   cout<<bd[i]<<" "<<aa[i]<<endl;   
   //check for A
   int j=0,a=0;
   for( int i=0;i<na;i++){
        
        if(ad[i]<add(aa[j],t))
            {a++;cout<<ad[i]<<" "<<add(aa[j],t)<<endl;}
        else
            j++;
            
            }
    //check for B
   int b=0;
   j=0;
   for( int i=0;i<nb;i++){
        cout<<add(ba[j],t)<<endl;
        if(bd[i]<add(ba[j],t))
            b++;
        else
            j++;  
            
            }    
    cout<<"case "<<k<<": "<<a<<" "<<b<<endl;        
   fprintf(outfile,"Case #%d: %d %d",k,a,b);
   fprintf(outfile,"\n");  
}   
fclose(outfile);
fclose(infile);	
getche();
return 0;
}

int sortarry(int a[],int n)
{int b;
  for(int i=0;i<n-1;i++)
     for(int j=i+1;j<n;j++)
        if(a[i]>a[j])
        {
          b=a[i];a[i]=a[j];a[j]=b;           
        }
         
  
 return 0;   
}
int add(int a,int b)
{int s;
 if(((a%100)+b) >=60)
  s=(((a/100)+1)*100)+((a%100)+b-60);
 else
  s=a+b;
    
 return s;   
}
