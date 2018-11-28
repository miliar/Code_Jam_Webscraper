#include<iostream>
#define MAX 100
using namespace std;
char N[MAX][MAX];
double WP[MAX];
double OWP[MAX];
double OOWP[MAX];
string temp;
int n;
double sum=0,ts;
int times=0,tt;
int T;
int main()
{
cin>>T;
for(int q=0;q<T;q++)
{
    cin>>n;
    for(int i=0;i<n;i++)
    {
     cin>>temp;      
     sum=times=0;
     for(int j=0;j<temp.size();j++)
      {
        if(temp[j]=='1') sum++;
        if(temp[j]!='.') times++;
        N[i][j]=temp[j];
      }
        if(times==0)
        WP[i]=0;
        else
        WP[i]=sum/times;
    }    

for(int i=0;i<n;i++)
{
 ts=tt=0; 
 for(int j=0;j<n;j++)
 {
  if(N[i][j]!='.')
  {
   sum=times=0;
   for(int k=0;k<n;k++)
   { 
     if(N[j][k]=='1' && k!=i) sum++;
     if(N[j][k]!='.' && k!=i) times++;
   }

   ts+=sum/times;;
   tt++;
  }
 }
 if(tt==0)
 OWP[i]=0;
 else
 OWP[i]=ts/tt;
}



for(int i=0;i<n;i++)
{
 sum=times=0;
 for(int j=0;j<n;j++)
 {
  if(N[i][j]!='.' && i!=j)
  {
   sum+=OWP[j];     
   times++;         
  }        
 }        
        if(times==0)
        OOWP[i]=0;
        else
   OOWP[i]=sum/times;       
}

 cout<<"Case #"<<q+1<<":"<<endl;
 cout.precision(12);
for(int i=0;i<n;i++)
 cout<<0.25*WP[i]+0.50*OWP[i]+0.25*OOWP[i]<<endl;

}  
return 0;
}
