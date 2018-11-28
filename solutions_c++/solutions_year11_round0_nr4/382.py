#include <iostream>
#include <string>
#include <cmath>
using namespace std;

const int MAXN = 1000+10; 
int a[MAXN], c[MAXN]; 
int tests, test, n; 
double ans; 

int main(){
    //freopen("4.in","r",stdin); 
    //freopen("4.out","w",stdout);

    scanf("%d",&tests);
     
    for (test = 1; test <= tests; ++test){
        scanf("%d", &n); 
		for (int i = 0; i < n; ++i ) {
            scanf("%d", &c[i]); 
		    a[i] = c[i];    
        }
		ans = 0; 
		sort(a, a+n); 
		
        for (int i = 0; i < n; ++i ) 
            if (a[i] != c[i]) ++ans;  

		
		printf("Case #%d: %.6f\n", test, ans );  
    }   
     
    return 0;  
}
