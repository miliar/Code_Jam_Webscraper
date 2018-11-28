#include <fstream.h>
#include <string.h>
#include <iostream.h>

using namespace std;

const char EOL = '\0';

// LUT
string from("ejpmyslckdxvnribtahwfougzq ");
string   to("ourlangeismpbtdhwyxfckjvqz ");

void main() {

	// fájl megnyitások
	ifstream in("A-small-attempt3.in");
	if(!in)	cout << ".txt nem nyitható meg!\n";
	
	ofstream out;
	out.open("out.txt");
	if(!out)	cout << "out.txt nem hozható létre!\n";

	
	// buffer
	char str[101];
	char ch[3];
	int lines;
	
	// hány eset?
	in.getline(ch, 3);
	lines = atoi(ch);

	// soronként
	for(int i = 1; i <= lines; i++) {
	
		// beolvas
		in.getline(str, 101);
cout << str << endl;
		// átalakítás
		int j = 0;
		size_t pos;
		while(str[j] != EOL) {
		
			// megkeressük a helyét
			pos = from.find(str[j]);
			
			// ha van ilyen, akkor csere
			//if(pos != string::npos)
	str[j] = to.at(pos);
			
			// következõ
			j++;
		}
cout << str << endl;		
		// kiír
		out << "Case #" << i << ": " << str << endl;
	}


	// fájl bezárások
	in.close();
	out.close();
}