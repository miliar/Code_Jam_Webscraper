#include <iostream>
#include <cstdio>
#include <cstring>
#include <queue>
#include <set>
#include <algorithm>
#include <cmath>

using namespace std;

int t, n, sol;
int o, b, peno, penb;

int main(){
    freopen("A.txt", "w", stdout);
    scanf("%d", &t);
    for (int tc=1; tc<=t; tc++){
        scanf("%d", &n);
        o=b=1;
        sol=peno=penb=0;

        char t1; int t2;
        while(n--){
            scanf(" %c %d", &t1, &t2);
            if (t1=='O'){
                int temp=max(0, abs(o-t2)-peno)+1;
                sol+=temp;
                penb+=temp;
                peno=0;
                o=t2;
            }
            else {
                int temp=max(0, abs(b-t2)-penb)+1;
                sol+=temp;
                peno+=temp;
                penb=0;
                b=t2;
            }
        }

        printf("Case #%d: %d\n", tc, sol);
    }
	return 0;
}
