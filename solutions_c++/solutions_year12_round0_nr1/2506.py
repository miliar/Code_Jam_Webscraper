#include <cstdio>
#include <vector>
#include <map>
#include <unordered_map>
#include <algorithm>

using namespace std ;

const char * clair [8] = 
  {
    "ejp mysljylc kd kxveddknmc re jsicpdrysi",
    "our language is impossible to understand",
    "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
    "there are twenty six factorial possibilities",
    "de kr kd eoya kw aej tysr re ujdr lkgc jv",
    "so it is okay if you want to just give up",
    "y qee",
    "a zoo"
  };

map<char,char> trad ;
bool pris[256] ;

void algo()
{
  char v [200];
  fgets(v,200,stdin);
  char * c = v ;
  //  printf("\n%s",v);
  while(*c)
    {
      if(*c <= 'z' && *c >= 'a' )
	printf("%c",trad[*c]);
      else
	if( *c == ' ' )
	  printf(" ");
      c++;
    }
}


int main()
{
  int t;
  for( int i = 0 ; i < 8 ; i+= 2 )
    {
      const char * a = clair[i] ;
      const char * b = clair[i+1];
      while(*a && *b)
	{
	  trad[*a] = *b;
	  pris[*b] = true ;
	  a++ ;
	  b++;
	}
    }
 
  for( int i = 'a' ; i <= 'z' ; i++ )
    if( trad.find(i) == trad.end() )
      for( int c = 'a'; c <= 'z' ; c++ )
	if( !pris[c])
	  trad[i] = c ;



  scanf("%d\n",&t);
  for(int i = 1 ; i <= t ; i++ )
    {
      printf("Case #%d: ",i);
      algo();
      printf("\n");
    }
  return 0;
}
