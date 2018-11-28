#include <cstdio>
#include <vector>
#include <map>
#include <algorithm>

using namespace std ;

char squi[200];

int algo()
{
  int nb_r ;
  int pos[2] = {1,1};
  int date_bouge[2] = {0,0};
  int date_cur = 0;
  scanf("%d",&nb_r);
  for(int r = 0 ; r < nb_r ; r++ )
    {
      int ou ;
      scanf("%s %d\n",squi,&ou);
      int qui = squi[0]=='O' ;
      date_cur = max( date_cur , date_bouge[qui]+abs(ou-pos[qui]))+1;
      date_bouge[qui] = date_cur ;
      pos[qui] = ou ;
    }
  return date_cur;
}

int main()
{
  int nb_t ;
  scanf("%d",&nb_t);
  for(int t = 0 ;t<nb_t;++t)
    {
      printf("Case #%d: %d\n",t+1,algo());
    }
  return 0 ;
}
