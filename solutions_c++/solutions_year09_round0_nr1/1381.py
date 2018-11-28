#include <cstdio>
#include <string>
#include <vector>
#include <iostream>

using namespace std;

int ncases, nwords, tokencounter, matches, len;
string pattern;
vector<string> tokens;
vector<string> words;

void parsepattern()
{
	int sz=pattern.size();
	for(int i=0; i<sz; i++, tokencounter++)
	{
		if(pattern[i]!='(')
		{
			tokens.push_back(string());
			tokens[tokencounter].push_back(pattern[i]);
		}
		
		else
		{
			tokens.push_back(string());
			while(pattern[++i]!=')')
				tokens[tokencounter].push_back(pattern[i]);
		}
	}
}

bool matchespattern(string s)
{
	bool stop=false;
	int sz=s.size();
	for(int i=0; i<sz && !stop; i++)
	{
		stop=true;
		for(unsigned int j=0; j<tokens[i].size(); j++)
			if(s[i]==tokens[i][j])
			{
				stop=false;
				break;
			}
	}
	return !stop;
}

int main()
{
	scanf("%d %d %d", &len, &nwords, &ncases);
	
	for(int i=0; i<nwords; i++)
	{
		string temp;
		cin >> temp;
		words.push_back(temp);
	}
	
	for(int i=0; i<ncases; i++)
	{
		matches=0;
		tokencounter=0;
		tokens.clear();
		pattern.clear();
		cin >> pattern;
		
		parsepattern();
		
		for(int j=0; j<nwords; j++)
			if(matchespattern(words[j]))
				matches++;

		printf("Case #%d: %d\n", i+1, matches);
	}
	return 0;
}
