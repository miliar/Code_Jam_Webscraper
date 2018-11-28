#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
using namespace std;
ofstream bug;
const bool DEBUG = true; 
const int MAXN = 10000+10;
const char PROBLEM[] = {"1l"}; 
char *PROB;

int tests, test; 
int i, j, k, r, x, y, m, n, ans, maxdist; 
int C, I, D, T; 
int f[MAXN], d[MAXN], l[MAXN]; 
string s; 

template <class T> void debug(T t){ if (DEBUG) bug << "[" << t << "]"; }
template <class T> void debug(T t, T t2){ if (DEBUG) bug << "[" << t << "," << t2 << "]"; }
template <class T> void debug(T t, T t2, T t3){ if (DEBUG) bug << "[" << t << "," << t2 << "," << t3 << "]"; }


bool solve(){
    if (d[1] > l[1]) return false; 
    memset(f, 0, sizeof(f)); 
    f[1] = 2 * d[1]; 
    if (f[1] >= D) return true; 
    for (int i = 2; i <= n; ++i ){
        f[i] = d[i];
        for (int j = 1; j < i; ++j ){
            if (f[j] >= d[i]){
                f[i] = max(f[i], d[i] + min(l[i], d[i] - d[j]));
                if (f[i] >= D) return true; 
            }    
        }    
    }
    return false;
}

bool solve2(int x,int can,int op){
	if (can >= D) return true;
	if (can < f[x]) return false;
	f[x] = can;
	int ed = op;
	for (int i = op + 1; i < n; ++i)
		if (d[i] <= can) ed = i;
	for (int i = op + 1; i <= ed; ++i)
		if (d[i] <= can){
			int t = min(d[i]-d[x],l[i]) + d[i];
			if (solve2(i,t,ed)) return true;
		}
	return false;
}

int main(){
if (DEBUG) {
    PROB = new char[10];
    strcpy(PROB, PROBLEM); freopen(strcat(PROB, ".in"), "r", stdin); 
    strcpy(PROB, PROBLEM); freopen(strcat(PROB, ".out"), "w", stdout);
    strcpy(PROB, PROBLEM); bug.open(strcat(PROB, ".txt")); 
}
    
    scanf("%d", &tests);
    
for (test = 1; test <= tests; ++test){
    int A, B; 
    if (DEBUG) bug << endl << "Case #" << test << ": " << endl; 
    scanf("%d", &n); 
    
    for (int i = 0; i < n; ++i ){
        scanf("%d%d", &d[i], &l[i]);
    }
    scanf("%d", &D); 
     memset(f, 0, sizeof(f)); 
    if (solve2(0, d[0]*2, 0)) printf("Case #%d: YES\n", test); else printf("Case #%d: NO\n", test);
}   
     
    return 0;  
}
