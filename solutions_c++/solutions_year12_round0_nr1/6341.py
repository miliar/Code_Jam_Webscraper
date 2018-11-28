#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(int argc, char* argv[]){
	char input[] = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
	char output[] = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
	char map[256] = "";

	map['z'] = 'q';
	map['q'] = 'z';
	for(int i = 0; i < strlen(input); i++){
		int index = input[i];
		map[index] = output[i];
		//printf("%c == %c\n",index+30, map[index]);
	}


	std::ifstream file( "input1.in" ) ;
	std::string line ;
	getline( file, line );
	int number = atoi( line.c_str() );
	for( int n = 1; n <= number; n++){
		printf("Case #%d: ",n);
	   getline( file, line );	
	   //cout << line << endl;
	   const char *translate = line.c_str();
	   for(int i = 0; i < strlen(translate); i++){
			int index = translate[i];
			printf("%c",map[index]);
		}
		printf("\n");
	}
	getchar();
	return 0;
}
