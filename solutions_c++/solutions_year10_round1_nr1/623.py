#include<iostream>
#include<cstring>
#include<cmath>
using namespace std;

const int maxn=55;
char ch[maxn][maxn],cc[maxn][maxn],c;
int tot,k,l,n,m;
int f[4];
string st;

void readdata()
  {
   memset(ch,0,sizeof(0));
   scanf("%d%d\n",&n,&k);
   for (int i=1;i<=n;i++)
     {
      for (int j=1;j<=n;j++)
        scanf("%c",&ch[i][j]);
      scanf("\n");
     }
  }
  
void work()
  {
   memset(cc,0,sizeof(cc));
   for (int i=1;i<=n;i++)
     for (int j=1;j<=n;j++)
       cc[j][n-i+1]=ch[i][j];
   for (int j=1;j<=n;j++)
     {
      st="";
      for (int i=n;i>0;i--)
        if (cc[i][j]!='.')
          st+=cc[i][j];
      for (int i=n;i>0;i--) cc[i][j]='.';
      l=n;
      for (int i=0;i<st.length();i++) cc[l--][j]=st[i];
     }
   m=0;l=0;
   for (int i=1;i<=n;i++)
     for (int j=1;j<=n;j++)
       {
        memset(f,0,sizeof(f));
        if (cc[i][j]=='.') continue;
        if (cc[i][j]=='R') l=0; else l=1;
        c=cc[i][j];
        for (int s=0;s<k;s++)
          {
           if (i+s<=n && cc[i+s][j]==c) f[0]++;
           if (i+s<=n && j-s>0 && cc[i+s][j-s]==c) f[1]++;
           if (i+s<=n && j+s<=n && cc[i+s][j+s]==c) f[2]++;
           if (j+s<=n && cc[i][j+s]==c) f[3]++;
          }
        if (max(max(f[0],f[1]),max(f[2],f[3]))==k) m|=1<<l;
       }
       
  }
  
int main()
  { 
   scanf("%d\n",&tot);
   for (int tt=1;tt<=tot;tt++)
     {
      readdata();
      work();
      printf("Case #%d: ",tt);
      switch (m)
        {
         case 0:printf("Neither\n");break;
         case 1:printf("Red\n");break;
         case 2:printf("Blue\n");break;
         case 3:printf("Both\n");break;
        }
     }
   return 0;
  }
