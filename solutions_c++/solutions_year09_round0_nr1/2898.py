#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using std::string;

class AlienLang
{
	public:
		AlienLang() { matches = 0; }
		~AlienLang() {}
	
		void MakeMatch(std::vector<string> &lang);
		void Generate(const string &ss);
		int Matches() { return matches; }
	private:
		string Parenthesis(const string &ss, int &i);
		bool CheckMatch(const string &ss);
		
		std::vector<string> tkns;
		int matches;
};

void AlienLang::Generate(const string &ss)
{
int i;
string aux;

	for (i=0; i<ss.length(); i++)
	{
		if (ss[i] == '(')
			tkns.push_back(Parenthesis(ss, i));
		else
		{
			aux.push_back(ss[i]);
			tkns.push_back(aux);
			aux.clear();
		}
	
	}
}

string AlienLang::Parenthesis(const string &ss, int &i)
{
string aux;

	i++;
	for (; ss[i] != ')'; i++)
		aux.push_back(ss[i]);
		
	return aux;
}

bool AlienLang::CheckMatch(const string &ss)
{
int i;
bool match = true;

	for (i=0; i<ss.length(); i++)
	{
		if (tkns[i].find(ss[i]) == string::npos)
			match = false;	
	}
	
	return match;
}

void AlienLang::MakeMatch(std::vector<string> &lang)
{
int i;

	for (i=0; i<lang.size(); i++)
	{
		if (CheckMatch(lang[i]))
			matches++;
	}
}

int main()
{
std::vector<string> lang;
std::ifstream in;
string aux;
int nLang, nTkns, i;

	in.open("alien_in");
	if (!in.is_open())
	{
		std::cerr << "Error opening file \"alien_in\"" << std::endl;
		return 1;
	}
	
	in >> nLang; //dummy;
	in >> nLang;
	in >> nTkns;
	
	//Load "lang"
	for (i=0; i<nLang; i++)
	{
		in >> aux;
		lang.push_back(aux);
	}
	
	//load alien words
	for (i=0; i<nTkns; i++)
	{
	AlienLang tmp;
	
		in >> aux;
		tmp.Generate(aux);
		tmp.MakeMatch(lang);
		std::cout << "Case #" << i+1 << ": " << tmp.Matches() << std::endl;
	}
	


	return 0;

}
