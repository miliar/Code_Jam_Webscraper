#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <set>
#include <algorithm>
#include <cmath>

using namespace std;

int t, n, l, h;
int a[105];

int main(){
    //freopen("C.in", "r", stdin);
    //freopen("C.out", "w", stdout);
    scanf("%d", &t);
    for (int tc=1; tc<=t; tc++){

        scanf("%d %d %d", &n, &l, &h);
        for (int i=0; i<n; i++)
            scanf("%d", &a[i]);

        bool done=false;
        printf("Case #%d: ", tc);

        for (int i=l; i<=h; i++){
            bool fail=false;
            for (int j=0; j<n; j++)
                if (i%a[j] and a[j]%i){
                    fail=true;
                    break;
                }
            if (!fail){
                printf("%d\n", i);
                done=true;
                break;
            }
        }

        if (!done)
            printf("NO\n");
    }
	return 0;
}
