#include<cstdio>
#include<iostream>
#include<vector>
using namespace std;
int main()
{
    int t,s,q;
   scanf("%d",&t);
   for(int pp=0;pp<t;++pp)
     {
       char abhi[111];
       scanf("%d\n",&s);
       string st[101],query[1001];
       for(int i=0;i<s;++i)gets(abhi),st[i]=abhi;
       scanf("%d\n",&q);
       for(int i=0;i<q;++i)gets(abhi),query[i]=abhi;
       int array[1001];
       //for(int i=0;i<s;++i)cout<<st[i]<<endl;
       bool visited[1200];
       int ans=0,cnt=0; 
       memset(visited,0,sizeof(visited));
       for(int i=0;i<q;++i)
          {
              for(int j=0;j<s;++j)
                 {
                     if(query[i]==st[j])
                        {
                           if(!visited[j])visited[j]=1,cnt++;
                           if(cnt==s)
                               {
                                  memset(visited,0,sizeof(visited));
                                  cnt=1;
                                  visited[j]=1;
                                  ans++;
                                }
                            break;
                         }
                     }
              }
    cout<<"Case #"<<pp+1<<": "<<ans<<endl;
    }
  return 0;
}
