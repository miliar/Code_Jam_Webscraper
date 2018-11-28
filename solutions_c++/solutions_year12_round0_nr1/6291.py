#include<cstdio>
#include<cstring>
#include<algorithm>
#define LL long long
#define pii pair<int, int>
using namespace std;
int n,a[30]={ 'y','h','e','s','o','c','v','x','d','u',
              'i','g','l','b','k','r','z','t','n','w',
              'j','p','f','m','a','q'},c;
char b[110];                                        

int main(){
    scanf("%d\n",&n);
    for (int i=1;i<=n;i++){
        gets(b);
        c=strlen(b);
        printf("Case #%d: ",i);
        for (int j=0;j<c;j++)
            printf("%c",a[b[j]-97]);
        printf("\n");
        }
    return 0;
}
