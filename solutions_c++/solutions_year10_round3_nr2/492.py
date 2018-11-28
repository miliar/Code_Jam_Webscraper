#include <stdio.h>
#include <algorithm>
#include <vector>
using namespace std;

long l,p,c;
vector<long> num,pw;

main()
{
  freopen("B-small-attempt0.in","r",stdin);
  freopen("file.out","w",stdout);
  long tc,t,l,p,c,i,cnt;
  
  pw.push_back(1);
  for(i=1;i<=31;i++)
    pw.push_back( pw[i-1]*2 );
    
  scanf("%d",&tc);
  for(t=1;t<=tc;t++)
  {
    num.clear();
    scanf("%d %d %d",&l,&p,&c);
    printf("Case #%d: ",t);
    
    if( l*c == p ) 
    {
      printf("0\n");
      continue;
    }
    
    num.push_back(l);
    while( num[ num.size()-1 ] < p )
      num.push_back( num[ num.size()-1 ]*c );
    cnt = (num.size()-2);
    
    for(i=0;i<=31;i++)
      if( cnt <= pw[i] )
      { 
        if(cnt==pw[i])i++;
        break;
      }
      
    printf("%d\n",i);
  }
}
