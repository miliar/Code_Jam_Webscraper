#include <cstdio>
using namespace std;

char t[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

int main()
{
    int a;
    scanf("%d\n", &a);
    for(int i = 1; i <= a; ++ i){
        printf("Case #%d: ", i);
        while(1){
            char s;
            scanf("%c", &s);
            if(s <= 'z' && s >= 'a')
                printf("%c", t[s-'a']);
            else printf("%c", s);
            if(s == 10) break;
        }
    }
}
