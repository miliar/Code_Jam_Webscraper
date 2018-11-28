#include<cstdio>
#include<cstdlib>
#include<cstring>
using namespace std;

const char a[20]="welcome to code jam";
int f[503][23];
bool b[503][23];
char s[10000];
int N,len;

int T(int x,int y)
{
  if(x==len)
    if(y==19)
      return 1;
    else
      return 0;
  if(!b[x][y])
  {
    b[x][y]=true;
    if(s[x]==a[y])
      f[x][y]=(T(x+1,y+1)+T(x+1,y))%10000;
    else
      f[x][y]=T(x+1,y)%10000;
  }
  return f[x][y];
}

int main()
{
  freopen("C.in","r",stdin);
  freopen("C.out","w",stdout);
  scanf("%d\n",&N);
  for(int i=1;i<=N;i++)
  {
    gets(s);
    len=strlen(s);
    memset(b,0,sizeof(b));
    memset(f,0,sizeof(f));
    printf("Case #%d: ",i);
    int ans=T(0,0);
    if(ans<1000)
      putchar('0');
    if(ans<100)
      putchar('0');
    if(ans<10)
      putchar('0');
    printf("%d\n",ans);
  }
  return 0;
}

