#include <iostream>
#include <string>
using namespace std;

string convert(string ori);
int main(int argc, char const *argv[])
{
	string gLan;
	string eLan;
	int n;

	cin >> n;
	cin.ignore(1000, '\n');
	for (int i = 0; i < n; ++i)
	{
		getline(cin, gLan);
		eLan = convert(gLan);
		cout << "Case #" << i+1 << ": " << eLan << endl;
	}
	return 0;
}

string convert(string gLan){
	string rs = "";
	for (int i = 0; i < gLan.length(); ++i)
	{
		switch(gLan[i]){
			case 'y':
				rs += 'a';
				break;
			case 'n':
				rs += 'b';
				break;
			case 'f':
				rs += 'c';
				break;
			case 'i':
				rs += 'd';
				break;
			case 'c':
				rs += 'e';
				break;
			case 'w':
				rs += 'f';
				break;
			case 'l':
				rs += 'g';
				break;
			case 'b':
				rs += 'h';
				break;
			case 'k':
				rs += 'i';
				break;
			case 'u':
				rs += 'j';
				break;
			case 'o':
				rs += 'k';
				break;
			case 'm':
				rs += 'l';
				break;
			case 'x':
				rs += 'm';
				break;
			case 's':
				rs += 'n';
				break;
			case 'e':
				rs += 'o';
				break;
			case 'v':
				rs += 'p';
				break;
			case 'z':
				rs += 'q';
				break;
			case 'p':
				rs += 'r';
				break;
			case 'd':
				rs += 's';
				break;
			case 'r':
				rs += 't';
				break;
			case 'j':
				rs += 'u';
				break;
			case 'g':
				rs += 'v';
				break;
			case 't':
				rs += 'w';
				break;
			case 'h':
				rs += 'x';
				break;
			case 'a':
				rs += 'y';
				break;
			case 'q':
				rs += 'z';
				break;
			default:
				rs += ' ';
				break; 
		}
	}
	return rs;
}
