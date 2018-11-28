#include <iostream>
#include <string>
#include <map>
using namespace std;

int main()
{
	int T;
	cin >> T;
	cin.ignore();
	string abc = "abcdefghijklmnopqrstuvwxyz ";
	string goo = "yhesocvxduiglbkrztnwjpfmaq ";
	map <char,char> mapo;
	for(int i = 0;i<abc.length();i++)
		mapo[abc[i]] = goo[i];
	for(int i = 0;i<T;i++)
	{
		string s,res;
		getline(cin,s);
		res = "";
		for(int j = 0;j<s.length();j++)	
			res += mapo[s[j]];
		cout << "Case #"<<i+1<<": "<<res << endl;
		
	}

} 
