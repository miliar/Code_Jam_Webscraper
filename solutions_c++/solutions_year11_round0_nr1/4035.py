#include <stdio.h>
#include <vector>

using namespace std;

long n,m[200];
char ch[200];
bool fix[200];
vector<long> vo,vb;

int main()
{
  freopen("A-large.in","r",stdin);
  freopen("file.out","w",stdout);
  
  long i,j,t,o,b,op,bp,time,tc;
  
  scanf("%d",&t);
  
  for( tc = 1; tc <= t; tc++ )
  {
    vo.clear();
    vb.clear();
    //
    scanf("%d",&n);
    for( i=0;i<n;i++ )
    {
      fix[i] = false;
      scanf(" %c %d",&ch[i],&m[i]);
      if( ch[i]=='O' ) vo.push_back( m[i] );
                  else vb.push_back( m[i] );
    }
    
    op = bp = 1;
    o = b = 0; time = 0; i = 0;
    while(1)
    {
      time++;
      if( ch[i]=='O' )
      {
        if( op == m[i] )
        {
          fix[i] = true;
          i++;
          o++;
        }
        else
          op = ( op > m[i] )? op-1 : op + 1;
          
        if( b < vb.size() )
        {
          if( bp > vb[b] ) bp--;
          else if( bp < vb[b] ) bp++;
        }
      }
      else
      {
        if( bp == m[i] )
        {
          fix[i] = true;
          i++;
          b++;
        }
        else
          bp = ( bp > m[i] )? bp-1: bp +1;
        
        if( o < vo.size() )
        {
          if( op > vo[o] ) op--;
          else if( op < vo[o] ) op++;
        }
      }
      if( fix[n-1] ) break;
    }
    
    
    printf("Case #%d: %d\n",tc,time);
    
    //
  }
  
  
  return 0;
}
