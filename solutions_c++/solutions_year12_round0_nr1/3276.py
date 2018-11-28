#include <fstream>
using namespace std;

void translate(char* input, int size){
	for(int i = 0; i < size; i++)
	{
		char in = input[i];
		
		switch(in)
		{
		case 'a':
			input[i] = 'y';
			break;
		case 'b':
			input[i] = 'h';
			break;
		case 'c':
			input[i] = 'e';
			break;
		case 'd':
			input[i] = 's';
			break;
		case 'e':
			input[i] = 'o';
			break;
		case 'f':
			input[i] = 'c';
			break;
		case 'g':
			input[i] = 'v';
			break;
		case 'h':
			input[i] = 'x';
			break;
		case 'i':
			input[i] = 'd';
			break;
		case 'j':
			input[i] = 'u';
			break;
		case 'k':
			input[i] = 'i';
			break;
		case 'l':
			input[i] = 'g';
			break;
		case 'm':
			input[i] = 'l';
			break;
		case 'n':
			input[i] = 'b';
			break;
		case 'o':
			input[i] = 'k';
			break;
		case 'p':
			input[i] = 'r';
			break;
		case 'q':
			input[i] = 'z';
			break;
		case 'r':
			input[i] = 't';
			break;
		case 's':
			input[i] = 'n';
			break;
		case 't':
			input[i] = 'w';
			break;
		case 'u':
			input[i] = 'j';
			break;
		case 'v':
			input[i] = 'p';
			break;
		case 'w':
			input[i] = 'f';
			break;
		case 'x':
			input[i] = 'm';
			break;
		case 'y':
			input[i] = 'a';
			break;
		case 'z':
			input[i] = 'q';
			break;
		}
	}
}

int main(){
	ifstream fin("C:\\Users\\ting\\Documents\\Visual Studio 2008\\Projects\\Google2012\\Debug\\file.in");
	ofstream oin("C:\\Users\\ting\\Documents\\Visual Studio 2008\\Projects\\Google2012\\Debug\\file.out");

	int cases;
	int counter = 1;
	fin >> cases;
	fin.ignore(100, '\n');

	while(counter <= cases){
		char googlerese[101];
		fin.getline(googlerese, 101);

		translate(googlerese, 101);

		oin << "Case #" << counter << ": " << googlerese << endl;;
		counter++;
	}

	return 0;
}