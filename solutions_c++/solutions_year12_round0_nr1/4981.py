#include <iostream>
using namespace std;

char mapping(const char& c){
	switch(c){
		case 'a':
			return 'y';
		case 'b':
			return 'h';
		case 'c':
			return 'e';
		case 'd':
			return 's';
		case 'e':
			return 'o';
		case 'f':
			return 'c';
		case 'g':
			return 'v';
		case 'h':
			return 'x';
		case 'i':
			return 'd';
		case 'j':
			return 'u';
		case 'k':
			return 'i';
		case 'l':
			return 'g';
		case 'm':
			return 'l';
		case 'n':
			return 'b';
		case 'o':
			return 'k';
		case 'p':
			return 'r';
		case 'q':
			return 'z';
		case 'r':
			return 't';
		case 's':
			return 'n';
		case 't':
			return 'w';
		case 'u':
			return 'j';
		case 'v':
			return 'p';
		case 'w':
			return 'f';
		case 'x':
			return 'm';
		case 'y':
			return 'a';
		case 'z':
			return 'q';
		default:
			return c;

	}
}

int main()
{
	int N;
	cin>>N;
	cin.get();
	for(int i=1; i<=N; i++){
		cout << "Case #"<<i<<": ";
		while(cin.peek()!='\n'){
			cout << mapping(cin.get());
		}
		cout << '\n';
		cin.get();
	}
	return 0;
}
