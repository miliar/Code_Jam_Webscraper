#include <iostream>
#include <string.h>
#include <stdio.h>
#include <map>

using namespace std;

int main(int argc, char *argv[]) {
	
	map<char , char > mp;
	char line[130];
	int casos;
	
	mp.insert(pair<char, char> ('a','y'));
	mp.insert(pair<char, char> ('b','h'));
	mp.insert(pair<char, char> ('c','e'));
	mp.insert(pair<char, char> ('d','s'));
	mp.insert(pair<char, char> ('e','o'));
	mp.insert(pair<char, char> ('f','c'));
	mp.insert(pair<char, char> ('g','v'));
	mp.insert(pair<char, char> ('h','x'));
	mp.insert(pair<char, char> ('i','d'));
	mp.insert(pair<char, char> ('j','u'));
	mp.insert(pair<char, char> ('k','i'));
	mp.insert(pair<char, char> ('l','g'));
	mp.insert(pair<char, char> ('m','l'));
	mp.insert(pair<char, char> ('n','b'));
	mp.insert(pair<char, char> ('o','k'));
	mp.insert(pair<char, char> ('p','r'));
	mp.insert(pair<char, char> ('q','z'));
	mp.insert(pair<char, char> ('r','t'));
	mp.insert(pair<char, char> ('s','n'));
	mp.insert(pair<char, char> ('t','w'));
	mp.insert(pair<char, char> ('u','j'));
	mp.insert(pair<char, char> ('v','p'));
	mp.insert(pair<char, char> ('w','f'));
	mp.insert(pair<char, char> ('x','m'));
	mp.insert(pair<char, char> ('y','a'));
	mp.insert(pair<char, char> ('z','q'));
	int n=1;
	cin>>casos;
	cin.ignore();
	while(casos--){
		gets(line);
		cout<<"Case #"<<n++<<": ";
		for(register unsigned int i=0;i<strlen(line);i++){
			if(line[i]==' ')
				cout<<" ";
			else
				cout<<mp.find(line[i])->second;
		}
		cout<<endl;
		
	}
	
	
	return 0;
}

