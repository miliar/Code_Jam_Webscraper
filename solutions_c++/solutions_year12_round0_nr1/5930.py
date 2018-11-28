#include <cstdio>
#include <cstring>
#include <cctype>

using namespace std;

int main(){
    freopen( "A-small-attempt0.in", "r", stdin );
	freopen( "output.txt", "w", stdout );

    int size, N, teste=0;
    char c[110];
    char alfabeto[] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

    scanf("%d", &N);int bkpn = N;char a; scanf("%d",&a);

    while(N--){
        size = strlen(gets(c));
        printf("Case #%d: ", ++teste);
        for(int i = 0; i < size; i++){
            if(isalpha(c[i])){printf("%c", alfabeto[int(c[i]-97)]);}
            else{printf("%c",c[i]);}
        }
        if(teste!=bkpn)putchar('\n');
        //printf("%d",size);
    }

    return 0;
}
