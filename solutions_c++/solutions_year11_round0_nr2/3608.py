#include <stdio.h>
#include <vector>
#include <map>

using namespace std;

char comb[300][300],list[300],l;
char core[8] = { 'Q','W','E','R','A','S','D','F' };
vector<char> oppose[300];
map<char,int> isinlist;
long n,d,c;

int main()
{
  freopen("B-large.in","r",stdin);
  freopen("file.out","w",stdout);
  long i,j,t,tc;
  char ch1,ch2,ch3;
  scanf("%d",&t);
  
  for( tc=1; tc<=t; tc++ )
  {
  //
  
    for(i=0;i<300;i++)
    {
      oppose[i].clear();
      for( j=0;j<300;j++ )
        comb[i][j] = 0;
    }
    isinlist.clear();
    
    scanf("%d ",&c);
    for( i=0; i<c; i++ )
    {
      scanf("%c%c%c ",&ch1,&ch2,&ch3);
      comb[ch1][ch2] = ch3;
      comb[ch2][ch1] = ch3;
    }
    
    scanf("%d ",&d);
    for( i=0; i<d ; i++ )
    {
      scanf("%c%c ",&ch1,&ch2);
      oppose[ch1].push_back( ch2 );
      oppose[ch2].push_back( ch1 );
    }
    
    scanf("%d ",&n); l = 0;
    for( i=0; i<n; i++ )
    {
      scanf("%c",&ch1);
      list[l] = ch1;
      l++;
      if( l > 1 )
      {
        if( comb[ch1][ list[l-2] ] != 0 )
        {
          isinlist[ list[l-2] ]--;
          ch1=comb[ch1][ list[l-2] ];
          list[l-2]=ch1;
          l--;
          isinlist[ch1]++;
          continue;
        }
        isinlist[ch1]++;
        for( j=0; j<oppose[ch1].size(); j++ )
          if( isinlist[ oppose[ch1][j] ] > 0 )
          {
            l = 0; isinlist.clear(); break;
          }
      } else isinlist[ch1]++;
    }
    
    printf("Case #%d: [",tc);
    
    if( l > 0 )
    {
      printf("%c",list[0]);
      for( i=1; i<l; i++ )
        printf(", %c",list[i]);
    }
    
    printf("]\n");
  //  
  }
  
  return 0;
}
