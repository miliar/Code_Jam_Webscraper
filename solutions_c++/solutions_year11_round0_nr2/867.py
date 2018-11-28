#include <cstdio>
#include <vector>
#include <map>
#include <algorithm>

using namespace std ;

char cur[200];
char buf[200] ;
int taille ;
map<pair<char,char>,char> combine ;
map<pair<char,char>,bool> oppose ;

void ajoute (char lettre)
{
  cur[taille++] = lettre ;
  if( taille==1 )
    return ;
  const char c =  combine[make_pair(cur[taille-1],cur[taille-2])] ; 
  if( c )
    {
      taille-=2;
      ajoute(c);
      return ;
    }
  for( int i = 0 ; i < taille ; i++ )
    if( oppose[make_pair(cur[taille-1],cur[i])] )
      taille = 0 ;
}

int main()
{
  int nb_t ;
  scanf("%d",&nb_t);
  for(int t = 0 ;t<nb_t;++t)
    {
      int nb_combi ;
      scanf("%d",&nb_combi);
      for(int q = 0 ; q < nb_combi ; q++)
        {
          scanf("%s",buf);
          combine[make_pair(buf[0],buf[1])] = buf[2] ;
          combine[make_pair(buf[1],buf[0])] = buf[2] ;
        }
      int nb_opp ;
      scanf("%d",&nb_opp);
      for(int q = 0 ; q < nb_opp ; q++)
        {
          scanf("%s",buf);
          oppose[make_pair(buf[0],buf[1])] = true ;
          oppose[make_pair(buf[1],buf[0])] = true ;
        }
      scanf("%d",&nb_opp);
      scanf("%s",buf);
      for( int i = 0 ; i < nb_opp ; i++ )
        ajoute(buf[i]);
      printf("Case #%d: [",t+1);
      for(int i = 0 ; i< taille - 1 ; i++ )
        printf("%c, ",cur[i]);
      if(taille)
        printf("%c",cur[taille-1]);
      printf("]\n");
      taille = 0 ;  
      combine.clear();
      oppose.clear();
    }
  return 0 ;
}
  
