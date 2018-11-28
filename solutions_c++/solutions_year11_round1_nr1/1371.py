#include <algorithm>
#include <vector>
#include <string>
#include <deque>
#include <queue>
#include <map>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
using namespace std;
typedef vector<int> vi;
typedef vector<vector<int> > vii;
typedef vector<double> vd;
typedef queue<int> qi;

#define fori(i, n) for(i=0;i<n;i++)
#define fordi(i, n) for(int i=0;i<n;i++)
#define INF 0x7fffffff

char sc() {char r; if (scanf("%c", &r) != 1) {printf("-1"); exit(0);} return r;}
int si() {int r; if (scanf("%d", &r) != 1) {printf("-1"); exit(0);} return r;}
double sf() {double r; if (scanf("%lf", &r) != 1) {printf("-1"); exit(0);} return r;}

bool check(int N, int pd, int pg) {
    if (pg == 100 && pd != 100)
        return false;
    if (pg == 0 && pd != 0)
        return false;

    int div=100;
    if (!(pd % 4)) div/=4;
    else if (!(pd %2)) div /=2;

    if(!(pd %25)) div/=25;
    else if (!(pd %5)) div/=5;
    if (div > N) return false;
    return true;

}


main() {
    int T=si();

    fordi(i,T) {
        int N=si(), pd=si(),pg=si();
        if (check(N,pd,pg))
            printf("Case #%d: Possible\n", i+1);
        else
            printf("Case #%d: Broken\n", i+1);
            
    
    }


}
