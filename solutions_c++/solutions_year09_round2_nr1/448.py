#include <iostream>
#include <sstream>
#include <vector>
#include <set>
using namespace std;
double strToDouble(string s) { istringstream sin(s); double r; sin >> r; return r;} 

double getans(double p,vector<string> tokens,set<string> cha)
{
	p*= strToDouble(tokens[1]);
	if(tokens.size() == 3)
	{
		return p;
	}
	else 
	{
		int pq = 1;
		int mid = 0;
		for(int i = 4; ; ++i)
		{
			if(tokens[i] == "(") pq ++;
			else if(tokens[i] == ")") pq--;
			if( pq == 0) 
			{
				mid = i;
				break;
			}
		}
		if(cha.find(tokens[2]) == cha.end())
		{// no this character
			vector<string> ntokens;
			for(int i = mid + 1; i< tokens.size() -1; ++i)
			{
				ntokens.push_back(tokens[i]);
			}
			return getans(p,ntokens,cha);
		}
		else
		{
			vector<string> ntokens;
			for(int i = 3; i<= mid; ++i)
			{
				ntokens.push_back(tokens[i]);
			}
			return getans(p,ntokens,cha);
		}
	}
}
int main()
{
	int T;
	cin >> T;
	for(int r = 1; r<= T; ++r)
	{
		printf("Case #%d:\n",r);
		int m,n;
		cin >> m;
		vector<string> token;
		char p[1000];
		string L;
		string w;
		getchar();
		for(int i = 0; i< m; ++i)
		{
			gets(p);
			L = p;
			istringstream sin(L);
			while(sin >> w)
			{
				if(w[0] == '(' && w[w.length()-1] == ')')
				{
					token.push_back("(");
					if(w.length()>2)
						token.push_back(w.substr(1,w.length()-2));
					token.push_back(")");
				}
				else if( w[0] == '(')
				{
					token.push_back("(");
					if(w.length() > 1)
						token.push_back(w.substr(1,w.length()-1));
				}
				else if(w[w.length() - 1] == ')')
				{
					if(w.length()>1)
						token.push_back(w.substr(0,w.length()-1));
					token.push_back(")");
				}
				else
				{
					token.push_back(w);
				}
			}
		}
		cin >> n;
		string name;
		int a;
		set<string> cha;
		for(int i = 0; i< n; ++i)
		{
			cin >> name;
			cin >> a;
			cha.clear();
			for(int j = 0; j< a; ++j)
			{
				cin >> name;
				cha.insert(name);
			}
			double possible = getans(1.0,token,cha);
			printf("%.7lf\n",possible);
		}
	}
	return 0;
}