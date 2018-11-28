#include<iostream>
#include<cstring>
#include<vector>
using namespace std;

const int maxn=28;
const int maxm=1010;
int a[maxm][maxn],c[maxn],l[maxn],r[maxn],g[maxn],h[maxn],mid[maxn],one[maxn];
char st[maxm];
string s,sm;
int t,n,m,k,tt;
int pw[4];

void init()
  {
   n=0;k=0;
   while (s[k]!=' ') n=n*10+s[k++]-'0';k++;
   m=0;
   while (k<s.length())
     {
      sm="";while (s[k]!=' ') sm+=s[k++];k++;
      memset(a[m],0,sizeof(a[m]));a[m][0]=1;
      int l=0;
      for (int i=sm.length()-1;i>=0;i--)
        if (l<4)
          {
           l++;
           a[m][a[m][0]]=a[m][a[m][0]]+(sm[i]-'0')*pw[l-1];
          }
        else {l=1;a[m][++a[m][0]]=sm[i]-'0';}
      m++;
     }
  }
  
bool cmp(int a[],int b[])
  {
   if (a[0]>b[0]) return true;
   if (a[0]<b[0]) return false;
   for (int i=a[0];i>0;i--)
     {
      if (a[i]>b[i]) return true;
      if (a[i]<b[i]) return false;
     }
   return false;
  }
  
void swap(int a[],int b[])
  {
   c[0]=a[0];for (int i=0;i<=c[0];i++) {c[i]=a[i];a[i]=0;}
   a[0]=b[0];for (int i=0;i<=a[0];i++) {a[i]=b[i];b[i]=0;}
   b[0]=c[0];for (int i=0;i<=b[0];i++) {b[i]=c[i];c[i]=0;}
  }
  
void qsort(int s,int t)
  {
   if (s>=t) return;
   int x[maxn];
   for (int i=0;i<=a[(s+t)/2][0];i++) x[i]=a[(s+t)/2][i];
   int i=s,j=t;
   do
    {
     while (cmp(a[j],x)) j--;
     while (cmp(x,a[i])) i++;
     if (i<=j)
       {
        swap(a[i],a[j]);
        i++;j--;
       }
    }
   while (i<j);
   qsort(s,j);
   qsort(i,t);
  }
  
void add(int c[],int a[],int b[])
  {
   c[0]=max(a[0],b[0]);
   for (int i=1;i<=c[0];i++)
     {
      c[i]+=a[i]+b[i];
      if (c[i]>=10000) {c[i]-=10000;c[i+1]++;}
     }
   while (c[c[0]+1]) c[0]++;
  }
  
void reduce(int c[],int a[],int b[])
  {
   c[0]=a[0];
   for (int i=1;i<=a[0];i++)
     {
      c[i]=c[i]+a[i]-b[i];
      if (c[i]<0) {c[i]+=10000;c[i+1]--;}
     }
   while (!c[c[0]] && c[0]>1) c[0]--;
  }
  
void mult(int c[],int a[],int b[])
  {
   c[0]=a[0]+b[0]-1;
   for (int i=1;i<=a[0];i++)
     for (int j=1;j<=b[0];j++)
       {
        c[i+j-1]+=a[i]*b[j];
        c[i+j]+=c[i+j-1]/10000;
        c[i+j-1]%=10000;
       }
   while (c[c[0]+1]) c[0]++;
  }
  
void div2(int c[])
  {
   int k=0;
   for (int i=c[0];i>0;i--)
     {
      k=k*10000+c[i];
      c[i]=k/2;
      k%=2;
     }
   while (!c[c[0]]) c[0]--;
  }
  
void print(int a[])
  {
   printf("Case #%d: ",tt);
   printf("%d",a[a[0]]);
   for (int i=a[0]-1;i>0;i--)
     {
      if (a[i]<1000) printf("0");
      if (a[i]<100) printf("0");
      if (a[i]<10) printf("0");
      printf("%d",a[i]);
     }
   printf("\n");
  }
  
