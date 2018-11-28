// A.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <map>
using namespace std;

int main()
{
	int tests;
	char origText[110];

    map<char,char> translationMap;

    translationMap['a']='y';
    translationMap['b']='h';
    translationMap['c']='e';
    translationMap['d']='s';
    translationMap['e']='o';
    translationMap['f']='c';
    translationMap['g']='v';
    translationMap['h']='x';
    translationMap['i']='d';
    translationMap['j']='u';
    translationMap['k']='i';
    translationMap['l']='g';
    translationMap['m']='l';
    translationMap['n']='b';
    translationMap['o']='k';
    translationMap['p']='r';
    translationMap['q']='z';
    translationMap['r']='t';
    translationMap['s']='n';
    translationMap['t']='w';
    translationMap['u']='j';
    translationMap['v']='p';
    translationMap['w']='f';
    translationMap['x']='m';
    translationMap['y']='a';
    translationMap['z']='q';
    translationMap[' ']=' ';

	cin >> tests;
    cin.getline(origText, 110);
	for(int i = 1; i<=tests; i++){
		cin.getline(origText, 110);
		cout << "Case #" << i << ": ";
        for(int j = 0; origText[j]!='\0';j++){
            cout << translationMap[origText[j]];
        }
        cout << "\n";
	}
}

