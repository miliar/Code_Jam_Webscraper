#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
string s[10010];
char S[30];
int n;
int main()
{
   int work(int);
   int T;
   scanf("%d",&T);
   while (T--)
   {
      int m;
      scanf("%d%d",&n,&m);
      for (int i=1;i<=n;i++)
      {
         scanf("%s",S);
         s[i]=S;
      }
      static int id=0;
      printf("Case #%d:",++id);
      for (int i=1;i<=m;i++)
      {
         scanf("%s",S);
         int value=-1,ans;
         for (int j=1;j<=n;j++)
         {
            int p=work(j);
            if (p>value)
               value=p,ans=j;
         }
         printf(" %s",s[ans].c_str());
      }
      printf("\n");
   }
}
bool f[20],vis[30];
vector <int> a,b;
int work(int id)
{
   void check();
   int pen=0;
   a.clear();
   for (int i=1;i<=n;i++)
      if (s[i].size()==s[id].size())
         a.push_back(i);
   check();
   for (int i=0;i<26;i++)
   {
      if (a.size()==1)
         break;
      if (!vis[S[i]-'a'])
         continue;
      memset(f,0,sizeof(f));
      bool flag=true;
      for (int j=0;j<s[id].size();j++)
         if (s[id][j]==S[i])
         {
            f[j]=true;
            flag=false;
         }
      pen+=flag;
      b.clear();
      for (int j=0;j<a.size();j++)
      {
         int x=a[j];
         flag=true;
         for (int k=0;k<s[x].size();k++)
            if (s[x][k]==S[i] && !f[k] || s[x][k]!=S[i] && f[k])
            {
               flag=false;
               break;
            }
         if (flag)
            b.push_back(x);
      }
      a=b;
      check();
   }
   return(pen);
}
void check()
{
   memset(vis,0,sizeof(vis));
   for (int i=0;i<a.size();i++)
   {
      int x=a[i];
      for (int j=0;j<s[x].size();j++)
         vis[s[x][j]-'a']=true;
   }
}
