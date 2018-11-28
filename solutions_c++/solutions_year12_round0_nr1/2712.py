#include <iostream>
#include <string>

using namespace std;

int main()
{
	char arr[256];
	arr['a'] = 'y';
	arr['b'] = 'h';
	arr['c'] = 'e';
	arr['d'] = 's';
	arr['e'] = 'o';
	arr['f'] = 'c';
	arr['g'] = 'v';
	arr['h'] = 'x';
	arr['i'] = 'd';
	arr['j'] = 'u';
	arr['k'] = 'i';
	arr['l'] = 'g';
	arr['m'] = 'l';
	arr['n'] = 'b';
	arr['o'] = 'k';
	arr['p'] = 'r';
	arr['q'] = 'z';
	arr['r'] = 't';
	arr['s'] = 'n';
	arr['t'] = 'w';
	arr['u'] = 'j';
	arr['v'] = 'p';
	arr['w'] = 'f';
	arr['x'] = 'm';
	arr['y'] = 'a';
	arr['z'] = 'q';
	arr[' '] = ' ';
	int N;
	cin>>N;
	string line1;
	getline(cin, line1);
	for(int i = 0; i<N; i++){
		string line;
		getline(cin, line);
		int length = line.length();
		cout<<"Case #"<<(i+1)<<": ";
		for(int j = 0; j<length; j++){
			cout<<arr[line[j]];
		}
		cout<<endl;
	}
}

