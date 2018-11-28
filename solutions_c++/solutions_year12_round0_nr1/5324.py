#include <cstdio>
#include <cstring>

using namespace std;

char ans[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','q','t','n','w','j','p','f','m','a','z'};
int main()
{
  // // freopen("A.in","r",stdin);
  //  freopen("A.out","w",stdout);
      int data; char a[1000]; int z = 0;
      scanf("%d\n",&data);
      while (data--)
      {
          gets(a);
          printf("Case #%d: ",++z);
          for (int i=0; i<strlen(a); i++)
              if (a[i]>='a' && a[i]<='z') printf("%c",ans[a[i]-'a']);
                                     else printf("%c",a[i]);
          printf("\n");
      }
    return 0;
}
