#include <iostream>
#include <string>

using std::string;

int T;
char G[101];
string test = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv qz";
string outs = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up zq";
char mapping[26];

void display() {
	for (int i = 0 ; i < 26 ; i++) {
		std::cout << (char)('a' + i) << " --> " << (char)('a' + mapping[i]) << std::endl;
 	}
}

void init() {
	for (int i = 0 ; i < 26 ; i ++) {
		mapping[i] = ' ';
	}
}

int main() {

	init();
	//display();
	for (int i = 0 ; i < test.length() ; i++) {
		if (outs[i] != ' ') { 
			//mapping[outs[i]-'a'] = test[i] - 'a';
			mapping[test[i]-'a'] = outs[i] - 'a';
		}
	}
	//std::cout << "final mapping" << std::endl;;
	//display();
	/*
	for (int i = 0 ; i <26 ; i++) {
		char start = i;
		char temp = mapping[start];
		std::cout << (char)(i+'a') << " "; 
		if (temp == ' ') {
			std::cout << std::endl;
			continue;
		}
		do {
			std::cout << (char)(temp + 'a') << " ";
			temp = mapping[temp];
			if (temp == ' ') {
				std::cout << (char)(temp + 'a') << " ";
				break;
			}
		}while (start != temp);
		std::cout << std::endl;
	}
	*/
	std::cin >> T;
	std::cin.getline(G,101);
	for (int i = 0 ; i < T ; i++) {
		std::cin.getline(G,101);
		//std::cout << G <<std::endl;
		G[100] = '\0'; 
		int length = strlen(G);
		for (int i = 0 ; i < length ; i++) {
			if (G[i] >= 'a' && G[i] <= 'z') {
				G[i] = mapping[G[i] - 'a'] + 'a';
			}
		}
		std::cout << "Case #" << i+1 << ": " << G;
		std::cout << std::endl;
	}
	
	return 0;
}
