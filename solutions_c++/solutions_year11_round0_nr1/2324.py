#include <cstdio>
#include <cstring>

const int maxn = 110;

int n;

char seqa[maxn];
int seqb[maxn];

int dis( int a, int b )
{
  return (a>b?a-b:b-a);
}

int main ()
{
  int cases,index;scanf("%d",&cases);
  for(index=0;index<cases;index++)
  {
    scanf("%d",&n);
    for(int i = 0; i < n; i ++ )
    {
      char s[2];
      scanf("%1s%d", s, seqb+i);
      seqa[i] = s[0];
    }
    int pa, pb;
    pa = pb = 1;
    int bufa, bufb;
    bufa = bufb = 0;
    int tm = 0;
    for(int i = 0; i < n; i ++ )
    {
      if( seqa[i] == 'O') 
      {
	int d = dis(seqb[i], pa)-bufa;
	bufa = 0;
	if( d < 0 ) d = 0;
	d++;
	bufb += d;
	tm += d;
	pa = seqb[i];
//	printf("(o->%d)",d);
      } else {
	int d = dis(seqb[i], pb)-bufb;
	bufb = 0;
	if( d < 0 ) d = 0;
	d++;
	bufa += d;
	tm += d;
	pb = seqb[i];
//	printf("(b->%d)",d);
      }
    }
    printf("Case #%d: %d\n",index+1, tm);
  }
  return 0;
}
