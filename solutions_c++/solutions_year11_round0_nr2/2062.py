#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

char magic [30][30];
bool oppose[30][30];
char stack[1024]; int sz = 0;
int in[30];
char s[1024];
int n;
void solve ()
{
  int i, j;
  for (i = 0; i < 30; i ++)
  {
	in[i] = 0;
	for (j =0; j < 30; j ++)
	{
	  
	  magic[i][j] = '$';
	  oppose[i][j] = 0;
	}
  }
  sz = 0; 
  
  int k; 
  char buf[5];
  scanf("%d", &k);
  for (i =0 ; i < k; i ++)
  {
	scanf ("%s", buf);
	magic [buf[0] - 'A'] [buf[1] - 'A'] = buf[2];
	magic [buf[1] - 'A'] [buf[0] - 'A'] = buf[2];
	
  }
  
  scanf("%d", &k);
  for (i =0 ; i < k; i ++)
  {
	scanf ("%s", buf);
	oppose [buf[0] - 'A'] [buf[1] - 'A'] = true;
	oppose [buf[1] - 'A'] [buf[0] - 'A'] = true;
  }
  
  scanf ("%d%s", &n, s);
  for (i = 0; i < n; i ++)
  {
	stack [ sz ++ ] = s[i];
	in [s[i] - 'A'] ++;
	if (sz >=2 && magic[stack[sz-1] - 'A'][stack[sz-2] - 'A'] != '$')
	{
	  in [stack[sz-1] - 'A'] --;
	  in [stack[sz-2] - 'A'] --;
	  stack [sz - 2] = magic[stack[sz-1] - 'A'][stack[sz-2] - 'A'];
	  sz --;
	  in [stack[sz - 1] -'A'] ++;
	  
	}
	for (j = 0; j < 30; j ++)
	{
	  if (in[j] > 0 && oppose [j][stack[sz-1] - 'A'])
	  {
		sz = 0;
		for (k = 0; k < 30; k ++)
		  in[k] = 0;
	  }
	}
  }
  
  printf ("[");
  for (i = 0; i < sz; i ++)
  {
	if (i!=0) printf (", ");
	printf ("%c", stack[i]);
  }
  printf ("]\n");
}

int main ()
{
  
  int t;
  scanf ("%d", &t);
  
  for (int i = 1; i <= t; i ++)
  {
	
	printf ("Case #%d: ", i);
	solve ();
	
  }
  
  return 0;
}