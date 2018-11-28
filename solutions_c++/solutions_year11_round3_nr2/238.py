#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <set>
#include <algorithm>
#include <cmath>

using namespace std;

int T, l, n, c;
long long total, t;
int a[1003];
int sorted[1000003];

int main(){
    //freopen("B.in", "r", stdin);
    //freopen("B.out", "w", stdout);
    scanf("%d", &T);
    for (int tc=1; tc<=T; tc++){
        total=0;

        scanf("%d %lld %d %d", &l, &t, &n, &c);
        for (int i=0; i<c; i++)
            scanf("%d", &a[i]);
        printf("Case #%d: ", tc);

        for (int i=0, j=0; i<n; i++, j=(j+1)%c){
            int curr=a[j];
            if ((total+curr)*2<=t){
                sorted[i]=0;
                total+=a[j];
                continue;
            }
            if (t>total*2 and t<(total+curr)*2)
                curr-=t/2-total;

            sorted[i]=curr;
            total+=a[j];
        }

        sort(sorted, sorted+n);

        total*=2;
        for (int i=n-1; i>=0 and l; i--, l--)
            total-=sorted[i];

        cout << total << endl;
    }
	return 0;
}
