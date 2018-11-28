#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <map>
#include <cstring>

using namespace std;

int main(int argc, char** argv){
	vector<string> input(3);
	vector<string> output(3);
	map<char, char> mapping;
	

	input[0] = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
	input[1] = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
	input[2] = "de kr kd eoya kw aej tysr re ujdr lkgc jv";

	output[0] = "our language is impossible to understand";
	output[1] = "there are twenty six factorial possibilities";
	output[2] = "so it is okay if you want to just give up";

	for(int i = 97; i < 123; ++i){
		//mapping.insert(pair<char,char>((char)i,'0'));
	}
	mapping.insert(pair<char, char>('q', 'z'));
	mapping.insert(pair<char, char>('z', 'q'));

	{
		for(int i = 0; i < 3; ++i){
			for(int j = 0; j < input[i].length(); ++j){
				mapping.insert(pair<char,char>(input[i][j], output[i][j]));
			}
		}
	}

	map<char, char>::iterator it;
	for(it = mapping.begin(); it != mapping.end(); ++it){
	//	cout <<	(*it).first << " " << (*it).second << endl;
	}


	FILE *fp = fopen("/tmp/A-small-attempt4.in", "rb");	
	char line[1000];
	
	int x = 0;
	if(fp != NULL){
		while(fgets(line, 1000, fp) != NULL){
			string out(line);
			for(int i = 0; i < strlen(line)-1; ++i){
				out[i] = mapping[line[i]];	
			}
			if(x == 0){
				x++;
				continue;
			}
			cout << "Case #" << x << ": " << out;;
			x++;
		}
	}


}
