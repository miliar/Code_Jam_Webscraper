#include <iostream>
#include <cstdio>
#include <string>
#include <map>
using namespace std;
int n;
string S;
map<char,char> M;

int main()
{
	M.insert(pair<char,char>('a','y') );
	M.insert(pair<char,char>('b','h') );
	M.insert(pair<char,char>('c','e') );
	M.insert(pair<char,char>('d','s') );
	M.insert(pair<char,char>('e','o') );
	M.insert(pair<char,char>('f','c') );
	M.insert(pair<char,char>('g','v') );
	M.insert(pair<char,char>('h','x') );
	M.insert(pair<char,char>('i','d') );
	M.insert(pair<char,char>('j','u') );
	M.insert(pair<char,char>('k','i') );
	M.insert(pair<char,char>('l','g') );
	M.insert(pair<char,char>('m','l') );
	M.insert(pair<char,char>('n','b') );
	M.insert(pair<char,char>('o','k') );
	M.insert(pair<char,char>('p','r') );
	M.insert(pair<char,char>('q','z') );
	M.insert(pair<char,char>('r','t') );
	M.insert(pair<char,char>('s','n') );
	M.insert(pair<char,char>('t','w') );
	M.insert(pair<char,char>('u','j') );
	M.insert(pair<char,char>('v','p') );
	M.insert(pair<char,char>('w','f') );
	M.insert(pair<char,char>('x','m') );
	M.insert(pair<char,char>('y','a') );
	M.insert(pair<char,char>('z','q') );
	M.insert(pair<char,char>(' ',' ') );
	

	cin >> n;
	getline(cin,S);
	for(int i=1;i<=n;i++)
	{
		getline(cin,S);
		cout << "Case #"<< i << ": ";
		for(int i=0;i<S.size();i++)
		{
			cout << char(M[S[i]]);
		}
		cout << endl;
	}
	return 0;
}
