#include <iostream>

using namespace std;

int main(){
	int t;
	cin >> t;
	char g[] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	cin.ignore();
	for(int i = 1; i <= t; i++){
		char c[200];
		cin.getline(c,200);
		cout << "Case #" << i << ": ";
		int idx = 0;
		while(c[idx]){
		       if(c[idx] != ' '){
			       cout << g[c[idx]-'a'];
		       }else cout << ' ';
		       idx++;
		}
		cout << endl;
	}
}
