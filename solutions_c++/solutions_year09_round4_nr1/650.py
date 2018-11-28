#include<iostream>
#include<cstdio>

using namespace std;

int main()
{
  int tc,t,n,i,j,cnt,tmpn;
  int a[50];
  char c;
  scanf("%d",&t);
  for(tc=1;tc<=t;tc++)
  {
    scanf("%d",&n);
    for(i=1;i<=n;i++)
    {
      cnt=0;
      for(j=1;j<=n;j++)
      {
	c=' ';
	while(c!='0'&&c!='1')
	{
	  scanf("%c",&c);
	}
	if(c=='1')
	  cnt=j;
      }
      a[i]=cnt;
    }
//    for(i=1;i<=n;i++)
//      cout<<a[i]<<' ';
//    cout<<endl;
    cnt=0;
    tmpn=n;
    for(i=1;i<=n;i++)
    {
      for(j=1;j<=tmpn;j++)
      {
	if(a[j]<=i)
	{
	  break;
	}
      }
      cnt+=j-1;
      for(;j<=tmpn;j++)
      {
	a[j]=a[j+1];
      }
      tmpn--;
    }
    printf("Case #%d: %d\n",tc,cnt);
  }
  return 0;
}