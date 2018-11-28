#include <cstdio>
#include <cstring>

const char *pattern = "welcome to code jam";
const int   pattern_length = strlen(pattern);

char text[501];
int  text_length;

int cnt;

void Search( const int t, const int p )
{
  if ( p==pattern_length ) {
    ++cnt;
    if ( cnt==10000 ) cnt = 0;
    return;
  }
  else {
    int i;
    for ( i=t; i<text_length; ++i )
      if ( text[i]==pattern[p] )
        Search(i+1,p+1);
  }
}

int Solve()
{
  text_length = strlen(text);
  cnt = 0;
  Search(0,0);
  return cnt;
}

int main()
{
  int num_cases,i;
  fgets(text,sizeof(text),stdin);
  sscanf(text,"%d",&num_cases);
  for ( i=1; i<=num_cases; ++i ) {
    fgets(text,sizeof(text),stdin);
    printf("Case #%d: %04d\n",i,Solve());
  }
}
