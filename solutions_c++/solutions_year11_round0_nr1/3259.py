#include <stdio.h>
#include <stdlib.h>

#define ABS(x) ((x)>=0?(x):-(x))

int size(int n)
{
  int ret = 0;
  do { n/=10; ret++; } while(n>0);
  return ret;
}

const char* read_number( const char *p, int &n )
{
  if(!*p)
    return NULL;

  n = atoi(p);
  p += size(n)+1;

  if(!*p)
    return NULL;
  return p;
}

int solve( const char *string )
{
  int n = 0;

  const char *p = read_number(string, n);
  int sum=0, partial_sum=0;
  char code='.'; // current code
  int cur_pos[2] = { 1, 1 };
  int curp =1;
  while( p )
  {
    while( p && *p == code )
    {
       int next_pos;
       p = read_number(p+2, next_pos);
       partial_sum += 1+ ABS(next_pos-curp);
       curp = next_pos;
    }

    if( !p )
      break;

    // new code
    cur_pos[code=='O'] = curp;
    int next_pos;
    code = *p;
    p = read_number(p+2, next_pos);
    curp = cur_pos[code=='O'];
    int move = ABS(next_pos-curp);
    move -= partial_sum;
    sum += partial_sum;
    partial_sum = 1+ (move>0?move:0);
    curp = next_pos;
  }

  sum += partial_sum;
  //printf( "sum=%d\n", sum );
  return sum;
}

int main(void)
{
  char buf[2048];
  fgets(buf, 2048, stdin);
  int count;
  read_number(buf, count);
  for( int i=0; i<count; i++ )
  {
    fgets(buf, 2048, stdin);
    int sum = solve(buf);
    printf( "Case #%d: %d\n", i+1, sum );
  }

  return 1;
}
