#include <iostream>
#include <cstdio>
using namespace std;

#define REP(x, n) for(int (x)=0; (x)<(n); (x)++)

void testcase(int no){
    int n, k; scanf("%d%d", &n, &k);
    int p = (1 << n) - 1;
   // cout << "checking power: " << p << endl;
    printf("Case #%d: %s\n", no, ((k & p) == p) ? "ON" : "OFF" );
}

int main(){
    int z; scanf("%d", &z);
    REP(x, z) testcase(x+1);
}
