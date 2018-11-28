#include <iostream>
#include <fstream>
using namespace std;



char change(char);
void main(){
	int test;
	char next,done;
	ifstream in;
	in.open("a.txt");
	ofstream out;
	out.open("b.txt");
	in>>test;
	in.get();
	for (int i=1;i<=test;i++){
		out<<"Case #"<<i<<": ";
		while(in.get(next)){
			if (next=='\n')break;
	done=change(next);
	out.put(done);
	}
	out<<endl;
	}
}

	char change(char n){
	switch(n){
	case 'y': return 'a'; break;
	case 'n': return 'b'; break;
	case 'f': return 'c'; break;
	case 'i': return 'd'; break;
	case 'c': return 'e'; break;
	case 'w': return 'f'; break;
	case 'l': return 'g'; break;
	case 'b': return 'h'; break;
	case 'k': return 'i'; break;
	case 'u': return 'j'; break;
	case 'o': return 'k'; break;
	case 'm': return 'l'; break;
	case 'x': return 'm'; break;
	case 's': return 'n'; break;
	case 'e': return 'o'; break;
	case 'v': return 'p'; break;
	case 'z': return 'q'; break;
	case 'p': return 'r'; break;
	case 'd': return 's'; break;
	case 'r': return 't'; break;
	case 'j': return 'u'; break;
	case 'g': return 'v'; break;
	case 't': return 'w'; break;
	case 'h': return 'x'; break;
	case 'a': return 'y'; break;
	case 'q': return 'z'; break;
	case ' ': return ' '; break;

	
	
	}
	
	
	}
