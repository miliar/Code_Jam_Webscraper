#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
using namespace std;
ofstream bug;
const bool DEBUG = true; 
const int MAXN = 2000+1;
const char PROBLEM[] = {"2l"}; 
char *PROB;

int tests, test; 
int i, j, k, r, x, y, m, n, ans; 
int S, P; 
int q[MAXN], g[MAXN];
int t[MAXN]; 
string s; 

template <class T> void debug(T t){ if (DEBUG) bug << "[" << t << "]"; }
template <class T> void debug(T t, T t2){ if (DEBUG) bug << "[" << t << "," << t2 << "]"; }
template <class T> void debug(T t, T t2, T t3){ if (DEBUG) bug << "[" << t << "," << t2 << "," << t3 << "]"; }
bool sort_desc(int a, int b) { return  a > b; }

int main(){
if (DEBUG) {
    PROB = new char[10];
    strcpy(PROB, PROBLEM); freopen(strcat(PROB, ".in"), "r", stdin); 
    strcpy(PROB, PROBLEM); freopen(strcat(PROB, ".out"), "w", stdout);
    strcpy(PROB, PROBLEM); bug.open(strcat(PROB, ".txt")); 
}
    
    scanf("%d", &tests);
    
for (test = 1; test <= tests; ++test){
    if (DEBUG) bug << endl << "Case #" << test << ": " << endl; 
    scanf("%d %d %d", &n, &S, &P);
    ans = 0; 
    for (i = 0; i < n; ++i ) {
        scanf("%d", &t[i]); 
    }
    sort(t, t+n, sort_desc); 
    for (i = 0; i < n; ++i ) {
        debug(t[i]); 
        x = t[i] / 3; 
        y = t[i] % 3; 
        if (y) ++x; 
        if (x >= P){
            ++ans;    
        } else {
            if (!S) break;   
            if (!t[i]) break;   
            debug(y, x+1, P);
            if ((y == 2 && x+1 >= P) || (y==0 && x+1 >= P)){
                --S; 
                ++ans; 
            }    
            if (!S) break;     
        }
    }
    printf("Case #%d: %d\n", test, ans); 
    
}   
     
    return 0;  
}
