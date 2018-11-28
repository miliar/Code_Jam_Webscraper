#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    int T;
    int N,a[1001],b[1000];

    cin >> T;
    for(int cc=1;cc<=T;cc++) {
        cin >> N;
        for(int i=0;i<N;i++) {
            cin >> a[i] >> b[i];
        }

        int cnt=0;
        for(int i=0;i<N;i++) {
            for(int j=i+1;j<N;j++) {
                if(a[i]<a[j] && b[i]>b[j]) cnt++;
                else if(a[i]>a[j] && b[i]<b[j]) cnt++;
            }
        }

        printf("Case #%d: %d\n", cc, cnt);
    }

    return 0;
}
