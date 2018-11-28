#include <stdio.h>
#include <string.h>
#include <iostream>

using namespace std;

char source[105];
char destin[105];

char code[26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

int main(){
	int n;
	cin>>n;
	getchar();
	for(int i = 0; i<n; i++){
		gets(source);
		cout<<"Case #"<<i+1<<": ";
		for(int j = 0; j<strlen(source); j++){
			cout<<code[source[j] - 'a'];
		}
		cout<<endl;
	}

	

	return 0;
}