#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <string>

using namespace std;

inline int q_num(string &,int,string*,int);

int main(int argc,char *argv[])
{
  if(argc!=3)
    return 0;
  ifstream fin(argv[1]);
  ofstream fout(argv[2]);
  int i,j,n,s,q,iq,c,maxq,t;
  char input[120],*p;
  fin.getline(input,120);
  n=strtol(input,&p,10);
  string search[100],queries[1000];
  for(i=0;i<n;i++)
  {
    fin.getline(input,120);
    s=strtol(input,&p,10);
    for(j=0;j<s;j++)
    {
      fin.getline(input,120);
      search[j]=strtok(input,"\n\r\t");
    }
    fin.getline(input,120);
    q=strtol(input,&p,10);
    for(j=0;j<q;j++)
    {
      fin.getline(input,120);
      queries[j]=strtok(input,"\n\r\t");
    }
    for(c=0,iq=0,maxq=0;iq<q;c++)
    {
      for(j=0;j<s;j++)
      {
        t=q_num(search[j],iq,queries,q);
        if(maxq<t)
          maxq=t;
      }
      iq=maxq;
    }
    fout<<"Case #"<<(i+1)<<": "<<(c?(c-1):c)<<endl;
    cout<<"Case #"<<(i+1)<<": "<<(c?(c-1):c)<<endl;
  }
  fin.close();
  fout.close();
  cout<<"Success"<<endl;
  return 0;
}

inline int q_num(string &search,int pos,string *queries,int num)
{
  int i;
  for(i=pos;i<num&&search!=queries[i];i++);
  return i;
}