void gcd(int a[],int b[])
  {
   if (b[0]==1 && b[1]==0)
     {
      memset(c,0,sizeof(c));
      for (int i=0;i<=a[0];i++) c[i]=a[i];
      return;
     }
   memset(l,0,sizeof(l));l[0]=l[1]=1;
   memset(r,0,sizeof(r));r[0]=13;r[13]=100;
   while (!cmp(l,r))
     {
      memset(mid,0,sizeof(mid));
      add(mid,l,r);
      div2(mid);
      memset(c,0,sizeof(c));
      mult(c,b,mid);
      if (cmp(c,a)) 
        {
         memset(r,0,sizeof(r));
         reduce(r,mid,one);
        }
      else
        {
         memset(l,0,sizeof(l));
         add(l,mid,one);
        }
     }
   memset(c,0,sizeof(c));
   mult(c,b,r);
   memset(r,0,sizeof(r));
   reduce(r,a,c);
   memset(a,0,sizeof(a));
   for (int i=0;i<=r[0];i++) a[i]=r[i];
   gcd(b,a);
  }
  
void solve()
  {
   qsort(0,n-1);
   /*for (int i=0;i<n;i++)
     {
      printf("%d",a[i][a[i][0]]);
      for (int j=a[i][0]-1;j>0;j--) 
        {
         if (a[i][j]<1000) printf("0");
         if (a[i][j]<100) printf("0");
         if (a[i][j]<10) printf("0");
         printf("%d",a[i][j]);
        }
      printf("\n");
     }*/
   for (int i=0;i<n-1;i++)
     {
      memset(c,0,sizeof(c));
      reduce(c,a[i+1],a[i]);
      memset(a[i],0,sizeof(a[i]));
      for (int j=0;j<=c[0];j++) a[i][j]=c[j];
     }
   m=n-1;
   /*for (int i=0;i<m;i++)
     {
      printf("%d",a[i][a[i][0]]);
      for (int j=a[i][0]-1;j>0;j--) 
        {
         if (a[i][j]<1000) printf("0");
         if (a[i][j]<100) printf("0");
         if (a[i][j]<10) printf("0");
         printf("%d",a[i][j]);
        }
      printf("\n");
     }*/
   for (int i=1;i<m;i++) 
     {
      memset(g,0,sizeof(g));
      for (int j=0;j<=a[i][0];j++) g[j]=a[i][j];
      memset(h,0,sizeof(h));
      for (int j=0;j<=a[i-1][0];j++) h[j]=a[0][j];
      gcd(g,h);
      memset(a[0],0,sizeof(a[0]));
      for (int j=0;j<=c[0];j++) a[0][j]=c[j];
     }
   memset(l,0,sizeof(l));l[0]=l[1]=1;
   memset(r,0,sizeof(r));r[0]=13;r[13]=100;
   //printf("%d\n",a[0][0]);
   //print(a[0]);print(a[n-1]);
   while (!cmp(l,r))
     {
      memset(mid,0,sizeof(mid));
      add(mid,l,r);
      div2(mid);
      memset(c,0,sizeof(c));
      mult(c,a[0],mid);
      if (cmp(c,a[n-1])) 
        {
         memset(r,0,sizeof(r));
         reduce(r,mid,one);
         //printf("R:\n");print(r);
        }
      else
        {
         memset(l,0,sizeof(l));
         add(l,mid,one);
         //printf("L:\n");print(l);
        }
     }
   memset(c,0,sizeof(c));
   mult(c,a[0],r);
   if (cmp(a[n-1],c))
     {
      memset(c,0,sizeof(c));
      mult(c,a[0],l);
     }
   //print(c);
   memset(r,0,sizeof(r));
   reduce(r,c,a[n-1]);
   print(r);
  }
  
int main()
  {
   //freopen("fair.in","r",stdin);
   //freopen("fair.out","w",stdout);
   pw[0]=1;for (int i=1;i<4;i++) pw[i]=pw[i-1]*10;
   one[0]=1;one[1]=1;
   scanf("%d\n",&t);
   for (tt=1;tt<=t;tt++)
     {
      gets(st);s=st;
      s+=' ';
      init();
      solve();
     }
   return 0;
  }
