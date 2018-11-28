#include <iostream>
#include<string.h>
using namespace std;
int check(string a);
int main()
{
  int i,j,k,t,p0,p1,p2,p3,p4,p5,p6,p7,p8,p9;
  cin>>t;
  int out[t];
  string input[t*4];
  char a[4];
  for(i=0;i<t*4;i++)
  {
    cin>>input[i];    
  }
 for(i=0;i<t;i++)
 {
   p0=check(input[4*i]);
   p1=check(input[4*i+1]);
   p2=check(input[4*i+2]);
   p3=check(input[4*i+3]);
   for(j=0;j<4;j++)
     a[j]=input[4*i+j][0];
   p4=check(a);
   for(j=0;j<4;j++)
     a[j]=input[4*i+j][1];
   p5=check(a);
   for(j=0;j<4;j++)
     a[j]=input[4*i+j][2];
   p6=check(a);
   for(j=0;j<4;j++)
     a[j]=input[4*i+j][3];
   p7=check(a);
   for(j=0;j<4;j++)
     a[j]=input[4*i+j][j];
   p8=check(a);
   for(j=0;j<4;j++)
     a[j]=input[4*i+j][3-j];
   p9=check(a);
  

   if(p0>0)
     out[i]=p0;
   else if(p1>0)
     out[i]=p1;
   else if(p2>0)
     out[i]=p2;
   else if(p3>0)
     out[i]=p3;
   else if(p4>0)
     out[i]=p4;
   else if(p5>0)
     out[i]=p5;
   else if(p6>0)
     out[i]=p6;
   else if(p7>0)
     out[i]=p7;
   else if(p8>0)
     out[i]=p8;
   else if(p9>0)
     out[i]=p9;
   else if((p0==-1)&&(p1==-1)&&(p2==-1)&&(p3==-1)&&(p4==-1)&&(p5==-1)&&(p6==-1)&&(p7==-1)&&(p8==-1)&&(p9==-1))
     out[i]=-1;
   else
     out[i]=0;
 }
 
 for(i=0;i<t;i++)
  {
    cout<<"Case #"<<i+1<<": "; 
    switch(out[i])
    {
      case -1:
      	cout<<"Draw";
      	break;
      case 0:
      	cout<<"Game has not completed";
      	break;
      case 1:
      	cout<<"X won";
      	break;
      case 2:
      	cout<<"O won";
      	break;
    }
   cout<<endl;
 }
   
   return 0;
}

int check(string b)
{  
   char a='a';
   int  j,match=1,mark=5,t;
   for(j=0;j<4;j++)
    {
      if(b[j]=='T')
      {
        mark=j;
      }
      else if(b[j]=='.')
        match=0;
      else
        a=b[j];
   }
   
   if(match!=0)  
   for(j=0;j<4;j++)
   {
     if(j!=mark)
     {
       if(b[j]!=a)
       match=-1;
     }
   }
  if(match==1 && a=='O')
  t=2;
  else
    t=match;
  
  return t;
}
