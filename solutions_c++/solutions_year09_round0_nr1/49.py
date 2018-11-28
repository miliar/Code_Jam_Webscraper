#include<cstdio>
#include<cstdlib>
#include<cstring>
using namespace std;

int l,d,n;
char s[50001][170];
int ans;
bool flag;
char q[10000001];
char a[170][270];
int now;
int num[170];

int main()
{
  freopen("A.in","r",stdin);
  freopen("A.out","w",stdout);
  scanf("%d%d%d",&l,&d,&n);
  for(int i=1;i<=d;i++)
    scanf("%s\n",&s[i]);
  for(int i=1;i<=n;i++)
  {
    ans=0;
    now=-1;
    memset(num,0,sizeof(num));
    flag=false;
    scanf("%s\n",&q);
    for(int j=0;j<strlen(q);j++)
    {
      if(q[j]=='(')
      {
	flag=true;
	now++;
	continue;
      }
      if(q[j]==')')
      {
	flag=false;
	continue;
      }
      if(flag)
	a[now][num[now]++]=q[j];
      else
      {
	a[++now][0]=q[j];
	num[now]=1;
      }
    }
    for(int j=1;j<=d;j++)
      for(int k=0;k<l;k++)
      {
	bool flag=false;
	for(int p=0;p<num[k];p++)
	  if(a[k][p]==s[j][k])
	  {
	    flag=true;
	    break;
	  }
	if(flag)
	  continue;
	else
	{
	  ans--;
	  break;
	}
      }
    printf("Case #%d: %d\n",i,ans+d);
  }
  return 0;
}



