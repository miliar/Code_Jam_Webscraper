#include <map>
#include <iostream>
#include <stdio.h>
#include <string> 
using namespace std; 

const string RULE_IN = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jvzq"; 
const string RULE_OUT= "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give upqz"; 

int main(){
	freopen("A-small-attempt1.in","r",stdin); 
	freopen("A-small-attempt1.out","w",stdout); 
	int T; 
	string str, ans; 
	cin >> T; 
	getline(cin, str); 
	for(int testid = 1; testid <= T; ++testid){
		getline(cin,str);  
		ans = ""; 
		for(int i = 0; i < str.length(); ++ i){
			int vt = RULE_IN.find(str[i]); 
			if (vt > -1) ans += RULE_OUT[vt];
			else cout << "############" << str[i] << endl << endl; 
		}
		cout << "Case #" << testid << ": " << ans << endl; 
	}
	return 0; 
}