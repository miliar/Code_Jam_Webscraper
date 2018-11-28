#include<cstdio>
#include<cstdlib>
using namespace std;

int main() {
    int t;
    int n;
    int arr[1010];
    scanf(" %d", &t);
    for(int i=0;i<t;i++) {
        scanf(" %d", &n);
        int max = -1;
        int min = 10000000;
        int pmax = 0;
        int pmin = 0;
        int total = 0;
        for(int j=0;j<n;j++) {
            scanf(" %d", &arr[j]);
            if(arr[j] > max) {
                max = arr[j];
                pmax = j;
            }
            if(arr[j] < min) {
                min = arr[j];
                pmin = j;
            }
            total += arr[j];
        }
        bool flag = true;
        while(arr[pmax]) {
            int temp = 0;
            for(int j=0;j<n;j++){
                if(arr[j] & 1){
                    temp++;
                }
                arr[j] >>= 1;
            }
            if(temp % 2) {
                flag = false;
                break;
            }
        }
        if(flag == false) {
            printf("Case #%d: NO\n", i+1);
        } else {
            printf("Case #%d: %d\n", i+1, total - min);
        }
    }
    return 0;
}

