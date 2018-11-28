#include<cstring>
#include<cstdio>
//          'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
char m[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
int Q;
char str1[200];
int main()
{
  freopen("a.in", "r", stdin);
  freopen("a.out", "w", stdout);
  scanf("%d\n", &Q);
  for(int q = 1; q <= Q; q++)
  {
    gets(str1);
    for(int i = 0;;i++)
    {
      if(str1[i] == 0) break;
      if(str1[i] != ' ') str1[i] = m[str1[i]-97];
    }
    printf("Case #%d: %s\n", q, str1);
  }
  fclose(stdin);
  fclose(stdout);
  return 0;
}
