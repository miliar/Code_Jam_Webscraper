#include<stdio.h>
#include<string.h>

int t,n,s,q,r;
char ss[105][150];
char qq[1005][150];
int qqq[1005];
int f[105];
FILE *fp1;
FILE *fp2;

int main()
{  
  fp1=fopen("A-large.in","r");
  fp2=fopen("A2.txt","w");
  fscanf(fp1,"%d",&n);
  for(int cc=1;cc<=n;cc++)
  {
    fscanf(fp1,"%d",&s);
    fgetc(fp1);
    for(int i=1;i<=s;i++)
      fgets(ss[i],110,fp1); 
    fscanf(fp1,"%d",&q);
    fgetc(fp1);
    for(int i=1;i<=q;i++)
    {
      fgets(qq[i],110,fp1);
      for(int j=1;j<=s;j++)
        if(strcmp(qq[i],ss[j])==0)
        {
          qqq[i]=j;
          break;  
        }
    }
    memset(f,-1,sizeof(f));
    t=0;
    r=0;
    for(int i=1;i<=q;i++)
      if(f[qqq[i]]==-1)
      {
        t++;
        if(t==s)
        {
          r++;
          memset(f,-1,sizeof(f));
          t=1;
        }
        f[qqq[i]]=0;                       
      }
    fprintf(fp2,"Case #%d: %d\n",cc,r);
  }
  fclose(fp1);
  fclose(fp2);
  return 0;
}
/*#include<iostream>
#include<fstream>
#include<string>
#include<map>
using namespace std;

map<string,int> mm;
int t,n,s,q,r;
string ss[105];
string qq[1005];
int qqq[1005];
int f[105];

int main()
{
  //ifstream cin("A-small-attempt2.in");
  //ofstream cout("A1.txt");
  cin>>n;
  for(int cc=1;cc<=n;cc++)
  {
    mm.clear();
    cin>>s;
    cin.ignore();
    for(int i=1;i<=s;i++)
    {
      getline(cin,ss[i]);
      mm[ss[i]]=i;   
    }
    cin>>q;
    cin.ignore();
    for(int i=1;i<=q;i++)
    {
      getline(cin,qq[i]);
      qqq[i]=mm[qq[i]];
    }
    memset(f,-1,sizeof(f));
    t=0;
    r=0;
    for(int i=1;i<=q;i++)
      if(f[qqq[i]]==-1)
      {
        t++;
        if(t==s)
        {
          r++;
          memset(f,-1,sizeof(f));
          t=1;
        }
        f[qqq[i]]=0;                       
      }
    cout<<"Case #"<<cc<<": "<<r<<"\n";
  }
}*/
