#include <fstream.h>
#include <string.h>
#include <iostream.h>

using namespace std;

const char EOL = '\0';

// LUT
string from("ejpmyslckdxvnribtahwfougzq ");
string   to("ourlangeismpbtdhwyxfckjvqz ");

void main() {

	// f�jl megnyit�sok
	ifstream in("A-small-attempt3.in");
	if(!in)	cout << ".txt nem nyithat� meg!\n";
	
	ofstream out;
	out.open("out.txt");
	if(!out)	cout << "out.txt nem hozhat� l�tre!\n";

	
	// buffer
	char str[101];
	char ch[3];
	int lines;
	
	// h�ny eset?
	in.getline(ch, 3);
	lines = atoi(ch);

	// soronk�nt
	for(int i = 1; i <= lines; i++) {
	
		// beolvas
		in.getline(str, 101);
cout << str << endl;
		// �talak�t�s
		int j = 0;
		size_t pos;
		while(str[j] != EOL) {
		
			// megkeress�k a hely�t
			pos = from.find(str[j]);
			
			// ha van ilyen, akkor csere
			//if(pos != string::npos)
	str[j] = to.at(pos);
			
			// k�vetkez�
			j++;
		}
cout << str << endl;		
		// ki�r
		out << "Case #" << i << ": " << str << endl;
	}


	// f�jl bez�r�sok
	in.close();
	out.close();
}