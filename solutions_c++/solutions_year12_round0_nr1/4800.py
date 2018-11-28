#include <iostream>
#include <string.h>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <ctime>
#include <queue>
#include <map>
#define pb push_back
#define MAXN 1
#define MAXM 1
#define INF (1<<30)
#define PI 3.1415926535898
#define esp 10e-6
const int dx[4]={1,0,-1,0};
const int dy[4]={0,-1,0,1};
using namespace std;
char ch[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l',
                 'b','k','r','z','t','n','w','j','p','f','m','a','q'};
class Point
{
      public:
             int x;
             int y;
};

int work()
{
    char str[10001];
    memset(str,0,sizeof(str));
    gets(str);
    for (int i=0;i<strlen(str);++i)
        if (str[i]>='a' && str[i]<='z')
        printf("%c",ch[str[i]-'a']);
        else 
        printf("%c",str[i]);
    printf("\n");
    return 0;
}

int main()
{
    freopen("A-small-attempt0.in","r",stdin);freopen("output.txt","w",stdout);
    int T;
    scanf("%d",&T);
    getchar();
    for (int i=1;i<=T;++i)
        {
        printf("Case #%d: ",i);
        work();
        }
    return 0;
}
