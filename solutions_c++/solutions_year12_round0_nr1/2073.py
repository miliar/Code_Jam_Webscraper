#include <cstdio>
#include <string>
using namespace std;
const int MAXL = 100;

char buff[MAXL+1];
const char mapping[27] = {"yhesocvxduiglbkrztnwjpfmaq"};

int main()
{
  int T; scanf("%d\n", &T);
  for( int t_case = 0; t_case < T; ++t_case ) {
    gets(buff);
    
    for( int i = 0; buff[i]; ++i ) 
      if (buff[i] != ' ')
	buff[i] = mapping[buff[i]-'a'];

    printf( "Case #%d: %s\n", t_case + 1, buff);
  }
  return 0;
}
