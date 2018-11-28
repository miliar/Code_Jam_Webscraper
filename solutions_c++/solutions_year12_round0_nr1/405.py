#include <cstdio>
#include <cstring>

const int MAXN = 27;
const int MAXL = 101;
const char change[MAXN] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

int N , len;
char str[MAXL];

int main () {
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    
    scanf("%d\n",&N);
    for (int i = 0;i < N;i++) {
        printf("Case #%d: ",i+1);
        gets(str);
        len = strlen(str);
        for (int j = 0;j < len;j++)
          if (str[j] >= 'a' && str[j] <= 'z')
            str[j] = change[str[j]-'a'];
        printf("%s\n",str);
    }
    return 0;
}
