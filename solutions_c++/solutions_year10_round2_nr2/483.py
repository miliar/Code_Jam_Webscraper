#include <cstdio>
#include <cstdlib>

int cmp (const void *a1, const void *a2)
{
  int * a = (int *)a1;
  int * b = (int *)a2;
  
  if(*a < *b) return -1;
  if(*b < *a) return  1;
  else return 0;
}

int main(void)
{
  int tt, c = 1, n, k, b, t, x[64], v[64], swn[64], gc, tw, i, j;
  int vn, vj;
  
  scanf("%d", &tt);
  
  while(c <= tt)
  {
    
    scanf("%d %d %d %d", &n, &k,&b, &t);
    
    gc = 0;
    
    for(i = 0; i < n; i++)
    {
	scanf("%d", &x[i]);
    }

    for(i = 0; i < n; i++)
    {
	scanf("%d", &v[i]);
    }
    
    for(i = 0; i < n; i++)
    {
      vn = (b-x[i])/t;
      if((b-x[i])%t != 0) vn++;
     
      //printf("vn[i] = %d v[i] = %d\n", vn, v[i]);
     
      if(v[i] < vn) continue;
      
      tw = 0;
      
      for(j = i + 1; j < n; j++)
      {
	vj = (b-x[j])/t;
	if((b-x[j])%t != 0) vj++;	
	
	if(v[j] < vn && v[j] < vj) tw++;
      }
      
      //printf("swn[%d] = %d\n", gc, tw);
      
      swn[gc] = tw;
      gc++;
    }

    

    if(k > gc)
    {
      printf("Case #%d: IMPOSSIBLE\n", c++);
    }
    else
    {
      qsort(swn, gc, sizeof(int), cmp);
      
      tw = 0;
      for(i = 0; i < k; i++) tw += swn[i];
      
      printf("Case #%d: %d\n", c++, tw);
    }
  }
  
  return 0;
}