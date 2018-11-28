
#include <iostream>
#include <string>
#include <algorithm>


char MAP[26] = {
	'y', //a
	'n',
	'f' ,
	'i',
	'c',
	'w', //f
	'l',
	'b',
	'k',
	'u',
	'o',
	'm', //l
	'x',
	's',
	'e', //o
	'v', //p
	'z',
	'p',
	'd',
	'r', //t
	'j',
	'g',
	't', //w
	'h',
	'a',
	'q'
};

char IMAP[26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
using namespace std;

int main () {
	
	int T;
	cin >> T;
	cin.ignore();
	for (int i=0;i < T;++i)
	{
		std::string l;
		std::getline(cin,l);
		
		std::string res = l;
		
		for (int j=0; j< l.size();++j)
			if (l[j] >= 'a' && l[j] <= 'z')
				res[j] = IMAP[l[j]-'a'];
			
		std::cout << "Case #" << i+1 << ": " << res << std::endl; 
	}
	return 0;
}