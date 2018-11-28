#include <iostream>
#include <fstream>
using namespace std;

struct mapping{
	char google;
	char normal;
};

class test{
	string s;
	int len;
};

mapping map[30];

test* t;
int numOftests=0;


int at=0;

void insert(char a,char b){
	map[at].google = a;
	map[at].normal= b;
	at++;
}


char getmap(char in){
	if(in == ' '){
		return ' ';
	}
	int index = in-'a';
	return map[index].normal;
}




void readIn(){
	ifstream in ("in.txt");
	in>> numOftests ;
	char a[1000];
	FILE * f = fopen("out.txt","w");
	in.getline(a,1000); //remove firs newline.
	for(int i=0;i<numOftests;i++){
		char input[101];
		int len =  in.getline(input,101).gcount();
		char result[100];
		fprintf(f,"Case #%i: ",i+1);
		for(int l =0;l<len;l++){
			if(input[l]=='\0'){
				break;
			}
			fprintf(f,"%c",(1,getmap(input[l])));
		}
		fprintf(f,"\n");
	}
	fclose(f);
}





int main(){
	insert('a','y');
	insert('b','h');
	insert('c','e');
	insert('d','s');
	insert('e','o');
	insert('f','c');
	insert('g','v');
	insert('h','x');
	insert('i','d');
	insert('j','u');
	insert('k','i');
	insert('l','g');
	insert('m','l');
	insert('n','b');
	insert('o','k');
	insert('p','r');
	insert('q','z');
	insert('r','t');
	insert('s','n');
	insert('t','w');
	insert('u','j');
	insert('v','p');
	insert('w','f');
	insert('x','m');
	insert('y','a');
	insert('z','q');
	readIn();
	cin.get();

}