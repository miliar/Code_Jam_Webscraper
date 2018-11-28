#include<algorithm>
#include<cstdio>
#include<iostream>
#include<string>
#include<vector>
#include<string.h>
#include<set>
#include<map>
#define taskname ""
#define sqr(a) (a)*(a)
#define forn(i,n) for(int i=0;i<(int)n;i++)
using namespace std;
#define N 1000
double p[N];
char s[N][100];
void read(int n)
{
  scanf(" (  %lf %c",&p[n],&s[n][0]);
  if(s[n][0]==')')
    return;
  int j=0;
  while(s[n][j]>32)
	scanf("%c",&s[n][++j]);
  s[n][j]=0;
  //cerr<<n<<' '<<s[n]<<' '<<p[n]<<endl;
  read(2*n);
  read(2*n+1);
  scanf(" ) ");
    /*char temp;
	scanf(" %c",&temp);
	cerr<<temp;
*/
}
char tmp[N][100];
int m;
double solve(int a,double pr)
{ 
  pr*=p[a];
  if(s[a][0]==')')
	return pr;
  for(int i=0;i<m;i++)
    if(!strcmp(s[a],tmp[i]))
      return solve(a*2,pr);
  return solve(a*2+1,pr);
}
int main()
{
  int n,k;
  freopen(taskname"in","r",stdin);
  freopen(taskname"out","w",stdout);
  scanf("%d",&n);
  for(int i=1;i<=n;i++)
  {
    scanf("%*d");
    read(1);
    scanf("%d",&k);
	  printf("Case #%d:\n",i);
    for(int j=0;j<k;j++)
    {
      scanf("%*s %d ",&m);
      forn(q,m)
        scanf("%s ",tmp[q]);
      printf("%.6lf\n",solve(1,1));
    }
  } 
  return 0;
}