#include<vector>
#include<iostream>
#include<string>
#include<fstream>
using namespace std;
int main(){
	ifstream cin;
	ofstream cout;
	cin.open("A-small-attempt1.in");
	cout.open("output.txt");
	vector<char> m;
	m.push_back('y');
	m.push_back('h');
	m.push_back('e');
	m.push_back('s');
	m.push_back('o');
	m.push_back('c');
	m.push_back('v');
	m.push_back('x');
	m.push_back('d');
	m.push_back('u');
	m.push_back('i');
	m.push_back('g');
	m.push_back('l');
	m.push_back('b');
	m.push_back('k');
	m.push_back('r');
	m.push_back('z');
	m.push_back('t');
	m.push_back('n');
	m.push_back('w');
	m.push_back('j');
	m.push_back('p');
	m.push_back('f');
	m.push_back('m');
	m.push_back('a');
	m.push_back('q');
	int n;
	string s1,s2;
	cin>>n;
	ws(cin);
	for(int i=0;i<n;i++)
	{
		getline(cin,s1);
		for(int j=0;j<s1.size();j++){
			if(s1[j]!=' ') s2+=m[s1[j]-'a'];
			else s2+=' ';
		}
		cout<<"Case #"<<i+1<<": "<<s2<<endl;
		s2.clear();
	}
	return 0;
}




