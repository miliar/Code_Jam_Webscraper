#include<stdio.h>
#include<string.h>
#include<sstream>
using namespace std;

bool flag[1000][12], app[1000];
int s[100];
int ans[2000];
char str[1000];

bool check(int n, int b)
{
    int top, i;

    memset(app, 0, sizeof(app));
    
    while(1){
        top=0;
        app[n]=1;
        while(n>0){
            s[top++]=n%b;
            n/=b;
        }
        for(i=0; i<top; i++) n+=s[i]*s[i];
        if(n==1) return 1;
        if(app[n]) return 0;
    }
}

bool check2(int n, int b)
{
    int top, sum, i;
    
    top=0;
    while(n>0){
        s[top++]=n%b;
        n/=b;
    }
    sum=0;
    for(i=0; i<top; i++) sum+=s[i]*s[i];
    if(sum==1) return 1;
    return flag[sum][b];
}

int main()
{
//    freopen("a.in", "r", stdin);
//    freopen("a.out", "w", stdout);

    freopen("table.std", "w", stdout);

    int n, b, t, cc, ct, i;
    stringstream ss;

    memset(flag, 0, sizeof(flag));

    for(n=2; n<1000; n++)
        for(b=2; b<=10; b++)
            if(check(n, b)) flag[n][b]=1;
    
    memset(ans, 0, sizeof(ans));
    
    n=1;
    while(ans[(1<<9)-1]==0){
       n++;
       t=0;
       for(b=2; b<=10; b++)
        if(check2(n, b)) t=t|(1<<(b-2));
        for(i=t; i; i=(i-1)&t)
            if(ans[i]==0) ans[i]=n; 
    }
    
    for(t=0; t<(1<<9); t++) printf("%d %d\n", t, ans[t]);
    
//    printf("%d %d\n", flag[3][2], flag[3][3]);
    
/*    scanf("%d", &cc);
    gets(str);
    for(ct=1; ct<=cc; ct++){
        gets(str);
        ss.clear();
        ss<<str;
        t=0;
        while(ss>>b) t=t|(1<<(b-2));//, printf("%d ", b);
//        printf("\n%d\n", t);
        printf("Case #%d: %d\n", ct, ans[t]);
    }*/

    return 0;
}
