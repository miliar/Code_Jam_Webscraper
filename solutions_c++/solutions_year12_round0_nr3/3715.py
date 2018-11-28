#include <stdio.h>
#include <memory.h>
#include <iostream>
#include <string>
#include <set>


using namespace std;

int a, b;
int m10[10];
set<int> rot;


void init() {
    m10[0] = 1;
    for (int i=1; i<10; i++) m10[i] = m10[i-1]*10;
}

int count(int a, int b, int x) {
    //
    int tmp = x, n = -1;    
    while (tmp>0) { n++; tmp /= 10; }
    tmp = x;
    

    //
    rot.clear();
    for (int i=0; i<n; i++) {
        x = (x%10)*m10[n] + (x/10);
        if (tmp<x && x<=b && rot.count(x)==0) rot.insert(x);
    }

    return rot.size();
}

int cal(int a, int b) {
    int res = 0;

    for (int i=a; i<=b; i++) {
        res += count(a, b, i);
    }

    return res;
}

int main() {
    int num_test;
    
    init();

    cin >> num_test;
    for (int i=1; i<=num_test; i++) {
        cin >> a >> b;
        printf("Case #%d: %d\n", i, cal(a,b));
    }

    return 0;
}
