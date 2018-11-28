#include <iostream>
#include <string>
#include <algorithm>
#include <map>

using namespace std;

map<char, char> translation;

int solve()
{
	return 0;
}

void learn()
{
	translation['a'] = 'y';
	translation['o'] = 'e';
	translation['z'] = 'q';
	
	// post 
	translation['q'] = 'z';

	string coded = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
	string original = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
	for(int i=0;i<coded.length();++i){
		translation[coded[i]] = original[i];
	}

	/*string alphabets = "abcdefghijklmnopqrstuvwxyz";
	string code;
	for(int i=0;i<alphabets.length();++i){
		code += translation[alphabets[i]];
	}

	string codeCopy = code;
	sort(codeCopy.begin(), codeCopy.end());
	cout << alphabets << endl << code << endl << codeCopy;*/
}

//int SpeakingInTongues()
int main()
{
	learn();

	freopen("SpeakingInTonguesS.in", "r", stdin);
	freopen("SpeakingInTonguesS.out", "w", stdout);

	int t;
	cin >> t;
	string line;
	getline(cin, line);
	for(int i=1;i<=t;++i)
	{
		getline(cin, line);
		
		string original;
		for(int j=0;j<line.length();++j){
			original += translation[line[j]];
		}

		cout << "Case #" << i << ": ";
		cout << original << endl;
	}
	return 0;
}