#include <iostream>
#include <string>
#include <cmath>
using namespace std;

string s; 
const int MAXN = 100 + 10; 
char ch; 
int r, v, ar, br, av, bv, a, b, ans, tests, test, Time, n, data; 
int q[MAXN], aq[MAXN], bq[MAXN], t[MAXN]; 

int min(int a, int b){ return a < b ? a : b; }

int main(){
    //freopen("1.in","r",stdin); 
    //freopen("1.out","w",stdout);

    scanf("%d",&tests);
     
    for (test = 1; test <= tests; ++test){
        scanf("%d", &n); 
        r = 0;
            v = 0;  
        ar = 0; br = 0; 
            av = 0; bv = 0; 
        a = 1; b = 1; 
        ans = 0; 
        
        for (int i = 0; i < n; ++i ) {
            scanf(" %c %d", &ch, &data);
			//cout << ch << data << endl; 
            q[r] = data;
                
            if (ch == 'O') {
                aq[ar++] = data;     
                t[r++] = 0; 
            } else {
                bq[br++] = data;
                t[r++] = 1;  
            }
        }
            
		while (v < r){
			if (!t[v]){
				Time = abs(a - q[v]) + 1; 
				a = q[v];   
				++av; 
			
				if (bv < br){
					if (b < bq[bv]){
						b += min(Time, bq[bv] - b);     
					} else {
						b -= min(Time, b - bq[bv]); 
					}
				}
				
			} else {
				Time = abs(b - q[v]) + 1; 
				b = q[v]; 
				++bv; 
				
				if (av < ar){
					if (a < aq[av]){
						a += min(Time, aq[av] - a); 
					} else {
						a -= min(Time, a - aq[av]); 
					}
				}
			}
			
			//printf("A:%d B:%d Time:%d\n", a, b, Time); 
			ans += Time;
			++v; 
		}

        printf("Case #%d: %d\n", test, ans);            
    }   
     
    return 0;  
}
