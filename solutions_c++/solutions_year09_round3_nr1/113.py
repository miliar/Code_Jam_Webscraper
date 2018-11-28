#include <iostream>
#include <cstring>
using namespace std;

int sym[300];

int main(){

    int cases, counted;
    cin >> cases;
    counted = cases;
    char symbols[1000];
    while(cases--){
	int num = 1;    
        memset(sym, 0, sizeof(sym));
        cin >>symbols;
	int first, second;

	for(int i = 0; i < strlen(symbols); i++){
	    if(sym[symbols[i]-'0'] == 0){
//		    cout << "symbol:" << symbols[i] << '\n';
		if(num== 1)
		    first = symbols[i]-'0';
	        if(num==2)
		    second = symbols[i]-'0';

	        sym[symbols[i]-'0'] = num++;
	    }	    
	}

	sym[first] = 2;
	sym[second] = 1;

	if(num == 2)
	    num++;
	//cout << "sym:" << sym << " " << num << '\n';

        long long int ans = 0;
	long long int c = 1;
        for(int i = strlen(symbols)-1; i >= 0; i--){
		//cout << "ans:" << ans << " s:" << sym[symbols[i]-'0'] << "c:" << symbols[i] << '\n';
	    ans += (sym[symbols[i]-'0']-1)*c;
	    c *= (num-1);
	}

        cout << "Case #" << counted - cases << ": " << ans << '\n'; 
    }

    return 0;
}
