#define maxl 510
#define LenT 20
#include <iostream>
using namespace std;
char s[maxl];
char T[LenT] = "welcome to code jam";
int f[maxl], last[maxl], sum[maxl];
int len, n, ans;

void process(){
    memset(f, 0, sizeof f);
    len = strlen(s);
    for (int i=0;i<maxl;i++) last[i] = 1;
    for (int i=1;i<LenT;i++){
        sum[0]=0;
        memset(f, 0, sizeof f);
        for (int j=1;j<=len;j++){
            if (s[j-1]==T[i-1]) f[j] = last[j];
            sum[j] = (sum[j-1] + f[j])%10000;
        }
        memcpy(last,sum,sizeof(sum));
/*        for (int j=1;j<=len;j++) printf("%4d",j);printf("\n");
        for (int j=1;j<=len;j++) printf("%4d",last[j]);printf("\n");
        for (int j=1;j<=len;j++) printf("%4d",f[j]);printf("\n");
        printf("=================================\n");
*/
    }
}

void print(int c){
    printf("Case #%d: ",c);
    if (sum[len]<1000) printf("0");
    if (sum[len]<100) printf("0");
    if (sum[len]<10) printf("0");
    printf("%d\n",sum[len]);
}

int main(){
    scanf("%d",&n);
    getchar();
    for (int i=1;i<=n;i++){
        gets(s);
        process();
        print(i);
    }
}
