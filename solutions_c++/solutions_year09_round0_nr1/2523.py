#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdio>

using namespace std;

char a[5005][20];
char b[2000];
int l, n, d;


int main(){
    cin >> l >> d >> n;
    for (int i = 0; i < d; ++i) cin >> a[i];

    for (int _i = 0; _i < n; ++_i){
    	cin >> b;
    	cout << "Case #" << _i + 1 << ": ";
    	int ans = 0;
    	for (int i = 0; i < d; ++i){
    		int flag = 1;
    		int lb = -1;
            for (int j = 0; j < l; ++j){
            	++lb;
            	if (b[lb] == '('){
                   +a+lb;
                   int p = 0;
                   while(b[lb] != ')'){
                	  if (a[i][j] == b[lb]) p = 1;
                	  ++lb;

                   }
                   if (p == 0){
                	   flag = false;
                	   break;
                   }
                }
              	else{
            		if (b[lb] != a[i][j]){
            		    flag = 0;
            		    break;
            		}
            	}
            }
            if (flag) ++ans;
    	}
    	cout << ans << endl;
    }

	return 0;
}
