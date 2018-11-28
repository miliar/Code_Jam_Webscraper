#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <string>

using namespace std;

struct t_table {
  int start;
  int end;
  bool used;
};

int sort_start(const void *,const void *);
int sort_end(const void *,const void *);

int main(int argc,char *argv[])
{
  if(argc!=3)
    return 0;
  ifstream fin(argv[1]);
  ofstream fout(argv[2]);
  int i,j,n,na,nb,ra,rb,t,k;
  char input[120],*p,*p2;
  fin.getline(input,120);
  n=strtol(input,&p,10);
  t_table a[100],b[100];
  for(i=0;i<n;i++)
  {
    fin.getline(input,120);
    t=strtol(input,&p,10);
    fin.getline(input,120);
    na=strtol(input,&p,10);
    nb=strtol(p,&p2,10);
    ra=na;
    rb=nb;
    for(j=0;j<na;j++)
    {
      fin.getline(input,120);
      a[j].start=strtol(input,&p,10)*60;
      a[j].start+=strtol(p+1,&p2,10);
      a[j].end=strtol(p2,&p,10)*60;
      a[j].end+=strtol(p+1,&p2,10)+t;
      a[j].used=false;
    }
    for(j=0;j<nb;j++)
    {
      fin.getline(input,120);
      b[j].start=strtol(input,&p,10)*60;
      b[j].start+=strtol(p+1,&p2,10);
      b[j].end=strtol(p2,&p,10)*60;
      b[j].end+=strtol(p+1,&p2,10)+t;
      b[j].used=false;
    }
    
    qsort(a,na,sizeof(t_table),sort_end);
    qsort(b,nb,sizeof(t_table),sort_start);
    for(j=0,k=0;j<na;j++)
    {
      for(;k<nb&&(b[k].start<a[j].end||b[k].used);k++);
      if(k==nb)
        break;
      b[k].used=true;
      rb--;
    }
    
    
    qsort(b,nb,sizeof(t_table),sort_end);
    qsort(a,na,sizeof(t_table),sort_start);
    
    for(j=0,k=0;j<nb;j++)
    {
      for(;k<na&&(a[k].start<b[j].end||a[k].used);k++);
      if(k==na)
        break;
      a[k].used=true;
      ra--;
    }
    
    fout<<"Case #"<<(i+1)<<": "<<ra<<" "<<rb<<endl;
    cout<<"Case #"<<(i+1)<<": "<<ra<<" "<<rb<<endl;
  }
  fin.close();
  fout.close();
  cout<<"Success"<<endl;
  return 0;
}

int sort_start(const void *a,const void *b)
{
  return (((t_table *)a)->start)-(((t_table *)b)->start);
}

int sort_end(const void *a,const void *b)
{
  return (((t_table *)a)->end)-(((t_table *)b)->end);
}
