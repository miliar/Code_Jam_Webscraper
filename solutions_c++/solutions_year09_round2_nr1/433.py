#include <iostream>
#include <sstream>
#include <vector>
#include <set>
using namespace std;
double strToD(string s) { istringstream sin(s); double r; sin >> r; return r;} 

double getans(double p,vector<string> Tokens,set<string> CS)
{
	p*= strToD(Tokens[1]);
	if(Tokens.size() == 3) return p;
	else 
	{
		int LR = 1,mid = 0;
		for(int i = 4; ; ++i)
		{
			if(Tokens[i] == "(") LR ++;
			else if(Tokens[i] == ")") LR--;
			if( LR == 0) 
			{
				mid = i;
				break;
			}
		}
		if(CS.find(Tokens[2]) == CS.end())
		{
			vector<string> nn;
			for(int i = mid + 1; i< Tokens.size() -1; ++i)
			{
				nn.push_back(Tokens[i]);
			}
			return getans(p,nn,CS);
		}
		else
		{
			vector<string> nn;
			for(int i = 3; i<= mid; ++i)
			{
				nn.push_back(Tokens[i]);
			}
			return getans(p,nn,CS);
		}
	}
}
int main()
{
	int T;
	cin >> T;
	for(int s = 1; s<= T; ++s)
	{
		printf("Case #%d:\n",s);
		int m,n;
		cin >> m;
		vector<string> Token;
		char p[1000];
		string L;
		string word;
		getchar();
		for(int i = 0; i< m; ++i)
		{
			gets(p);
			L = p;
			istringstream sin(L);
			while(sin >> word)
			{
				if(word[0] == '(' && word[word.length()-1] == ')')
				{
					Token.push_back("(");
					if(word.length()>2)
						Token.push_back(word.substr(1,word.length()-2));
					Token.push_back(")");
				}
				else if( word[0] == '(')
				{
					Token.push_back("(");
					if(word.length() > 1)
						Token.push_back(word.substr(1,word.length()-1));
				}
				else if(word[word.length() - 1] == ')')
				{
					if(word.length()>1)
						Token.push_back(word.substr(0,word.length()-1));
					Token.push_back(")");
				}
				else
				{
					Token.push_back(word);
				}
			}
		}
		cin >> n;
		string name;
		int a;
		set<string> CS;
		for(int i = 0; i< n; ++i)
		{
			cin >> name >> a;
			CS.clear();
			for(int j = 0; j< a; ++j)
			{
				cin >> name;
				CS.insert(name);
			}
			printf("%.7lf\n",getans(1.0,Token,CS));
		}
	}
}