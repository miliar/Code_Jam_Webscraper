#include <iostream>
#include <string>

using namespace std;

char a[27] = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' '};
char b[27] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q',' '};

char mymap(char in){
	int j;
	for(j = 0; j<26; j++){
		if(a[j] == in)  break;
	}
	return b[j];
}

int main(){

	int k;
	string st,output;
	cin >> k;
	getline(cin,st);
	for (int i = 0; i < k; i++){
		getline(cin,st);
		for(int j = 0; j < st.length(); j++){
			output = output + mymap(st[j]);
		}
		cout << "Case #" << i+1 << ": "<< output << endl;
		output = "";
	}		
}
	 
