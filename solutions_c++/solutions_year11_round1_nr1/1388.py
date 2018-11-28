#include<iostream>
#include<cstdio>
#include<vector>
using namespace std;

void doit(int test){
    printf("Case #%d: ",test);
    int n,pd,pg;
    scanf("%d%d%d",&n,&pd,&pg);
    for(int i = 1 ; i <= n ; i++){
        if( (pd*i % 100) != 0 ) continue;
        int gd = (pd*i)/100;
        int pd = i - gd;
        for(int j = i ; j <= 10000 ; j++){
            if( pg*j % 100 != 0 ) continue;
            int gg = (pg*j)/100;
            int gp = j - gg;
            if( gg >= gd && gp >= pd ){ puts("Possible"); return; }
        }
    }
    puts("Broken");
}

int main(){
    int t;
    scanf("%d",&t);
    for(int i = 1 ; i <= t ; i++) doit(i);
}
