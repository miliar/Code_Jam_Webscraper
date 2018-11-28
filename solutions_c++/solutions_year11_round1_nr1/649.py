#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;


long long n,a,b;
bool check(){
    if(b==100)   return a==100;
    if(b==0)     return a==0;
    if(n >= 100) return 1;

    for(int i=1;i<=n;i++){
        if(a*i%100 == 0)return 1;
    }
    return 0;
}

int main(){
    int T,cas=1;
    scanf("%d",&T);
    while(T--){
        cin >> n >> a >> b;

        if(check()){
            printf("Case #%d: Possible\n",cas++);
        }else{
            printf("Case #%d: Broken\n",cas++);
        }
    }
    return 0;
}

