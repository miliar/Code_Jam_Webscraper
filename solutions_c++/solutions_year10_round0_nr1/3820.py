#include <stdio.h>
int main ()
{freopen("snap.in","r",stdin);
 freopen("snap.out","w",stdout);
 int t,i;
 unsigned n,k,aux;
 scanf("%d",&t);
 for (i=1;i<=t;i++)
 {scanf("%d %d",&n,&k);
  aux=((unsigned)1<<n)-1;
  if((aux&k)==aux)
  {printf("Case #%d: ON\n",i);
  }
  else
  {printf("Case #%d: OFF\n",i);
  }
 }
 return 0;
}
