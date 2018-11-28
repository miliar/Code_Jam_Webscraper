#include<iostream>
#include<string>
#include<fstream>
using namespace std;

int a,b,n;

int recycle(int x)
{
int c=0;
int max;
int ll=1;
for(int i=1;i<n;++i)
ll*=10;
int m=x;
for(int i=0;i<n;++i)
{ max=((m%10)*ll)+(m/10);
  m=((m%10)*ll)+(m/10);
  if((max<=b)&&(max>x)) c++;
}
return c;
}

int main()
{
  

 int t;
 fstream fs,gs;
 fs.open("C-small.in",ios::in);
 gs.open("C-output.txt",ios::out);
 fs>>t;
 for(int i=1;i<=t;i++)
 {
 int count=0;
 fs>>a>>b; 
   n=0;
    int m=a;
    while(m>0)
    {
    m=m/10;
    n++;
    }
   
    for(int i=a;i<b;++i)
        count+=recycle(i);
      

 gs<<"Case #"<<i<<": "<<count<<endl;
}
 return 0;

}
