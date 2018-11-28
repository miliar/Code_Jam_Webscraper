#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
int n,m,f[260];
string a[40],b[30];
int main()
{
   void work(string &);
   int T;
   scanf("%d",&T);
   while (T--)
   {
      scanf("%d",&n);
      string s;
      for (int i=1;i<=n;i++)
      {
         cin>>s;

      scanf("%d",&m);
      for (int i=1;i<=m;i++)
         cin>>b[i];
      int len;
      scanf("%d",&len);
      string ans,s;
      cin>>s;
      memset(f,0,sizeof(f));
      for (int i=0;i<len;i++)
      {
         ans+=s[i];
         f[s[i]]++;
         work(ans);
      }
      static int id=0;
      printf("Case #%d: [",++id);
      for (int i=0;i<ans.size();i++)
      {
         if (i)
            printf(", ");
         printf("%c",ans[i]);
      }
      printf("]\n");
   }
   return(0);
}
void work(string &s)
{
   if (s.size()<=1)
      return;
   for (int i=1;i<=n;i++)
   {
      string now=s.substr(s.size()-2),p=a[i].substr(0,2),q=p;
      swap(q[0],q[1]);
      if (now==p || now==q)
      {
         s.resize(s.size()-2);
         f[a[i][0]]--,f[a[i][1]]--,f[a[i][2]]++;
         s+=a[i][2];
         return;
      }
   }
   for (int i=1;i<=m;i++)
   {
      if (f[b[i][0]] && f[b[i][1]])
      {
         s.clear();
         memset(f,0,sizeof(f));
         return;
      }
   }
}
