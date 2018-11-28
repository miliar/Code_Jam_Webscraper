#define HASH(x,y) ((x)*m+y)
#include <iostream>
using namespace std;
int f[20001];
bool u[20001];
char c[111][111];
int a[111][111];
int getf(int x)
{
  if (x!=f[x])f[x]=getf(f[x]);
  return f[x];
}
int main()
{
  freopen("B-large.in","r",stdin);
  freopen("x.out","w",stdout);
  int tn;
  int n,m;
  cin>>tn;
 
  for (int ts=1;ts<=tn;ts++)
  {
    cin>>n>>m;
    for (int i=0;i<n;i++)
      for (int j=0;j<m;j++)
      {
        cin>>a[i][j];
      }
    for (int i=0;i<n*m;i++)f[i]=i;
    for (int i=0;i<n;i++)
    {
      for (int j=0; j<m;j++)
      {
         int h=a[i][j];
         if (i>0&&a[i-1][j]<h){h=a[i-1][j];f[HASH(i,j)]=getf(HASH(i-1,j));}
         if (j>0&&a[i][j-1]<h){h=a[i][j-1];f[HASH(i,j)]=getf(HASH(i,j-1));}
         if (j<m-1&&a[i][j+1]<h){h=a[i][j+1];f[HASH(i,j)]=getf(HASH(i,j+1));}
         if (i<n-1&&a[i+1][j]<h){h=a[i+1][j];f[HASH(i,j)]=getf(HASH(i+1,j));}
      }
    }
   // for (int i=0;i<n*m;i++)
   ///   cout<<getf(i)<<" ";
  //  cout<<endl;
    char A='a'-1;
    memset(u,false,sizeof(u));
    cout<<"Case #"<<ts<<":"<<endl;
    for (int i=0;i<n*m;i++)
    {
      int pre=getf(i);
      if(!u[pre])
        {
        A++;
        u[pre]=true;
        c[pre/m][pre%m]=A;
        }
      c[i/m][i%m]=c[pre/m][pre%m];
    }
    for (int i=0;i<n;i++)
    {
      for (int j=0;j<m-1;j++)
        printf("%c ",c[i][j]);
      printf("%c\n",c[i][m-1]);
    }
  }
  return 0;
}
