#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std;

int main(){
    int z;
    scanf("%d", &z);
    for(int j=1; j<=z; j++){
        int n;
        scanf("%d", &n);
        int x=0, a, min=-1;
        int sum=0;
        for(int i=0; i<n; i++){
            scanf("%d", &a);
            x^=a;
            sum+=a;
            if(min==-1 || a < min){
                min = a;
            }
        }
        printf("Case #%d: ", j); 
        if(x==0){
            printf("%d\n", sum-min);
        }else{
            printf("NO\n");
        }
    }
    return 0;
}
