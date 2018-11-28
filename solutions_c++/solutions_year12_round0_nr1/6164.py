#include <iostream>
#include <string>
using namespace std;

int main()
{
	int T;
	string G;
	cin >> T;
	cin.ignore();
	for (int i=0;i<T;i++){
		cout << "Case #" << i+1 << ": ";
		getline(cin, G);
		for(unsigned int t=0;t<G.length();t++){
			switch (G[t]) {
				case 'a': cout << "y"; break;
				case 'b': cout << "h"; break;
				case 'c': cout << "e"; break;
				case 'd': cout << "s"; break;
				case 'e': cout << "o"; break;
				case 'f': cout << "c"; break;
				case 'g': cout << "v"; break;
				case 'h': cout << "x"; break;
				case 'i': cout << "d"; break;
				case 'j': cout << "u"; break;
				case 'k': cout << "i"; break;
				case 'l': cout << "g"; break;
				case 'm': cout << "l"; break;
				case 'n': cout << "b"; break;
				case 'o': cout << "k"; break;
				case 'p': cout << "r"; break;
				case 'q': cout << "z"; break;
				case 'r': cout << "t"; break;
				case 's': cout << "n"; break;
				case 't': cout << "w"; break;
				case 'u': cout << "j"; break;
				case 'v': cout << "p"; break;
				case 'w': cout << "f"; break;
				case 'x': cout << "m"; break;
				case 'y': cout << "a"; break;
				case 'z': cout << "q"; break;
				default: cout << " "; break;
			} // end of switch
		} // text iter
		cout << endl;
	}
}