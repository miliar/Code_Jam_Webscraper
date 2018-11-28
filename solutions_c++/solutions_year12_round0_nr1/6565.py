#include<iostream>
#include<fstream>
#include<string>
#include<map>

using namespace std;

void createMap (map<char,char>& googlerese);
string translateGooglerese(string tempString, map<char,char>& map);

int main(){

	map<char,char> Googlerese;
	int testCases,temp=1;
	string gtext; //googlerese
	string translation;

	createMap(Googlerese);
	ifstream in;
	ofstream out;
	in.open("A-small-attempt0.in");
	out.open("output.txt");

	in >> testCases;
	getline(in,gtext);

	while (temp<=testCases)
	{
		getline(in,gtext);
		translation = translateGooglerese(gtext,Googlerese);
		out << "Case #" << temp << ": " << translation << endl;
		temp++;
		
	}


	return 0;

}

string translateGooglerese(string tempString, map<char,char>& googlerese)
{
	map<char,char>::iterator it;
	string translatedText = "";

	for(int i=0; i<tempString.length();i++)
	{
		it = googlerese.find(tempString.at(i));
		translatedText = translatedText + it->second;
	}

	return translatedText;
	
}
void createMap(map<char,char>& googlerese)
{
	googlerese.insert(pair<char,char>('a','y'));
	googlerese.insert(pair<char,char>('b','h'));
	googlerese.insert(pair<char,char>('c','e'));
	googlerese.insert(pair<char,char>('d','s'));
	googlerese.insert(pair<char,char>('e','o'));
	googlerese.insert(pair<char,char>('f','c'));
	googlerese.insert(pair<char,char>('g','v'));
	googlerese.insert(pair<char,char>('h','x'));
	googlerese.insert(pair<char,char>('i','d'));
	googlerese.insert(pair<char,char>('j','u'));
	googlerese.insert(pair<char,char>('k','i'));
	googlerese.insert(pair<char,char>('l','g'));
	googlerese.insert(pair<char,char>('m','l'));
	googlerese.insert(pair<char,char>('n','b'));
	googlerese.insert(pair<char,char>('o','k'));
	googlerese.insert(pair<char,char>('p','r'));
	googlerese.insert(pair<char,char>('q','z'));
	googlerese.insert(pair<char,char>('r','t'));
	googlerese.insert(pair<char,char>('s','n'));
	googlerese.insert(pair<char,char>('t','w'));
	googlerese.insert(pair<char,char>('u','j'));
	googlerese.insert(pair<char,char>('v','p'));
	googlerese.insert(pair<char,char>('w','f'));
	googlerese.insert(pair<char,char>('x','m'));
	googlerese.insert(pair<char,char>('y','a'));
	googlerese.insert(pair<char,char>('z','q'));
	googlerese.insert(pair<char,char>(' ',' '));
}