#include <iostream>
#include <string>
using namespace std;

int main(){
	int L, D, N;
	cin >> L >> D >> N;
	string data[D];
	for(int i = 0; i < D; i++){
		cin >> data[i];
	}
	
	for(int n = 1; n <= N; n++){
		string str, data2[L];
		for(int i = 0; i < L; i++) data2[i] = "";
		cin >> str;
		int len = str.length(), s=0, index=0;
		for(int i = 0; i < len; i++){
			if(str[i] == '('){
				s = 1;
			}
			else if(str[i] == ')'){
				s = 0;
				index++;
			}
			else{
				data2[index] += str[i];
				if(s == 0) index++;
			}
		}
		int count = 0, NG=0;
		for(int i = 0; i < D; i++){
			NG=0;
			for(int j = 0; j < L; j++){
				if(data2[j].find(data[i][j]) == string::npos){
					NG=1;
					break;
				}
			}
			if(!NG) count++;
		}
		cout << "Case #" << n << ": " << count << endl;
	}
}
