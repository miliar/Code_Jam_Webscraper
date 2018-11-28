#include<iostream>
#include<cstring>
using namespace std;

const int maxn=26;
char c[maxn][maxn];
bool vis[maxn][maxn];
char ans[100000];
int tt,n,m;
string st;

void init()
  {
   for (int i=0;i<26;i++)
     for (int j=0;j<26;j++)
       c[i][j]='.';
   memset(vis,0,sizeof(vis));
   cin>>n;for (int i=0;i<n;i++) {cin>>st;c[int(st[0]-'A')][int(st[1]-'A')]=c[int(st[1]-'A')][int(st[0]-'A')]=st[2];}
   cin>>n;for (int i=0;i<n;i++) {cin>>st;vis[int(st[0]-'A')][int(st[1]-'A')]=vis[int(st[1]-'A')][int(st[0]-'A')]=true;}
   cin>>n;cin>>st;
  }
  
void solve()
  {
   m=0;
   for (int i=0;i<st.length();i++)
     {
      ans[m++]=st[i];
      if (m>1 && c[int(ans[m-1]-'A')][int(ans[m-2]-'A')]!='.')
        {
         ans[m-2]=c[int(ans[m-1]-'A')][int(ans[m-2]-'A')];
         m--;
         continue;
        }
      for (int j=m-1;j>=0;j--)
        if (vis[int(ans[j]-'A')][int(ans[m-1]-'A')])
          {
           m=0;
           break;
          }
     }
  }
  
int main()
  {
   freopen("B.in","r",stdin);
   freopen("B.out","w",stdout);
   cin>>tt;
   for (int t=1;t<=tt;t++)
     {
      init();
      solve();
      printf("Case #%d: ",t);
      printf("[");if (m) printf("%c",ans[0]);
      for (int i=1;i<m;i++) printf(", %c",ans[i]);
      printf("]\n");
     }
   return 0;
  }
