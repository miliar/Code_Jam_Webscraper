#include <stdio.h>
#include <iostream>
#include <sstream>
#include <stdlib.h>
#include <string>
#include <vector>
#include <set>
#include <queue>
#include <stack>
#include <list>
#include <math.h>
#include <algorithm>
#include <map>

using namespace std;

typedef pair<int,int>PII;
typedef pair<PII,int>PII2;


int A, B;
double in[100005];
double pro[100005];
class Solve {

    public:
    void main2(){
        scanf("%d %d",&A, &B);
        double minn = B + 2;
        for(int i=1;i<=A;i++){
            scanf("%lf",&in[i]);
        }
        pro[0] = 1.0;
        pro[1] = in[1];
        for(int i=2;i<=A;i++){
            pro[i] = pro[i-1] * in[i];
        }
        for(int i=0;i<=A;i++){
            double sol = 0;
            double temp1 = B - A + 1 + 2 * i;
            double temp2 = B - A + 1 + B + 1 + i * 2;
            sol = temp1 * pro[A-i];
            sol += temp2 * (1 - pro[A-i]);
            minn = min(minn, sol);
        }
        printf("%.06lf\n", minn);
    }
};

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int Test;
    scanf("%d",&Test);
    for(int t=1;t<=Test;t++){
        Solve ___test;
        printf("Case #%d: ", t);
        ___test.main2();
    }
return 0;
}
