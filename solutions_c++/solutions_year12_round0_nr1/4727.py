#include<fstream>
#include<map>
#include<string>

using namespace std;

int main(){
	//variabiles
	int n, i, j, string_length;
	char caracter;
	map<char, char> decoder;
	string line;
	ifstream fin("A-small-attempt2.in");
	ofstream fout("A-small-attempt2.out");
	
	//ensuring enough space for the string
	if(line.capacity() < 100)
		line.reserve(100*sizeof(char));
		
	//build "decoder" map
	decoder['a'] = 'y';
	decoder['b'] = 'h';
	decoder['c'] = 'e';
	decoder['d'] = 's';
	decoder['e'] = 'o';
	decoder['f'] = 'c';
	decoder['g'] = 'v';
	decoder['h'] = 'x';
	decoder['i'] = 'd';
	decoder['j'] = 'u';
	decoder['k'] = 'i';
	decoder['l'] = 'g';
	decoder['m'] = 'l';
	decoder['n'] = 'b';
	decoder['o'] = 'k';
	decoder['p'] = 'r';
	decoder['q'] = 'z';
	decoder['r'] = 't';
	decoder['s'] = 'n';
	decoder['t'] = 'w';
	decoder['u'] = 'j';
	decoder['v'] = 'p';
	decoder['w'] = 'f';
	decoder['x'] = 'm';
	decoder['y'] = 'a';
	decoder['z'] = 'q';
	
	
	//reading data
	fin>>n;
	fin.ignore(256, '\n');
	
	//for each test
	for(i = 1; i <= n; i++){
	
		//read line
		getline(fin, line);
		
		//change letters
		string_length = line.length();
		for( j = 0; j < string_length; j++){
			caracter = line.at(j);
			if(caracter != ' ')
				line.replace(j, 1, 1, decoder[caracter]);
		}
	
		//write line in output file
		if(i >= 2) 
			fout<<'\n';
		fout<<"Case #"<<i<<": "<<line;
	}
	
	//close everything
	fin.close();
	fout.close();
	
	//done!
	return 0;
}