#include<iostream>

using namespace std;

int main(){
	string str = "yhesocvxduiglbkrztnwjpfmaq";
	int n;
	scanf("%d\n", &n);
	for(int q = 0; q < n; q++){
		string line;
		getline(cin, line);
		string result;
		for(int i = 0; i < line.size(); i++){
			if(line[i] > 'z' || line[i] < 'a') result += line[i];
			else result += str[line[i] - 'a'];
		}
		printf("Case #%d: %s\n", q+1, result.c_str());
	}
}
