#include <iostream>
#include <cstdio>
using namespace std;

/*
Google CodeJam 2012 - Problem A
Guillermo Croppi (Argentina)

Normal -> A B C D E F G H I J K L M N O P Q R S T Y U W X Y Z
Google -> Y N F I C W L B K U O M X S E V ? P D R J G T H A ?

rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
there are twenty six factorial possibilities

*/
int main(int argc, char *argv[]) {
	char map[26][2] = {	{'a','y'},
						{'b','h'},
						{'c','e'},
						{'d','s'},
						{'e','o'},
						{'f','c'},
						{'g','v'},
						{'h','x'},
						{'i','d'},
						{'j','u'},
						{'k','i'},
						{'l','g'},
						{'m','l'},
						{'n','b'},
						{'o','k'},
						{'p','r'},
						{'q','z'},
						{'r','t'},
						{'s','n'},
						{'t','w'},
						{'u','j'},
						{'v','p'},
						{'w','f'},
						{'x','m'},
						{'y','a'},
						{'z','q'} };
	int cases;
	int caseNumber = 1;
	char s[110];
	string str;
	
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A.out","w",stdout);
	
	scanf("%d\n",&cases);
	while(cases--){
		gets(s);
		str.assign(s);
		
		for(int i=0; i<str.length(); i++){
			if(str[i]!=' ')
				str[i] = map[str[i]-97][1];
		}
		
		cout << "Case #" << caseNumber++ << ": " << str << endl;
	}
	
	
	
	return 0;
}

