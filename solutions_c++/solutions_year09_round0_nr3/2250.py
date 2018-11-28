#include <cstdlib>
#include <iostream>

using namespace std;
int a[20];
char ch[]="welcome to code jam";
int main(int argc, char *argv[])
{
    freopen("code.in","r",stdin);
    freopen("code.out","w",stdout);
    int n; char  c;
    scanf("%d\n",&n);
    for (int t=0; t<n; t++)
    {
      memset(a,0,sizeof(a));
      a[19]=1;
      scanf("%c",&c);
      string s("");
      while (c!='\n') { s=s+c; scanf("%c",&c); };
       for (int i=s.length()-1; i>=0; i--)
      {
       for (int j=0; j<=18; j++)
       if (s[i]==ch[j]) 
        a[j]=(a[j]+a[j+1])%10000;
      }
      printf("Case #%d: %04d\n",t+1,a[0]);
       
    }
}
