#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <fstream>
using namespace std;

map<char, char> googlet;
typedef pair<char,char> cpair;
string translate(string inp)
{
	string out;
	for(string::iterator it = inp.begin(); it != inp.end(); ++it)
		out.append(1,googlet.find(*it)->second);
	return out;
}
int main(int argc, char * argv[])
{
	googlet.insert(cpair('a','y'));
	googlet.insert(cpair('b', 'h'));
	googlet.insert(cpair('c', 'e'));
	googlet.insert(cpair('d', 's'));
	googlet.insert(cpair('e', 'o'));
	googlet.insert(cpair('f', 'c'));
	googlet.insert(cpair('g', 'v'));
	googlet.insert(cpair('h', 'x'));
	googlet.insert(cpair('i', 'd'));
	googlet.insert(cpair('j', 'u'));
	googlet.insert(cpair('k', 'i'));
	googlet.insert(cpair('l', 'g'));
	googlet.insert(cpair('m', 'l'));
	googlet.insert(cpair('n', 'b'));
	googlet.insert(cpair('o', 'k'));
	googlet.insert(cpair('p', 'r'));
	googlet.insert(cpair('q', 'z'));
	googlet.insert(cpair('r', 't'));
	googlet.insert(cpair('s', 'n'));
	googlet.insert(cpair('t', 'w'));
	googlet.insert(cpair('u', 'j'));
	googlet.insert(cpair('v', 'p'));
	googlet.insert(cpair('w', 'f'));
	googlet.insert(cpair('x', 'm'));
	googlet.insert(cpair('y', 'a'));
	googlet.insert(cpair('z', 'q'));
	googlet.insert(cpair(' ', ' '));
	int sz;
	cout << "input a file" << endl;
	string file;
	cin >> file;
	cout << "output a file" << endl;
	string ofile;
	cin >> ofile;
	fstream f(file);
	if(!f.is_open())
	{
		return 0;
	}
	f >> sz;
	f.ignore();
	string x;
	vector<string> cases;
	for(int i = 0; i < sz; ++i)
	{
		getline(f, x);
		cases.push_back(translate(x));
	}
	fstream of(ofile);
	for(vector<string>::iterator it = cases.begin(); it != cases.end(); ++it)
	{
		of << "Case #" << it - cases.begin() + 1 << ": " << *it << endl;
	}
	return 0;
}