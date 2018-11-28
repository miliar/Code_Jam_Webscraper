#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>

using namespace std;

int arr[2000010];
bool isin(vector<int> a, int b){
    for(int i = 0; i < a.size(); i++){
        if(b == a[i]) return 1;
    }
    return 0;
}
int fun(int a2, int bb){
    vector<int> cmp;
    int count = 0;
    int weisu[9];
    int i = 0, wei = 0;
    int a1 = a2;
    int a = a1;
    while(a){
        weisu[i] = a%10;
        a/=10;
        wei++;
        i++;
    }
    //for(int i = 0; i < wei; i++) printf("wei %d\n", weisu[i]);
    for(int i = 0; i < wei - 1;i++){
        int c = a1/10;
        int b= a1%10;
        a1 = c + weisu[i]*(int)(pow(10.0, (wei - 1)*1.0));
        if(a1 > a2 && a1 <= bb && !isin(cmp, a1)){
            count++;cmp.push_back(a1);
        }
    }
    return count;
}
int main(){
    #ifdef LOCAL
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    #endif
	int t;
	while(scanf("%d", &t) != EOF){
	    int aa;
	   // aa = fun(123, 3000);
	   // printf("aa:%d ", aa);

        for(int i = 1; i <= t; i++){
            int a, b;
            scanf("%d%d", &a, &b);
            if(b <= 11){
                printf("Case #%d: %d\n",i,0);
            }
            else{
                int sum = 0;
                for(int j = a; j <= b; j++){
                    //if(fun(j, b)) printf("maz:%d  count:%d\n", j, fun(j,b));
                    sum+=fun(j,b);
                }
                printf("Case #%d: %d\n",i, sum);
            }
        }
	}
	return 0;
}
