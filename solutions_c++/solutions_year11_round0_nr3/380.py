#include <iostream>
#include <string>
#include <cmath>
using namespace std;

const int MAXN = 1000 + 10;  
int tests, test, total, n, sum, ans; 
int c[MAXN]; 

int main(){
    //freopen("3.in","r",stdin); 
    //freopen("3.out","w",stdout);

    scanf("%d",&tests);
     
    for (test = 1; test <= tests; ++test){
        scanf("%d", &n); 
        ans = 1<<31-1;
        sum = 0; 
        total = 0; 
		for (int i = 0; i < n; ++i ) {
			scanf("%d", &c[i]); 
			total = total ^ c[i];
			sum += c[i]; 
			if (c[i] < ans) ans = c[i]; 
		}
		if (total){
			printf("Case #%d: NO\n", test); 
			continue; 
		}
		
		printf("Case #%d: %d\n", test, sum - ans);  
    }   
     
    return 0;  
}
