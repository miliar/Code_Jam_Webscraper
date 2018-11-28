#include <iostream>
#include <fstream>
#include <string>
using namespace std;

ifstream fin("Alien Language.txt");
#define cin fin

ofstream fout("Alien Language out.txt");
#define cout fout

class Trie
{
public:
	Trie()
	{
		long long  i;
		for(i=0; i<26; i++)
		{
			children[i] = NULL;
		}
		word = 0;
	}
	Trie* children[26];
	bool word;
};

void AddToTrie(Trie* t, string s);
long long  SearchTrie(Trie* t, string s, long long  ind);
void DeleteTrie(Trie* t);

int  main()
{
	Trie * t = new Trie;
	string s;
	long long  L, D, N, i = 1;
	cin>>L>>D>>N;
	while(D)
	{
		cin>>s;
		AddToTrie(t, s);
		D--;
	}
	while(N)
	{
		cin>>s;
		long long  a = SearchTrie(t, s, 0);
		cout<<"Case #"<<i++<<": "<<a<<endl;
		N--;
	}
	return 0;
}

void AddToTrie(Trie* t, string s)
{
	long long  i, j;
	for(i=0; i<s.size();  i++)
	{
		j = (long long )(s[i] - 'a');
		if(t->children[j] == NULL)
			t->children[j] = new Trie;
		t = t->children[j];
	}
	t->word = 1;
}
long long  SearchTrie(Trie* t, string s, long long  ind)
{
	if(ind == s.size())
		return t->word;
	long long  i, j, k;
	if(s[ind] == '(')
	{
		long long  ret = 0;
		for(i=ind+1; ; i++)
		{
			if(s[i] == ')')
			{
				k = i;
				break;
			}
		}
		for(i=ind+1; i<k; i++)
		{
			j = (long long )(s[i] - 'a');
			if(t->children[j] != NULL)
				ret += SearchTrie(t->children[j], s, k+1);
		}
		return ret;
	}
	else
	{
		j = (long long )(s[ind] - 'a');
		if(t->children[j] == NULL)
			return 0;
		return SearchTrie(t->children[j], s, ind+1);
	}
}
void DeleteTrie(Trie* t)
{
	long long  i;
	for(i=0; i<26; i++)
	{
		if(t->children[i] != NULL)
			DeleteTrie(t->children[i]);
	}
	delete t;
}