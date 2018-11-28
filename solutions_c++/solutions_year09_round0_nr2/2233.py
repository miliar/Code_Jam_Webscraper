#include <iostream.h>
  int main()
	{
	int T,i,j,ii,m,n,k,f[102][102],s,z,x[102][102],y[102][102],a[102][102],min,t1,t2;
	scanf("%ld",&T);
    for(ii=1;ii<=T;ii++)
      {
      scanf("%ld%ld",&m,&n);
      for(i=0;i<n+2;i++)
        a[0][i]=a[m+1][i]=20000;
      for(i=0;i<m+2;i++)
        a[i][0]=a[i][n+1]=20000;
      for(i=1;i<=m;i++)
        for(j=1;j<=n;j++)
          scanf("%ld",&a[i][j]);
      for(i=1;i<=m;i++)
        for(j=1;j<=n;j++)
		  {
		  x[i][j]=y[i][j]=0;
		  min=a[i][j];
		  if(a[i-1][j]<min) {
							min=a[i-1][j];
							x[i][j]=-1;
							y[i][j]=0;
							}
		  if(a[i][j-1]<min) {
							min=a[i][j-1];
							x[i][j]=0;
							y[i][j]=-1;
							}
		  if(a[i][j+1]<min) {
							min=a[i][j+1];
							x[i][j]=0;
							y[i][j]=1;
							}
		  if(a[i+1][j]<min) {
							min=a[i+1][j];
							x[i][j]=1;
							y[i][j]=0;
							}
          }
	  z=m*n;
	  memset(f,0,sizeof(f));
      for(i=1;z;i++)
        {
		s=0;
		for(j=1;j<=m;j++)
		  {
		  for(k=1;k<=n;k++)
			if(!f[j][k]) {
						 f[j][k]=i;
						 s=1;
						 z--;
						 break;
						 }
		  if(s) break;
		  }
        for(;s;)
		  {
		  s=0;
		  for(j=1;j<=m;j++)
			for(k=1;k<=n;k++)
			  {
			  t1=f[j][k];
			  t2=f[j+x[j][k]][k+y[j][k]];
			  if((t1+t2==i)&&(t1*t2==0)) {
										 f[j][k]=f[j+x[j][k]][k+y[j][k]]=i;
										 z--;
										 s=1;
										 }
			  }
          }
        }
      printf("Case #%ld:\n",ii);
      for(i=1;i<=m;i++)
        {
		for(j=1;j<n;j++)
		  printf("%c ",f[i][j]+96);
		printf("%c\n",f[i][n]+96);
        }
      }
	}
