#include <cstdio>
#include <cstdlib>

using namespace std;

char translate[26];

char mapping( char c ) {
  if( c == ' ' ) return ' ';

  return translate[c-'a'];  
}

int main(int argc, char *argv[]) {

  int T;
  char line[128];

  //Set mapping values
  translate['a'-'a'] = 'y';
  translate['b'-'a'] = 'h';
  translate['c'-'a'] = 'e';
  translate['d'-'a'] = 's';
  translate['e'-'a'] = 'o';
  translate['f'-'a'] = 'c';
  translate['g'-'a'] = 'v';
  translate['h'-'a'] = 'x';
  translate['i'-'a'] = 'd';
  translate['j'-'a'] = 'u';
  translate['k'-'a'] = 'i';
  translate['l'-'a'] = 'g';
  translate['m'-'a'] = 'l';
  translate['n'-'a'] = 'b';
  translate['o'-'a'] = 'k';
  translate['p'-'a'] = 'r';
  translate['q'-'a'] = 'z';
  translate['r'-'a'] = 't';
  translate['s'-'a'] = 'n';
  translate['t'-'a'] = 'w';
  translate['u'-'a'] = 'j';
  translate['v'-'a'] = 'p';
  translate['w'-'a'] = 'f';
  translate['x'-'a'] = 'm';
  translate['y'-'a'] = 'a';
  translate['z'-'a'] = 'q';

  //Read number of test cases
  scanf("%d", &T); getchar();
  for(int t=1; t<=T; t++) {

    //Read line
    fgets(line, 128, stdin);

    int i=0;
    while( line[i] && line[i] != '\n' ) {
      line[i] = mapping( line[i] );
      i++;
    }
    line[i] = '\0';

    printf("Case #%d: %s\n", t, line);
  }

  return 0;
}
