#include <cstdio>
#include <queue>
using namespace std;
queue<int> b,a[20];
FILE *in, *out;
int p[20];
char s[30];
void move(int x)
{
  if (p[x]==a[x].front())
    return;
  if (p[x] < a[x].front())
    p[x]++;
  if (p[x] > a[x].front())
    p[x]--;
}
int main()
{
  int n,i,t,T,q,time,x;
  in=fopen("robot_trust.in","r");
  out=fopen("robot_trust.out","w");
  fscanf(in,"%d",&T);
  for (t=1;t<=T;t++)
  {
    fscanf(in,"%d",&n);
    for (i=1;i<=n;i++)
    {
      fscanf(in,"%s %d",s,&x);
      if (s[0]=='O')
      {
        a[0].push(x);
        b.push(0);
      }
      else
      {
        a[1].push(x);
        b.push(1);
      }
    }
    p[0]=p[1]=1;
    time=0;
    while(!b.empty())
    {
      time++;
      q=b.front();
      move(!q);
      if (a[q].front()==p[q])
      {
        b.pop();
        a[q].pop();
        continue;
      }
      move(q);
    }
    fprintf(out,"Case #%d: %d\n",t,time);
  }
  fclose(in);
  fclose(out);
  return 0;
}
