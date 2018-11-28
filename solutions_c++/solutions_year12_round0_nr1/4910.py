#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(void){
	char alfa[] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	int t;
	ofstream fw;
	fw.open("out.txt");
	cin >> t;
	string riadok;
	getline(cin,riadok);
	for(int i=0;i<t;i++){
		getline(cin, riadok);
		fw << "Case #" << i+1 << ": ";
		for(int j=0;j<riadok.size();j++){
			if(riadok[j] == ' '){
				fw << ' ';
			}else{
				fw << alfa[riadok[j] - 'a'];
			}
		}
		fw << endl;
	}

	return 0;
}
