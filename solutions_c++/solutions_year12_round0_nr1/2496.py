#include <cstdio>
#include <algorithm>

using namespace std;
char mapa[26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
char linha[200];

int main()
{
  int casos;
  scanf("%d ", &casos);
  for(int h = 1; h <= casos; h++){
    gets(linha);
    printf("Case #%d: ", h);
    for(int i = 0; linha[i]; i++){
      putchar((('a' <= linha[i] && linha[i] <= 'z') 
	       ? mapa[(int)linha[i]-'a'] : linha[i]));
    }
    printf("\n");
  }
  return 0;
}
