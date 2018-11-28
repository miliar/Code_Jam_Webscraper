#include <string>
#include <fstream>
using namespace std;


void main()
{
	ifstream in("A-small-attempt0.in");
	ofstream out("output.txt");
	string T;
	getline(in,T);
	int t = atoi(T.c_str());
	char arr[26]= {'y', 'h' ,'e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	for (int i =0;i<t;i++){
		string s="";
		string normalEnglish="";
		getline(in,s);
		for (unsigned int j=0;j<s.length();j++){
		if (s[j]!= ' '){
			normalEnglish += arr[int(s[j]-'a')];
		}
		else {normalEnglish += ' ';}
		}
		out << "Case #"<<i+1<<": "<<normalEnglish<<endl;
	}
}