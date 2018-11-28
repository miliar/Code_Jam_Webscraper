#include <iostream>
#include <string>
#include <set>
#include <vector>
using namespace std;

string code_jam = "welcome to code jam", str, str2;
int c, code_jam_len = 19, len;

void func(int code_i, int i){
	string sub = str2.substr(i, len-i);
	//cout << sub << endl;
	int p=0, pos=i;
	while(1){
		p = sub.find(code_jam[code_i]);
		if(p == string::npos) break;
		else{
			pos += p;
			if(code_i==18){
				c = (c+1)%10000;
			}
			else
				func(code_i+1, pos+1);
			sub = sub.substr(p+1, sub.length()-p-1);
			pos++;
		}
	}
}

int main(){
	int n;
	string str;
	cin >> n;
	getline(cin, str);
	for(int nn = 1; nn <= n; nn++){
		c=0;
		str2="";
		getline(cin, str);
		len = str.length();
		for(int i = 0; i < len; i++){
			if(code_jam.find(str[i]) != string::npos){
				str2 += str[i];
			}
		}
		len = str2.length();
		func(0,0);
		cout << "Case #" << nn << ": ";
		if(c / 1000 == 0) cout << 0;
		if(c / 100 == 0) cout << 0;
		if(c / 10 == 0) cout << 0;
		cout << c << endl;
	}
}
