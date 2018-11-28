#include <iostream>
#include <fstream>
#include <stdio.h>
using namespace std;

char table[27] = {
	'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'
};

int main() {
	FILE* fp = fopen("A-small-attempt1.in", "r");
	ofstream fout("outputA.txt");
	int T;
	fscanf(fp, "%d", &T);

	char c;
	fscanf(fp, "%c", &c);
	for( int t=0; t<T; t++){
		fout<<"Case #"<<t+1<<": ";
		for(int i=0; i<100; i++){
			fscanf(fp, "%c", &c);
			if(c == '\n')
				break;
			if(c==' '){
				fout<<' ';
				continue;
			}
			int index = c - 'a';
			fout<<table[index];
		}
		fout<<endl;
	}
	fclose(fp);
	fout.close();
	return 0;
}

