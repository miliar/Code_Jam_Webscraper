#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <map>
#include <cstring>

using namespace std;

int main(int argc, char** argv){
	vector<string> in(3);
	vector<string> out(3);
	FILE *fp = fopen("A-small-attempt1.in", "rb");	
	map<char, char> map_values;
	map<char, char>::iterator it;
	char line[110];
	int inc = 0;
	

	in[0] = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
	out[0] = "our language is impossible to understand";
	in[1] = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
	out[1] = "there are twenty six factorial possibilities";
	in[2] = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
	out[2] = "so it is okay if you want to just give up";

	for(int i = 0; i < 3; ++i){
		for(int j = 0; j < in[i].length(); ++j){
			map_values.insert(pair<char,char>(in[i][j], out[i][j]));
		}
	}
	map_values.insert(pair<char, char>('q', 'z'));
	map_values.insert(pair<char, char>('z', 'q'));

	if(fp != NULL){
		while(fgets(line, 1000, fp) != NULL){
			string out(line);
			for(int i = 0; i < strlen(line)-1; ++i){
				out[i] = map_values[line[i]];	
			}
			if (inc == 0){
				inc++;
				continue;
			}
			cout << "Case #" << inc++ << ": " << out;;
		}
	}


}
