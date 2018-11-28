#include <iostream>
#include <string.h>
#include <stdio.h>
using namespace std;

int main() {
	int caseno;
	char input[102],map[27]={' ','y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	cin>>caseno;
	cin.getline(input,100);
	for(int j=0;j<caseno;j++) {
		bzero(input,( sizeof(char))*102);
		cin.getline(input,101);
		for( int i=0; i<strlen(input); i++) {
			if(i==0)
				cout<<"Case #"<<j+1<<": ";
			if(*(input+i)==' ')
				cout<<map[0];
			else
				cout<<map[*(input+i)-96];
		}
		cout<<"\n";
	}
}
