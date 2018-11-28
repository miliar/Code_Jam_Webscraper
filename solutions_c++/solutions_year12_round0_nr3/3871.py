#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <queue>
#include <string>
#include <cmath>
#include <set>
#define pb push_back
#define fs first
#define sc second

using namespace std;

int memoo[2000005];

set<int> precalcValues[2000005];


inline int rev2(int num, int pos){
    int p1, p2, pot = 1;
    for (int i=0;i<pos;++i) pot*=10;

    p1 = num / pot;
    p2 = num % pot;
    char buffer[15];
    sprintf (buffer, "%d%d", p2, p1);
    if ( buffer[0] == '0') return -1;
    int n;
    sscanf (buffer, "%d", &n);
    return n;
}

inline int rev(int num, int pos){
    int p1, p2, pot = 1;
    for (int i=0;i<pos;++i) pot*=10;

    p1 = num / pot;
    p2 = num % pot;
    if ( p1 == num || p2 == num ) return -1;
    int pot2 = 1;
    while (pot2 <= p1){
        pot2*=10;
        p2*=10;
    }
    return p2 + p1;
}


void precalc(){

    for (int i=1;i<=2000000;++i){
        int pot = 1;
        int num = i;

        set<int> found_nums;
        for (int j=1;;++j){
            if ( pot > num ) break;
            int r = rev(num, j);
            if ( r > num  ) {
                found_nums.insert(r);
            }
            pot *= 10;
        }
        precalcValues[i] = found_nums;
    }

}

int calcNum(int a, int b){
    int cnt = 0;
    for (int i=a;i<=b;++i){
        for(set<int> :: iterator it = precalcValues[i].begin();it != precalcValues[i].end();++it){
            if ( *it <= b ) ++cnt;
        }
    }
    return cnt;
}

int main(void){


    #ifndef KEYBOARD_INPUT
    freopen("c-small-in.txt", "r", stdin);
    freopen("c-small-out.txt", "w", stdout);
    #endif

    precalc();

    int _test, a, b;
    scanf("%d", &_test);
    for (int test=1;test<=_test;++test){
        scanf ("%d %d", &a, &b);
        printf ("Case #%d: %d\n", test,calcNum(a,b));
    }

	return 0;
}
