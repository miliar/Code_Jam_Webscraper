#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>
#include <utility>
#include<map>

using namespace std;

int main(int argc, char **argv) {
	ifstream input (argv[argc-1]);
	char tmap[26];
	char tmp[2024];
	string num;
	string mapinput[3];
	string mapoutput[3];
	int input_size;

	if(argc!=2){
		cout << "There is no input file!" << endl;
		return -1;
	}

	mapinput[0]="ejp mysljylc kd kxveddknmc re jsicpdrysi";
	mapinput[1]="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
	mapinput[2]="de kr kd eoya kw aej tysr re ujdr lkgc jv";
	mapoutput[0]="our language is impossible to understand";
	mapoutput[1]="there are twenty six factorial possibilities";
	mapoutput[2]="so it is okay if you want to just give up";

	// make map
	tmap['a'-'a']='y';
	tmap['y'-'a']='a';
	tmap['o'-'a']='e';
	tmap['e'-'a']='o';
	tmap['q'-'a']='z';
	tmap['z'-'a']='q';
	for(int i=0; i<3; i++){
		for(int j=0; j<mapinput[i].size(); j++){
			if(mapinput[i][j]!=' ')	tmap[mapinput[i][j]-'a']=mapoutput[i][j];
		}
	}


	// cout << "maked tmap" << endl;

	input.getline(tmp, 2024);
	input_size=atoi(tmp);

	for(int i=1; i<=input_size; i++){
		cout << "Case #" << i << ": ";
		input.getline(tmp, 2024);
		for(int j=0; j<2024; j++){
			if(tmp[j]!=' ' && tmp[j]!='\0'){
				cout << tmap[tmp[j]-'a'];
			}else if(tmp[j]=='\0'){
				break;
			}else{
				cout << " ";
			}
		}
		cout << endl;
	}

	return 0;
}