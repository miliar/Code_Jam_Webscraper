#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
using namespace std;
char map[30]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
int main(){
    //freopen("A-small-attempt2.in", "r", stdin);
    //freopen("A-small-attempt2.out", "w", stdout);
    int i, cas=1, T;
    char str[200];
    scanf("%d", &T);
    getchar();
    while(T--){
        gets(str);
        printf("Case #%d: ", cas++);
        for(i=0; str[i]!='\0'; i++){
            if(str[i]>='a'&&str[i]<='z')
                printf("%c", map[str[i]-'a']);
            else printf("%c", str[i]);
        }
        printf("\n");
    }
    return 0;
}
