#include<iostream>
#include<cstring>
#include<cstdlib>
#include<fstream>
using namespace std;
char key[200];
//ofstream out("k.txt");

int main()
{

	ifstream in("k.txt");
	for(int i=0; i<26;i++)
	{
		char x, y;
		in >> x >> y;
	//	cout << x << " " << y << endl;
		key[x] = y;
	}
	/*
	for(int i=97; i<123; i++)
		cout << (char)i << "-> " << key[i] << endl;
	*/

	int T;
	char line[200];
	cin.getline(line, 200);
	T = atoi(line);

//	cout << T << endl;
/*
	for(int x=1; x<=T; x++)
	{

		char inl[256];
		cin.getline(inl, 256);
		char ol[256];
		cin.getline(ol, 256);

		for(int i=0; i<strlen(inl); i++)
		{
			key[(inl[i])] = ol[i];
		}
		for(int i=97; i<122; i++)
			cout << (char)i << " " << key[i] << endl;

	}
	for(int i=97; i<=122; i++)
		out << (char)i << " " << key[i] << endl;


*/
	for(int x=1; x<=T; x++)
	{
		char line[256];
		cin.getline(line, 256);
		cout << "Case #"<<x<< ": ";
		for(int i=0; i<strlen(line); i++)
		{
			if(line[i] == ' ')
				cout << ' ';
			else
				cout << key[(line[i])];	
		}
		cout << endl;
	}



}
