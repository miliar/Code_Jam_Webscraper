#include <iostream>
#include <string>
#include <cstring>

using namespace std;

char str[6000][30];
bool appear[30][26];

int main(){

    int L, D, N;	
    cin >> L >> D >> N;
    for(int i = 0; i < D; i++)
        cin >> str[i];

    for(int i = 0; i < N; i++){ 
        string s;
        cin >> s;
        int token = 0;
	bool inside = false;
        memset(appear, false, sizeof(appear));
	for(int j = 0; j < s.size(); j++){
	    switch(s[j]){
	        case '(':
		    inside = true;    	
                break;
	        case ')':
		    token++;
		    inside = false;
		break;
                default:
	            appear[token][s[j]-'a'] = true;
	            if(!inside)
		        token++;	    
	    }    
	}
        int ans = 0;
	if(token <= L){
	    for(int j = 0; j < D; j++){
		bool math = true;    
	        for(int k = 0; k < L; k++)
		    if(appear[k][str[j][k]-'a'] != true){
                        math = false;
			break;
		    }
		if(math)
		    ans++;	
	    }
	}
	cout << "Case #" << i+1 << ": " << ans << '\n'; 
    }

    return 0;
}
