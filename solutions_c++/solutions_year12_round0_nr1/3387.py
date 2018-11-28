#include <iostream>
#include <fstream>
#include <regex>

using namespace std;

int main() {
	fstream f, g;
	f.open("input.txt",ios::in);
	g.open("output.txt",ios::out);
	int line;
	int ln = 1;
	char c;	// s'in ilk karakteri
	f >> line;
	c = f.get();
	//for(int j=0; j<line; j++){
		
		//char s[101];	// isleyecegimiz string
		//f.getline(s,101);
		//g << s;
		g << "Case #1: ";	// cevabimiz
		
		for(int i=0 ; !f.eof(); i++) {	// s'in butun karakterleri icin
			c = f.get();
			switch (c) {
			case '\n' : g << "\nCase #" << ++ln << ": "; break;
			case ' ' : g << " "; break;
			case 'a' : g << "y"; break;
			case 'b' : g << "h"; break;
			case 'c' : g << "e"; break;
			case 'd' : g << "s"; break;
			case 'e' : g << "o"; break;
			case 'f' : g << "c"; break;
			case 'g' : g << "v"; break;
			case 'h' : g << "x"; break;
			case 'i' : g << "d"; break;
			case 'j' : g << "u"; break;
			case 'k' : g << "i"; break;
			case 'l' : g << "g"; break;
			case 'm' : g << "l"; break;
			case 'n' : g << "b"; break;
			case 'o' : g << "k"; break;
			case 'p' : g << "r"; break;
			case 'q' : g << "z"; break;
			case 'r' : g << "t"; break;
			case 's' : g << "n"; break;
			case 't' : g << "w"; break;
			case 'u' : g << "j"; break;
			case 'v' : g << "p"; break;
			case 'w' : g << "f"; break;
			case 'x' : g << "m"; break;
			case 'y' : g << "a"; break;
			case 'z' : g << "q"; break;
			//default : t.append("*"); break;
			}
		}
	//}
	f.close();
	g.close();
	return 0;
}