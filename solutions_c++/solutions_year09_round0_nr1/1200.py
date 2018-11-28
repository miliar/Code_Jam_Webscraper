#include <stdio.h>
#include <cstring>

char s[5005][20], t[1000000]; 
int a[20][30];

int main(void)
{
  freopen("a.in", "r", stdin);
  freopen("a.out", "w", stdout);

  int tn, nt, i, l, n, j;
  scanf("%d%d%d\n", &l, &n, &nt);
  for (i=0; i<n; i++)
    gets(s[i]);

  for (tn=0; tn<nt; tn++)
  {
    memset(a, 0, sizeof(a));
    gets(t);
    for (i=j=0; t[i]; j++, i++)
      if (t[i]=='(') 
        for (i++; t[i]!=')'; i++) 
          a[j][t[i]-'a']=1;
      else
        a[j][t[i]-'a']=1;

    int ans=0;
    for (i=0; i<n; i++)
    {
      for (j=0; j<l; j++)
        if (!a[j][s[i][j]-'a']) break;
      ans+=(j==l);
    }
      
    printf("Case #%d: %d\n", tn+1, ans);
  }

  return 0;
}