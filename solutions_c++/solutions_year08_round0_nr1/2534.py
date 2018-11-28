#include<fstream.h>
#include<string.h>
#include<conio.h>

//compiled in Borland C++ Version 5.02

int found(char str[100][105],char temp[305], int s)
{
 for(;s>0;--s)
 {
  if(strcmp(temp,str[s-1])==0)
  {
   return (s-1);
  }
 }
 return -1;
}

int gcount;

int **array=new int *[100];

void func(int & j, int & s, int & q, int neglect, int count)
{
 if(j>=q)
 {
  if(gcount==-1 || gcount>count)
  {
   gcount=count;
   cout<<count<<endl;
  }
 }
 else
 {
  if(j==0)
  {
   for(int i=0;i<s;++i)
   {
    if(array[i][j]==1)
    {
     j=j+1;
     func(j,s,q,i,count);
     j=j-1;
    }
   }
  }
  else
  {
   if(array[neglect][j]==1)
   {
    j=j+1;
    func(j,s,q,neglect,count);
    j=j-1;
   }
   else
   {
    int k=-1,nk=-1;
    int found=0;
    for(int i=0;i<s;++i)
    {
     if(array[i][j]==1)
     {
      if(i!=neglect)
      {
       int ni=j+1;
       for(;ni<q;++ni)
       {
        if(array[i][ni]!=1)
        {
         break;
        }
       }
       ni-=(j+1);
       if(k==-1 || nk<ni)
       {
        k=i;
        nk=ni;
        found=1;
       }
      }
     }
    }
    if(found>0)
    {
     j=j+1;
     func(j,s,q,k,count+1);
     j=j-1;
    }
   }
  }
 }
}

int main()
{
 ofstream fout;
 ifstream fin;
 char temp[305];
 char str[100][105];
 strcpy(temp,"a-small.in");
 fin.open(temp);
 strcpy(temp,"output.txt");
 fout.open(temp);
 int num,rq;
 fin>>num;
 fin.get();
 int s,q;
 for(int i=0;i<100;++i)
 {
  array[i]=new int [1000];
 }
 for(int i=0;i<num;++i)
 {
  fin>>s;
  fin.get();
  if(s==0)
  {
   fout<<"Case #"<<(i+1)<<": 0"<<endl;
   continue;
  }
  for(int j=0;j<s;++j)
  {
   fin.getline(str[j],105);
  }
  fin>>q;
  rq=0;
  fin.get();
  for(int j=0;j<q;++j)
  {
   fin.getline(temp,105);
   if(found(str,temp,s)!=-1)
   {
    for(int k=0;k<s;++k)
    {
     array[k][rq]=1;
    }
    array[found(str,temp,s)][rq]=0;
    rq++;
   }
  }
  gcount=-1;
  if(rq>0)
  {
   int t=0;
   func(t,s,rq,-1,0);
  }
  else
  {
   gcount=0;
  }
  fout<<"Case #"<<(i+1)<<": "<<gcount<<endl;
 }
 for(int j=0;j<100;++j)
 {
  delete[] array[j];
 }
 delete[] array;
 fout.close();
 fin.close();
 return 0;
}