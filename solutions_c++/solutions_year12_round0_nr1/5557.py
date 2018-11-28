/*a = y  b = h    c = e d = s e = o f = c g = v h = x i = d j = u k = i
    l = g  m = l     n = b o = k p = r q = z r = t s = n t = w u = j
    v = p w = f x = m    y = a z = q
*/
#include<stdio.h>
#include<string.h>

int k = 0;
const char word[26] = {'y','h','e','s','o','c','v','x','d','u','i',
                                    'g','l','b','k','r','z','t','n','w','j',
                                    'p','f','m','a','q'};

void work()
{
    char c;
    printf("Case #%d: ",++k);
    while(scanf("%c",&c), c != '\n')  if(c <= 'z' && c >= 'a') printf("%c",word[c-'a']);
                                                    else printf("%c",c);
    printf("%c",c);
}

int main()
{
  int n,c;
  freopen("GCJ_A.in","r",stdin);
  freopen("GCJ_A.out","w",stdout);
  scanf("%d%c%c",&n,&c,&c);
  while(n--) work();
  return 0;
}
