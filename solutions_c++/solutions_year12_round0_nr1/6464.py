#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <cstdio>
#include <sstream>

using namespace std;

int main(){
	char map[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	string line;
	int n;

	getline(cin,line);
	sscanf(line.c_str(),"%d",&n);
	for(int i=0;i<n;i++){
		getline(cin,line);
		for(int j=0; j < line.length(); j++) if(line[j]!=' ') line[j] = map[ line[j]-'a' ];
		cout<<"Case #"<<i+1<<": "<<line<<endl;
	}
	return 0;
}

