#include <cstdio>
#include <string>
#include <cstring>
#include <iostream>
using namespace std;

int i,j,k,s,t,n,m,T;
int opt[1001][101];
string a[101],b[1001];
char st[20000];
main()
{
  scanf("%d",&T);
  for (int I=1;I<=T;++I)
    {
      scanf("%d\n",&n);
      for (i=1;i<=n;++i)
	{
	  gets(st);
	  a[i]=st;
	}
      scanf("%d\n",&m);
      for (i=1;i<=m;++i)
	{
	  gets(st);
	  b[i]=st;
	}
      for (i=1;i<=n;++i)
	if (a[i]!=b[1]) opt[1][i]=0;
	else opt[1][i]=1000000;
      for (i=2;i<=m;++i)
	for (j=1;j<=n;++j)
	  if (a[j]!=b[i])
	    {
	      opt[i][j]=1000000;
	      for (k=1;k<=n;++k)
		if (opt[i-1][k]+(j!=k)<opt[i][j])
		  opt[i][j]=opt[i-1][k]+(j!=k);
	    }
	  else opt[i][j]=1000000;
      int ans=1000000;
      for (i=1;i<=n;++i)
	if (opt[m][i]<=ans)
	  ans=opt[m][i];
      cout<<"Case #"<<I<<": "<<ans<<endl;
    }
  return 0;
}
		 
