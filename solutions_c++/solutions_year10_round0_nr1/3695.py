#include<iostream>
#include<cstdio>
#include<algorithm>
#include<string>
#include<cstring>
using namespace std;
int cal(int a,int b)
{
  if(b==1)
    return a;
  if(b==0)
    return 1;
  int p=cal(a,b/2);
  p*=p;
  if(b%2==1)
    p=p*a;
  return p;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("large.out","w",stdout);
  int T,t=1,i,k,fg,s,n;
  scanf("%d",&T);
  while(T--)
  {
    scanf("%d%d",&n,&k);
    if(k==0)
      fg=0;
    else
    {
        s=cal(2,n);
        fg=k%s==s-1;
    }
    printf("Case #%d: ",t++);
    if(fg==1)
      printf("ON\n");
    else
      printf("OFF\n");
  }
  //system("pause");
  return 0;
}
