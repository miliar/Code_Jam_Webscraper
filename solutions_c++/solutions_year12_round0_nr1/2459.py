#include <iostream>
#include <cstdio>
#include <map>
#include <string>

using namespace std;


map<char,char> dizionario;

void process(string gstr, string estr) {
	string::iterator j=estr.begin();
	for (string::iterator i=gstr.begin(); i!=gstr.end(); ++i) {
		if ( (*i) == ' ' ) {
			j++;
			//printf("ops\n");
			continue;
		}
		//printf("%c va in %c\n",(*i),(*j));
		dizionario[(*i)] = (*(j++));
	}
}

int main() {
	
	dizionario['y'] = 'a';
	dizionario['e'] = 'o';
	dizionario['q'] = 'z';
	dizionario['z'] = 'q';
	
	process( "ejp mysljylc kd kxveddknmc re jsicpdrysi", "our language is impossible to understand" );
	process( "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "there are twenty six factorial possibilities" );
	process( "de kr kd eoya kw aej tysr re ujdr lkgc jv", "so it is okay if you want to just give up" );
	
	/*
	for (map<char,char>::iterator i = dizionario.begin(); i != dizionario.end(); ++i) {
		printf("%c\n",(*i).second);
	}
	*/
	
	dizionario[' '] = ' ';
	
	//FILE* ifstream = fopen("input.txt","r");
	//FILE* ofstream = fopen("output.txt","w");
	
	int t;
	scanf("%d",&t);
	
	char c;
	scanf("%c",&c);
	
	for (int i=1; i<=t; ++i ) {
		printf("Case #%d: ",i);
		c = 'a';
		
		while (c != '\n') {
			scanf("%c",&c);
			if ( c != '\n' ) printf("%c", dizionario[c]);
		}
		
		printf("\n");
	}
	
	//	printf("%c\n",'a'+1);
	
	//fclose(ifstream);
	//fclose(ofstream);
	
	return 0;
}
