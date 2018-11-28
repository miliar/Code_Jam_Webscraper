#include<cstdio>
#include<string>
#include<iostream>

using namespace std;

int main(void){
	
	int n;
	string str;
	string c = "yhesocvxduiglbkrztnwjpfmaq";
	scanf("%d", &n);
	for(int i = 1; i <= n; i++){
		getline(cin,str);
		for(int j = 0; j < str.size(); j++){
			if(str[j] != ' ' )str[j] = c[str[j]-'a'];
		}
		cout << "Case #" << i << ": "<< str << endl;;
	}
	
	return 0;
}