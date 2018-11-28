#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <cmath>
#include <cctype>
#include <stack>
#include <queue>
#include <sstream>

using namespace std;

#define REP(i, T) for(int (i)=0; (i) < T; (i) ++)
#define FOR(i, L, R) for(int (i)=L; (i) < R; (i) ++)
#define PB push_back
#define ERS(v, i) (v).erase((v).begin()+(i))
#define ALL(v) v.begin(), v.end()
#define SORT(v) sort(ALL(v))
#define SZ(v) (int)v.size()

#define vi vector<int>
#define vs vector<string>
#define ll long long
#define pi pair<int, int>
#define MP make_pair
#define X first
#define Y second

int C, D;
int loc[220];
int newloc[220];
int V[220];

int radio(int i) {
    int v = V[i];
    if(v % 2) return ((v-1)/2)*D;
    else return ((v/2)-1)*D + D/2;
}

int minim(int a, int b) {
    return (a<b)?a:b;
}

int myabs(int a) {
    return (a<0)?-a:a;
}

int main()
{
    int T, i, j, k;
    cin >> T;
    for(int caso=1; caso<=T; caso++) {
        cin >> C >> D;
        D *= 2;
        for(i=0; i<C; i++) cin >> loc[i] >> V[i], loc[i]*=2;
        
        int a, b;
        a = 0;
        b = 1000000000;
        int x = 0;
        while(a < b) {
            //~printf("--- %d %d       ", a, b);
            x = (a+b)/2;
            //~printf("%d\n", x);
            bool ok=true;
            if(radio(0) > x) ok = false;
            else {
                newloc[0] = loc[0] - (x-radio(0));
                //~if(x == 4) printf("%d %d %d   %d\n", 0, loc[0], newloc[0], radio(0));
                for(i=1; ok && i<C; i++) {
                    if(radio(i) > x) {
                        ok = false;
                        break;
                    }
                    
                    int dif = (loc[i]-radio(i)) - (newloc[i-1]+radio(i-1));
                    //~if(x == 4) printf("diff %d\n", dif);
                    //~if(x == 4) printf("D %d\n", D);
                    if(dif >= D) {
                        newloc[i] = loc[i] - minim(dif-D, x-radio(i));
                    } else {
                        if(D-dif <= x-radio(i)) {
                            //~printf("Aloha\n");
                            newloc[i] = loc[i] + (D-dif);
                        } else ok = false;
                    }
                    //~if(x == 4) printf("%d %d %d     %d\n", i, loc[i], newloc[i], radio(i));
                }
            }
            
            if(ok) {
                b = x;
            } else {
                a = x+1;
            }
        }
        
        x = a;
        
        //~bool ok = true;
        //~if(radio(0) > x) ok = false;
        //~else {
            //~newloc[0] = loc[0] - (x-radio(0));
            //~
            //~for(i=1; ok && i<C; i++) {
                //~if(radio(i) > x) {
                    //~ok = false;
                    //~break;
                //~}
                //~
                //~int dif = (loc[i]-radio(i)) - (newloc[i-1]+radio(i-1));
                //~if(dif >= D) {
                    //~newloc[i] = loc[i] - minim(dif-D, x-radio(i));
                //~} else {
                    //~if(D-dif <= x-radio(i)) {
                        //~newloc[i] = loc[i] + (D-dif);
                    //~} else ok = false;
                //~}
            //~}
            //~
            //~if(ok) {
                //~b = x;
            //~} else {
                //~a = x+1;
            //~}
        //~}
        
        printf("Case #%d: %lf\n", caso, (double)x/2.0);
        
    }

        
        
    return 0;
}
