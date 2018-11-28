#include <iostream>
#include <string>

using namespace std;

int main()
{
	int T;
	char ch[27] = "00000000000000000000000000";
	string inStr;

	string str[3][2] = {
		{
			"ejp mysljylc kd kxveddknmc re jsicpdrysi",
			"our language is impossible to understand"
		},
		{
			"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
			"there are twenty six factorial possibilities"
		},
		{
			"de kr kd eoya kw aej tysr re ujdr lkgc jv",
			"so it is okay if you want to just give up"
		}	
	};

	for (int i = 0; i < 3; i++) {
		//cout << "i: " << i << " => " << str[i][0] << endl;
		//cout << "i: " << i << " => " << str[i][1] << endl;
		
		for (int j = 0; j < str[i][0].length(); j++) {
			ch[str[i][0].at(j)-'a'] = str[i][1].at(j);	
		}	
	}
	
	for (int i = 0; i < 26; i++) {
	//	cout << (char)(i + 'a') << " ";
	}	
	//cout << endl;
	
	for (int i = 0; i < 26; i++) {
	//	cout << ch[i] << " ";	
	}
	//cout << endl;
	
	// a b c d e f g h i j k l m n o p q r s t u v w x y z
	// y n f i c w l b k u o m x s e v 0 p d r j g t h a 0
	// q, z => q, z | z, q
	
	/*
	ch['q'-'a'] = 'q';
	ch['z'-'a'] = 'z';
	*/
	
	ch['q'-'a'] = 'z';
	ch['z'-'a'] = 'q';
	
	
	
	cin >> T;
	getline (cin, inStr);

		
	for (int t = 0; t < T; t++) {
		getline (cin, inStr);
		
		for (int i = 0; i < inStr.length(); i++) {
			inStr.at(i) = ch[inStr.at(i) - 'a'];	
		}
		
		cout << "Case #" << (t + 1) << ": " << inStr << endl;		
	}
	
	return 0;	
}