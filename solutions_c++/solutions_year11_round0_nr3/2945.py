#include <iostream>
#include <cstdio>
using namespace std;
const int MAXN = 20;
int t, n, Digit[MAXN];
int Judge(int &v, int j)
{
    int num1 = 0, num2 = 0, flag1 = 0, flag2 = 0;
    int x = 0, y = 0;
    for(int i = 0; i < n; i++){
        if((1<<i) & j){
            x += Digit[i];
            if(flag1){
                num1 ^= Digit[i];
            }else {
                num1 = Digit[i];
                flag1 = 1;
            }
        }else{
            y += Digit[i];
            if(flag2){
                num2 ^= Digit[i];
            }else{
                num2 = Digit[i];
                flag2 = 1;
            }
        }
    }
    if(!flag1 || !flag2){
        return 0;
    }else {
        if(num1 == num2){
            v = max(x, y);
            return 1;
        }else return 0;
    }
}
int main()
{
    int value, flag, con = 1;
    int v;
    //freopen("input.txt", "r", stdin);
    //freopen("out.txt", "w", stdout);
    scanf("%d", &t);
    while(t--){
        scanf("%d", &n);
        for(int i = 0; i < n; i++)
            scanf("%d", &Digit[i]);
        flag = 0;
        v = 0;
        printf("Case #%d: ", con++);
        for(int i = 0; i < (1<<n); i++){
            if(Judge(value, i)){
                flag = 1;
                if(v < value){
                    v = value;
                }
            }
        }
        if(!flag) printf("NO\n");
        else printf("%d\n", v);
    }
    return 0;
}
