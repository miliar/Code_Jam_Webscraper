#include<iostream>
#include<sstream>
using namespace std ;

int convert(int n,int base)
{
 int t,ret = 0 ;
 while(n)
 {
  t = n%base ;
  ret += t*t ;
  n /= base ;
 }
 return ret ;
}

int base ;
char vis[20000000] ;
bool check(int k)
{
 if(k == 1) return 1 ;
 if(vis[k] == -2) return 0 ;
 if(vis[k] != -1) return vis[k] ;
 vis[k] = -2 ;
 return vis[k] = check(convert(k,base)) ;
}


bool Vis[11][12000000] ;
int get(int a[],int sz)
{
 int i,j ;
 for(i=2;i<12000000;i++)
 {
  for(j=0;j<sz;j++) if(!Vis[a[j]][i]) break ;
  if(j == sz) return i ;
 }
 return -1 ;
}

char ss[100000] ;
main()
{
 int i,j,k,runs ;
 
 for(base=2;base<=10;base++)
 {
  memset(vis,255,sizeof vis) ;
  for(j=2;j<12000000;j++) Vis[base][j] = check(j) ;
 }
 cout << "here" << endl ;
 
 freopen("in.in","r",stdin) ;
 freopen("out.txt","w",stdout) ;
 scanf("%d\n",&runs) ;
 for(int t=1;t<=runs;t++)
 {
  bool use[20] ;
  memset(use,0,sizeof use) ;
  gets(ss) ;
  istringstream iss(ss) ;
  while(iss >> k) use[k] = true ;
  int a[20],sz = 0 ;
  for(i=2;i<=10;i++) if(use[i]) a[sz++] = i ;
  int ret = get(a,sz) ;
  printf("Case #%d: %d\n",t,ret) ;
 }
// while(1) ;
}
