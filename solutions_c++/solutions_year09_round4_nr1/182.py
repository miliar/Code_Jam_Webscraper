#include <cstdio>

#define MAX_N  40

int n;
int m[MAX_N];
char r[MAX_N+10];

void read_one_input()
{
  scanf("%d",&n);
  for(int i=0; i<n; i++) {
    scanf("%s",r);
    int mm = 0;
    for(int j=0; j<n; j++) 
      if(r[j]=='1')
	mm = j;
    m[i]=mm;
  }
}

void print_m()
{
  for(int i=0; i<n; i++)
    printf("%d",m[i]);
  printf("\n");
}

int do_sort()
{
  int count = 0;
  bool moved = false;
  do {
    //print_m();
    moved = false;
    for(int i=0; i<n-1; i++)
      if(m[i]>i) {
	// i'm bad... go find the first good one
	int j;
	for(j=i+1; j<n; j++)
	  if(m[j]<=i)
	    break;
	// have to move j to here
	int t = m[j];
	for(int k=j-1; k>=i; k--)
	  m[k+1] = m[k];
	m[i] = t;
	count += (j-i);
	moved = true;
      }
  } while(moved);
  return count;
}

main()
{
  int t;
  scanf("%d", &t);
  for(int tt=0; tt<t; tt++) {
    read_one_input();
    printf("Case #%d: %d\n",tt+1,do_sort());
  }
}
