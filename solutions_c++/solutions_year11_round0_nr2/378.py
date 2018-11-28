#include <iostream>
#include <string>
#include <cmath>
using namespace std;

string s; 
const int MAXN = 26 + 10; 
const int MAXQ = 100+30; 

int f(char c){ return int(c-'A')+1; }

char c[MAXN][MAXN]; 
bool o[MAXN][MAXN]; 
char q[MAXQ]; 
char ca, cb, cc; 
bool deduction; 
int cn, on, test, tests, n, r; 

int main(){
    //freopen("2.in","r",stdin); 
    //freopen("2.out","w",stdout);

    scanf("%d",&tests);
     
    for (test = 1; test <= tests; ++test){
        scanf("%d", &cn); 
		for (int i = 0; i < MAXN; ++i )
		for (int j = 0; j < MAXN; ++j ){
			c[i][j] = '@'; 
			o[i][j] = false; 
		}
		
        for (int i = 0; i < cn; ++i ){
			scanf(" %c%c%c", &ca, &cb, &cc ); 
			c[f(ca)][f(cb)]  = cc; 
			c[f(cb)][f(ca)]  = cc; 
		}
			
		scanf("%d", &on); 
		for (int i = 0; i < on; ++i ){
			scanf(" %c%c", &ca, &cb); 
			o[f(ca)][f(cb)] = true; 
			o[f(cb)][f(ca)] = true; 
		}
		
		scanf("%d", &n); 
		deduction = false; 
		r = 0; 
		scanf("%c", &ca); //blank
		for (int i = 0; i < n; ++i ) {
			if (!deduction){
				scanf("%c", &ca);
				q[++r] = ca; 
			}
			while (r > 1){
			if (c[f(q[r])][f(q[r-1])] != '@'){
				q[r-1] = c[f(q[r])][f(q[r-1])]; 
				--r; 
				continue; 
			} else{
                for (int j = 1; j <= r - 1; ++j )
			    if (o[f(q[j])][f(q[r])]){
				    r = 0; 
                    break;  
                }
			}
            break;  
            }
		}		
        if (r == 0) {
            printf("Case #%d: []\n", test); 
        } else {
		  printf("Case #%d: [%c", test, q[1]);
		  for (int i = 2; i <= r; ++i ) printf(", %c",q[i]); 
		  printf("]\n");
        } 
    }   
     
    return 0;  
}
