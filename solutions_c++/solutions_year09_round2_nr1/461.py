#include<iostream>
#include<fstream>
#include<cstdio>
using namespace std;

int main()
{
  char a[1009];
  ifstream fin("in");
  int i,cnt=0,l;
  l=0;
  while(!fin.eof())
  {
    fin.getline(a,1000,'\n');
    i=0;
    while(a[i]!='\0')
    {
      if(a[i]==' ' && l==0)
      {   
          cout<<endl;
          l=1;
      }
      else
      {
        if(a[i]=='('||a[i]==')' && l==0)
        {
          cout<<endl;
          l=0;
        }
        cout<<a[i];
        l=0;
        if(a[i]=='('||a[i]==')' && l==0)
        {
          cout<<endl;
          l=0;
        }
      }
      i++;
    }
    cout<<endl;
  }

  return 0;
}

