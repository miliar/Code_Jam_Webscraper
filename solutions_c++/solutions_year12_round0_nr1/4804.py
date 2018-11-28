#include<cstdio>
#include<iostream>
#include<cstring>
using namespace std;
int main()
{
  freopen("in.txt","r",stdin);
  freopen("out.txt","w",stdout);
  int t;
  scanf("%d",&t);
  string s1="ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
  string s2="our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
  char map[26];
  bool dn[26][2];
  memset(dn,0,sizeof(dn));
  int l=s1.length();
  map['q'-'a']='z';
  dn['q'-'a'][0]=true;
  dn['z'-'a'][1]=true;
  for(int i=0;i<l;i++)
  {
    if(s1[i]<='z' && s1[i]>='a')
    {
      map[s1[i]-'a']=s2[i];
      dn[s1[i]-'a'][0]=true;
      dn[s2[i]-'a'][1]=true;
    }
  }
  char c1,c2;
  for(int i=0;i<26;i++)
  {
    if(!dn[i][0])
    {
      c1=i+'a';
    }
    if(!dn[i][1])
    {
      c2=i+'a';
    }
  }
  map[c1-'a']=c2;
  /*for(int i=0;i<26;i++)
  {
    cout<<(char)(i+'a')<<':'<<map[i]<<endl;
  }*/
  int i=1;
  scanf("%c",&c1);
  do
  {
    printf("Case #%d: ",i);
    while(true)
    {
      char t1;
      scanf("%c",&t1);
      if(t1=='\n')
      {
        printf("\n");
        break;
      }
      if(t1==' ')
      {
        printf(" ");
      }
      if(t1<='z' && t1>='a')
      {
        printf("%c",map[t1-'a']);
      }
    }
    i++;
  }
  while(i<=t);
  return 0;
}
