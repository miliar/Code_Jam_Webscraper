#include <iostream>
#include <fstream>
#include <string>
#include <string.h>
#include <algorithm>

using namespace std;
const char* encoded1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
const char* encoded2 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
const char* encoded3 = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
const char* encoded4 = "y qee";
const char* encoded5 = "z";

const char* decoded1 = "our language is impossible to understand";
const char* decoded2 = "there are twenty six factorial possibilities";
const char* decoded3 = "so it is okay if you want to just give up";
const char* decoded4 = "a zoo";
const char* decoded5 = "q";

string translateText(string s, char* ttable)
{
	string out;
	for(unsigned int i=0; i < s.length(); i++)
		if(s[i]!=' ')
			out+=ttable[s[i]-'a'];
		else
			out+=' ';
	return out;
}

void addmapping(const char* encoded, const char* decoded, char* ttable)
{
	for(unsigned int i=0; i < strlen(encoded);i++)
		if(encoded[i]!=' ')
			ttable[encoded[i]-'a'] = decoded[i];
}

int main() {
	ifstream is("A-small-attempt0.in");
	ofstream os("A-small-attempt0.out");
	if(!is)
		return -1;
	int N = 0; is >> N;
	char ttable[26];
	for(int i=0; i<26; i++)
		ttable[i] = '_';
	addmapping(encoded1, decoded1, ttable);
	addmapping(encoded2, decoded2, ttable);
	addmapping(encoded3, decoded3, ttable);
	addmapping(encoded4, decoded4, ttable);
	addmapping(encoded5, decoded5, ttable);
	string s;
	getline ( is, s );
	for(int cnt=1; cnt<=N; cnt++)
	{
		getline ( is, s );
		cout << "Case #" << cnt << ": " << translateText(s, ttable) << endl;
		os << "Case #" << cnt << ": " << translateText(s, ttable) << endl;
	}
	is.close();
	os.close();
}
