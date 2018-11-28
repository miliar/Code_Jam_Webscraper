#include <cstdio>
#include <cstring>
#define LL long long

int in[256];
int val[100];

int main()
{
  int tt;
  scanf("%d", &tt);
  for(int t=1;t<=tt;t++) {
    char tmps[100];
    scanf("%s", tmps);
    memset(in,-1,sizeof(in));
    int len=strlen(tmps);
    int base=1;
    val[0] = 1;
    in[tmps[0]] = 1;
    int cur=0;
    for(int i=1;i<len;i++)
      if(in[tmps[i]]==-1) {
	val[i] = cur;
	in[tmps[i]] = cur;
	if(cur==0) cur+=2;
	else cur++;
	base++;
      } else 
	val[i] = in[tmps[i]];
    
    /*printf("base = %d, val=", base);
    for(int i=0;i<len;i++) printf("%d", val[i]);
    printf("\n");*/
    printf("Case #%d: ", t);

    LL res=0;
    LL B = base;

    if(B==1) {
      for(int i=0;i<len;i++)
	{ res *=2; res++; }
      printf("%lld\n", res);
      continue;
    }

    res = val[0];
    for(int i=1;i<len;i++)
      { res *= base; res += (LL)val[i]; }
    printf("%lld\n",res);
    
  }
  return 0;
}
