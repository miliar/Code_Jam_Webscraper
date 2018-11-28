#include<iostream>
#include<algorithm>
using namespace std;
#define getc() getchar_unlocked()
int main()
{
  char c;
  int a[30];
  int n,i,t,tc,flag;
  cin>>t;
  c=' ';
  for(tc=1;tc<=t;tc++)
  {
    while(c==' '||c=='\n')
    {
      c=getc();
    }
    n=0;
    //cout<<"enter no";
    while(c>='0' && c<='9')
    {
      a[n++]=(c-('0'));
      //cout<<"entered "<<c<<"   N:"<<n<<endl;
      c=getc();
      //cin>>c;
    }
    next_permutation(a,a+n);
    flag=0;
    for(i=1;i<n;i++)
    {
      if(a[i]<a[i-1])
      {
	flag=1;
	break;
      }
    }
    if(flag==0)
    {
      for(i=n;i>=0;i--)
	a[i+1]=a[i];
      a[0]=0;
      i=0;
      while(a[i]==0)
      {
	i++;
      }
      a[0]=a[i];
      a[i]=0;
      n++;
    }
      
    cout<<"Case #"<<tc<<": ";
    for(i=0;i<n;i++)
    {
      cout<<a[i];
    }
    cout<<endl;
  }
  
  return 0;
}