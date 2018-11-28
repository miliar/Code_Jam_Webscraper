#include<iostream>
#include<fstream>
#include<math.h>
#include<stdlib.h>
using namespace std;
void get_data();
void solve();
int t=0;
int n,p,s;
int ar[100];
int ar1[100];
char ch;
int ctr=0;
int j;
ifstream afile("c:/users/vaibhav/desktop/small.in");
main()
{
      get_data();
}     
void get_data()
{
      cout<<"the contents of file are : ";
      while(1)
      {
      afile.get(ch);
      if(ch!=10)
      t=(t*10)+((int) ch)-48;
      else
      break;
      cout<<t<<"\n";                     
      }
      while(afile)
      {
      for(j=0;j<t;j++)
      solve();   
      }    
}

void solve()
{
     int min,min1;
     n=p=s=0;
     while(1)
      {
      afile.get(ch);
      if(ch!=32)
      n=(n*10)+((int) ch)-48;
      else
      break;
      //cout<<n<<"\t";
      }
      while(1)
      {
      afile.get(ch);
      if(ch!=32)
      s=(s*10)+((int) ch)-48;
      else
      break;
      //cout<<s<<"\n";
      }
      while(1)
      {
      afile.get(ch);
      if(ch!=32)
      p=(p*10)+((int) ch)-48;
      else
      break;
      //cout<<p<<"\n";
      }
      for(int i=0;i<n;i++)
      {
      ar[i]=0;
      while(1)
              {
              afile.get(ch);
              if(ch!=32&&ch!=10&&afile.eof()==0)
              ar[i]=(ar[i]*10)+((int) ch)-48;
              else
              break;
              //cout<<ar[i]<<"\n";
              }         
      }
      ar1[0]=0;
      min=(3*p)-2;
      min1=abs(min-2);
      for(int k=0;k<n;k++)
      {
      if(ar[k]>=min)
      ctr++;
      else if(ar[k]>=min1&&s>0)
           {
           ctr++;
           s--;
           }
      } 
      //cout<<ctr<<"\n";
      //ar1[j]=ctr;
      ofstream bfile("c:/users/vaibhav/desktop/small_out.in",ios::app);
      bfile<<"Case #";
      bfile<<j+1;
      bfile<<": ";
      bfile<<ctr;
      bfile<<"\n";
      ctr=0;
      if(afile.eof()!=0)
      {
      afile.close();
      bfile.close();
      exit(0);
      }     
}
