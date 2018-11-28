#include<iostream>
#include<cstdio>
#include<fstream>
#include<string>
#include<vector>
#include<istream>
#include<map>
#define M 300
using namespace std;
int g[M][M];
int match[M];
int len1=0,len2=0;
int v[M];
int dfs(int p,int m)
{
    int i,t;
    for(int i=0;i<m;i++)
    {
        if(g[p][i]==1&&!v[i])
        {
            v[i]=1;
            t=match[i];
            match[i]=p;
            if(t==-1||dfs(t,m))return 1;
            match[i]=t;
        }
    }
    return 0;
}
int mat(int n,int m)
{
    int i,res=0;
    for(int i=0;i<n;i++)
    {
        memset(v,0,sizeof(v));
        if(dfs(i,m))res++;
    }
    return res;
}
int main()
{
    freopen("B-large.in","r",stdin);freopen("out.txt","w",stdout);
    int n;
    cin>>n;
    int l1[M][4];
    int l2[M][4];
    int A,B;
    string aa,bb;
    for(int i=0;i<n;i++)
    {
        len1=0;
        len2=0;
        int t;
        cin>>t;
        int m,mm;
        cin>>m>>mm;
        getchar();
        memset(l1,0,sizeof(l1));
        memset(l2,0,sizeof(l2));
        for(int j=0;j<m;j++)
        {
            cin>>aa>>bb;
            getchar();
            int s1=0;
            int k=0;
            while(aa[k]!=':')
            s1=s1*10+aa[k++]-'0';
            int s2=0;
            k++;
            while(k<aa.size())
            {
                s2=s2*10+aa[k++]-'0';
            }
            l1[len1][0]=s1*60+s2;
            s1=0;
            k=0;
            while(bb[k]!=':')
            s1=s1*10+bb[k++]-'0';
            s2=0;
            k++;
            while(k<bb.size())
            s2=s2*10+bb[k++]-'0';
            l1[len1][1]=s1*60+s2+t;
            len1++;
        }
        for(int j=0;j<mm;j++)
        {
            cin>>aa>>bb;
            int s1=0;
            int k=0;
            while(aa[k]!=':')
            s1=s1*10+aa[k++]-'0';
            int s2=0;
            k++;
            while(k<aa.size())
            s2=s2*10+aa[k++]-'0';
            l2[len2][0]=s1*60+s2;
            
            s1=0;
            k=0;
            while(bb[k]!=':')
            s1=s1*10+bb[k++]-'0';
            s2=0;
            k++;
            while(k<bb.size())
            s2=s2*10+bb[k++]-'0';
            l2[len2][1]=s1*60+s2+t;
            len2++;
        }
       memset(match,-1,sizeof(match));
       memset(g,0,sizeof(g));
       for(int j=0;j<len1;j++)
       {
          for(int k=0;k<len2;k++)
          {
              if(l2[k][0]>=l1[j][1])
              {
                  
                  g[j][k]=1;
              }
          }
       }
       mat(len1,len2);
       A=0;B=0;
       for(int j=0;j<len2;j++)
       {
           if(match[j]==-1)
           {
               B++;
           }
       }
       memset(match,-1,sizeof(match));
       memset(g,0,sizeof(g));
       for(int j=0;j<len2;j++)
       {
          for(int k=0;k<len1;k++)
          {
              if(!l1[k][2]&&l1[k][0]>=l2[j][1])
              {
                  g[j][k]=1;
              }
          }
       }
       mat(len2,len1);
       for(int j=0;j<len1;j++)
       {
           if(match[j]==-1)
           {
               A++;
           }
       }
       cout<<"Case #"<<i+1<<": "<<A<<" "<<B<<endl;
    }
}
