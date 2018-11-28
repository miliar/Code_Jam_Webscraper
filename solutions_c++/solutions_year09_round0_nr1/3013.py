#include<iostream>
#include<string>
#include<vector>
using namespace std;

int main(){
	vector <string> dict;
	int l,d,n, count=0;
	bool foundall;
	string str;
	cin >> l >> d >> n;
	for(int i=0;i<d;i++){
		cin >> str;
		dict.push_back(str);
	}
	for(int i=0;i < n;i++){
		cin >> str;
		count=0;
		for(int j=0;j<d;j++){
			int p =0;
			foundall = true;
			for(int k=0;k<l;k++){
				bool found = false;
				if(str[p]=='('){
					p++;
					while(str[p] != ')' ){
						if(str[p] == dict[j][k])
							found = true;
						p++;
					}
					p++;
					if(found == false)
						foundall=false;
				}
				else{
					if(str[p++] != dict[j][k])
						foundall= false;
				}
			}
			if(foundall== true)
				count++;
		}
		cout << "Case #"<< i+1 << ": " << count <<endl;
	}
	return 0;
}
