#include <iostream>
using namespace std;

char s[1000];
char *key="welcome to code jam";
int H[1000][25];

main()
{
  int n; cin >> n; gets(s);
  int k=strlen(key);

  for(int line=1;line<=n;line++)
  {
    gets(s); int l=strlen(s);

    for(int i=0;i<k;i++) H[l][i]=0; H[l][k]=1;

    for(int i=l-1;i>=0;i--) for(int j=0;j<=k;j++)
    {
      H[i][j]=H[i+1][j];
      if (key[j]==s[i]) { H[i][j]+=H[i+1][j+1]; H[i][j]%=10000; }
    }
   
    printf("Case #%d: %04d\n", line, H[0][0]);
  }
}
