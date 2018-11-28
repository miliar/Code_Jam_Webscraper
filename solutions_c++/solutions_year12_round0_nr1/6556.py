#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;
int main()
{

int arr[26];
int brr[26];
memset(arr,-1,26*sizeof(int));
memset(brr,-1,26*sizeof(int));
char maps[26][2];
char out1[]="our language is impossible to understand";
char in1[]="ejp mysljylc kd kxveddknmc re jsicpdrysi";
char out2[]="there are twenty six factorial possibilities";
char in2[]="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
char out3[]="so it is okay if you want to just give up";
char in3[]="de kr kd eoya kw aej tysr re ujdr lkgc jv";


int i,j,k,n,t;
    for (i=0;i<strlen(in1);i++)
    {
        if(in1[i]>='a'&& in1[i]<='z')
        {
        arr[in1[i]-'a']=out1[i]-'a';
        }
    }
        for (i=0;i<strlen(in2);i++)
    {
        if(in2[i]>='a'&& in2[i]<='z')
        {
        arr[in2[i]-'a']=out2[i]-'a';
        }
    }
        for (i=0;i<strlen(in3);i++)
    {
        if(in3[i]>='a'&& in3[i]<='z')
        {
        arr[in3[i]-'a']=out3[i]-'a';
        }
    }
    
    for(i=0;i<26;i++)
    {
        if(arr[i]>=0 &&arr[i]<26 )
        {
       //     cout<<"\n"<<(char)(i+'a')<<"\t"<<(char)(arr[i]+'a');
            brr[arr[i]]=1;
        }
      }
       
    arr[16]=25;
    arr[25]=16;
int T;
char g[35][105];
       scanf("%d\n",&T);
       for(t=0;t<T;t++)
       {
           gets(g[t]);
       }
       for(t=0;t<T;t++)
       {
          //scanf("%[^\n]s",g);
          //cin>>g;
          //cout<<"\ninp="<<g<<"\tlen="<<strlen(g);
          cout<<"\nCase #"<<t+1<<": ";
          for(i=0;i<strlen(g[t]);i++)
          {
               if(g[t][i]>='a' && g[t][i]<='z')
                   cout<<(char)(arr[g[t][i]-'a']+'a');
               else
                   cout<<g[t][i];
          }
          //cout<<"\n";
       }

return 0;
}