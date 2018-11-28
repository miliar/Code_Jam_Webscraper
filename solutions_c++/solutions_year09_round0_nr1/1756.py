#include <cstdio>
#include <cstring>

int word_length;
int num_words;
int num_patterns;

char word[5000][16];
char pattern[140001];

bool allow[15][26];

void Preprocess()
{
  const int pattern_length = strlen(pattern);
  int  i,j,k(0);
  
  for ( i=0; i<15; ++i )
    for ( j=0; j<26; ++j )
      allow[i][j] = false;
  
  for ( i=0; i<pattern_length; ++i ) {
    if ( pattern[i]=='(' ) {
      for ( j=i+1; j<pattern_length; ++j )
        if ( pattern[j]==')' )
          break;
      while ( ++i<j )
        allow[k][pattern[i]-'a'] = true;
      i = j;
      ++k;
    }
    else allow[k++][pattern[i]-'a'] = true;
  }
  
  /*
  for ( k=0; k<word_length; ++k ) {
    printf("allow[%d]:",k);
    for ( i=0; i<26; ++i )
      if ( allow[k][i] )
        printf(" %c",i+'a');
    putchar('\n');
  }
   */
}

bool Match( char *str )
{
  int i;
  for ( i=0; i<word_length; ++i )
    if ( !allow[i][str[i]-'a'] )
      return false;
  return true;
}

int main()
{
  scanf("%d%d%d",&word_length,
                 &num_words,
                 &num_patterns);
  int i,j,match_cnt(0);
  for ( i=0; i<num_words; ++i ) scanf("%s",word[i]);
  for ( i=1; i<=num_patterns; ++i ) {
    scanf("%s",pattern);
    Preprocess();
    match_cnt = 0;
    for ( j=0; j<num_words; ++j ) {
//      printf("  Test %s (%s)\n",word[j],Match(word[j])?"Matched":"-");
      if ( Match(word[j]) )
        ++match_cnt;
    }
    printf("Case #%d: %d\n",i,match_cnt);
  }
}