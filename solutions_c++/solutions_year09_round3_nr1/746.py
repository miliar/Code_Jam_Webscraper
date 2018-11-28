#include<cstdio>
#include<cstdlib>
#include<cstring>
using namespace std;

int t;
char s[1000];
int b[10001];
bool use[10001];

int main()
{
  freopen("A-large.in","r",stdin);
  freopen("a.out","w",stdout);
  scanf("%d\n",&t);
  for(int T=1;T<=t;T++)
  {
    memset(b,0,sizeof(b));
    memset(use,0,sizeof(use));
    int cnt=0;
    gets(s);
    for(int i=0;i<strlen(s);i++)
    {
      if(!b[s[i]])
      {
	b[s[i]]=-1;
	cnt++;
      }
    }
    if(cnt==1)
      cnt++;
    for(int i=0;i<strlen(s);i++)
      if(!i)
      {
	b[s[i]]=1;
	use[1]=true;
      }
      else
	if(b[s[i]]!=-1)
	  continue;
	else
	  for(int j=0;j<100;j++)
	    if(!use[j])
	    {
	      b[s[i]]=j;
	      use[j]=true;
	      break;
	    }
    long long p=1,ans=0;
    for(int i=strlen(s)-1;i>=0;i--)
    {
      ans+=p*b[s[i]];
      p*=cnt;
    }
    printf("Case #%d: %I64d\n",T,ans);
  }
  return 0;
}

