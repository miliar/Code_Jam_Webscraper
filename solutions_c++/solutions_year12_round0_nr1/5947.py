#include <iostream>
#include <string.h>
#include <stdio.h>
#include <map>
using namespace std;

int main(int argc, char *argv[]) {
	map<char, char> refer;
	char abcd[27]={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' '};
	char goog[27]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q',' '};
	for(int i = 0; i < 27; i++)
		refer.insert(pair<char, char> (abcd[i], goog[i]));
	int n, caso = 1;
	cin>>n;
	cin.ignore();
	while(n-- > 0) {
		char G[150];
		gets(G);
		cout<<"Case #"<<caso<<": ";
		for(int i = 0; i < strlen(G); i++)
			cout<<refer.find(G[i])->second;
		cout<<endl;
		caso++;
	}
	
	return 0;
}

