#include <iostream>
#include <string>
using namespace std;

int main(){
	int n;
	cin >> n;

	char v[26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

	string linia;
	getline(cin, linia);
	
	for (int i=0;i<n;++i){
		
		getline(cin, linia);
		for(int k=0; k<linia.size(); ++k){
			
			if (linia[k]>='a' && linia[k]<='z'){
				
				linia[k] = v[linia[k]-'a'];
				
			}
	}

	cout << "Case #" << i+1 << ": " << linia << endl;
	}
}