#include <set>
#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
using namespace std;

struct N
{
	double p;
	string f;
	N *l;
	N *r;
};

N *getNode(double pp, string ff)
{
	N *nn = new N();
	nn->p = pp;
	nn->f = ff;
	nn->l = nn->r = NULL;
	return nn;
}
void TrimWhiteSpaces(std::string& str)
{
	const size_t startPos = str.find_first_not_of(" \t\r\n");
	const size_t endPos   = str.find_last_not_of(" \t\r\n");
	if(startPos != std::string::npos && endPos != std::string::npos) 
		str = str.substr( startPos, endPos-startPos+1 );  
	else   
		str = "";
}

bool GetToken(std::istream &isr, std::string &token, const char delim)
{
	token = "";
	if ( std::getline(isr, token, delim) ) TrimWhiteSpaces(token);
	return token.length() > 0;
}

string readVals(int lines)
{
	string str;
	int c = 0;
	while (lines--)
	{
		string sv;
		getline(cin, sv);
		TrimWhiteSpaces(sv);
		str += sv;
	}
	return str;
}

N *ReadNodes(char * &str)
{
	if (*str == 0) return NULL;
	while (*str == ' ') ++str;
	++str;

	char lv[1000];
	char *c = strchr(str, ')');
	char *o = strchr(str, '(');
	if (c == NULL || ( o != NULL && c > o) )
	{
		strncpy(lv, str, o-str);
		lv [ o-str] = 0;
		str = o;
	}else
	{
		strncpy(lv, str, c-str);
		lv [ c-str] = 0;
		str = c;
	}

	string llv(lv);
	istringstream is(llv);
	double pp;
	is >> pp;
	char ds[100];
	is >> ds;
	N *n = getNode(pp, ds);
	if (*str != ')')
	{
		n->l = ReadNodes(str);
		n->r = ReadNodes(str);
	}
	++str;
	return n;
}

int getIntLine()
{
	int v;
	cin >> v;
	string dummy;
	getline(cin, dummy);
	return v;
}

void getAnimal( set<string> &f)
{
	string str;
	getline(cin, str);
	istringstream is(str);

	char name[100];
	is >> name;
	int t;
	is >> t;
	while (t--)
	{
		char fe[100];
		is >> fe;
		f.insert(fe);
	}


}
double getP(N* r, set<string> &fs)
{
	if (r == NULL) return 1.0;
	double p = r->p;
	if (fs.find(r->f) != fs.end()) p *= getP(r->l, fs);
	else p *= getP(r->r, fs);
	return p;
}

int main()
{
	int T = getIntLine();
	for (int i=0; i < T; ++i)
	{
		string str = readVals( getIntLine() );
		char v[1000], *p;
		strcpy(v, str.c_str());
		p = v;
		N *n=ReadNodes(p);
		printf("Case #%d:\n", i+1);

		int aniCount = getIntLine();
		while (aniCount--)
		{
			set<string> fs;
			getAnimal(fs);
			printf("%0.7f\n", getP(n, fs));
		}

	}
}
