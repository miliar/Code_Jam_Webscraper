#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<cstring>
using namespace std;

typedef struct
{
  int n1;
  int n2;
}set;

void swap(set *p)
{
  if((*p).n1<=(*p).n2)
   return;
  int t=(*p).n1;
  (*p).n1=(*p).n2;
  (*p).n2=t;
}

int main()
{
  char a[8],b[8];
  bool flag;
  int t,ct;
  set *s=NULL,p;
  
  cin>>t;
  for(int i=0;i<t;i++)
  {
     ct=0;
     char start[8];
     scanf("%s",a);
     strcpy(start,a);
     scanf("%s",b);
     char temp[8],buf[8],ans[8];
     while(1)
     {
      int lpos=strlen(a)-1;
      if(lpos!=0)
      {
       for(int j=lpos;j>0;j--)
       {
          if(a[lpos]=='0')
           continue;
          sprintf(temp,"%s",a+j);
          snprintf(buf,j+1,"%s",a);
          sprintf(ans,"%s%s",temp,buf);
          if(strcmp(ans,b)<=0 && strcmp(ans,start)>=0 && strcmp(ans,a)!=0)
          {
           p.n1=atoi(a);
           p.n2=atoi(ans);
           swap(&p);
           if(s==NULL)
           {
             s=(set *)malloc(sizeof(set));
             s[ct]=p;
             ct++;
           }
           else
           {
             flag=true;
             for(int k=0;k<ct;k++)
              if(s[k].n1==p.n1 && s[k].n2==p.n2)
              {
                flag=false;
                break;
              }
             if(flag)
             {
               s=(set *)realloc(s,sizeof(set)*(ct+1));
               s[ct]=p;
               ct++;
             }
           }
          }
       }
      }
      unsigned int x=atoi(a);
      if(x==atoi(b))
       break;
      sprintf(a,"%d",x+1);
     }
     cout<<"Case #"<<i+1<<": "<<ct<<endl;
     if(s!=NULL)
     {
      free(s);
      s=NULL;
     }
  }

  return 0;
}
