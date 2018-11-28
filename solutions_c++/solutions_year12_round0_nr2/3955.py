#include <iostream>
#include <cstdio>
using namespace std;

int x[31] = {0,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,9,9,9,10,10,10};
int y[31] = {0,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,9,9,9,10,10,10,10,10};
int a[100];

int ni(){
    int v;
    scanf("%d", &v);
    return v;
}

int main(){
    freopen("input.txt","r", stdin);
    freopen("output.txt","w", stdout);

    int t = ni();
    for(int i = 0; i < t; i++){
        int N = ni();
        int S = ni();
        int P = ni();
        for(int j = 0; j < N; j++){
            a[j] = ni();
        }
        int ans = 0;
        for(int j = 0; j < N; j++){
            if(x[a[j]] >= P){
                 ans++;
            }
            else if(S > 0 && y[a[j]] >= P){
                S--;
                ans++;
            }
        }
        printf("Case #%d: %d\n", i+1,ans);
    }
}
