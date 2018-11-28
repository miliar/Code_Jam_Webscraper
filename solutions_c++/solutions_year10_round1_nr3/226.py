#include<cstdio>
#include<iostream>
#include<sstream>
#include<cmath>
#include<algorithm>
#include<map>
#include<set>
#include<list>
#include<vector>
#include<stack>
#include<queue>
#include<string>
#include<ctime>
using namespace std;
const int INF = 2147483647;
const double PI = 3.141592653589793;

long long res;
int q,a1,a2,b1,b2,c,z,a,b;

int main() {
scanf ("%d",&z);
for (q=1;q<=z;q++) {
    scanf ("%d %d %d %d",&a1,&a2,&b1,&b2);
    res=0;
    for (a=a1;a<=a2;a++) {
        c = int(ceil(a*((1+sqrt(5))/2)));
        c = max (c,b1);
        if (c<=b2) res+=(b2-c+1);
    }
    for (b=b1;b<=b2;b++) {
        c = int(ceil(b*((1+sqrt(5))/2)));
        c = max (c,a1);
        if (c<=a2) res+=(a2-c+1);
    }
    cout << "Case #" << q << ": " << res << endl;
    //printf("Case #%d: %d\n",q,res);
}
return 0;
}
