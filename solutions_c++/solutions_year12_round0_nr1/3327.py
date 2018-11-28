#include <iostream>
using namespace std;

char decode[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q',};

int main(){
	int n;
	cin >> n;
	string line;
	getline(cin,line);
	for (int test=0;test<n;test++){
		getline(cin,line);
		cout << "Case #" << test+1 << ": ";
		for (int i=0;i<line.length();i++)
			cout << (line[i]==' ' ? ' ' : decode[line[i]-'a']);
		cout << endl;
	}
}