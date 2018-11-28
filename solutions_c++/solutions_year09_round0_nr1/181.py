#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int L, D, N;

struct letter
{
	letter *ptr[26];
	letter(){for(int i=0; i<26; i++) ptr[i] = NULL;}
	~letter(){for(int i=0; i<26; i++)	if(ptr[i] != NULL)	delete ptr[i];}
};

string gow;

int go(int index, int depth, letter* pos)
{
	if(gow[index] == '(')
	{
		int end=index+1, total=0;
		for(;gow[end]!=')'; end++);
		for(int i=index+1; i<end; i++)	if(pos->ptr[gow[i]-'a'] != NULL)
		{
			if(depth == L-1)	total++;
			else total += go(end+1, depth+1, pos->ptr[gow[i]-'a']);
		}
		return total;
	}
	else 
	{
		if(pos->ptr[gow[index]-'a'] != NULL)
		{
			if(depth < L-1)
				return go(index+1, depth+1, pos->ptr[gow[index]-'a']);
			else return 1;
		}
		return 0;
	}
}

int main()
{
	ifstream fin("A-small-attempt0.in");
	ofstream fout("A-out.txt");
	
	fin>>L>>D>>N;
	string word;
	letter * trie = new letter();
	
	
	for(int i=0; i<D; i++)
	{
		fin>>word;
		letter * current = trie;
		for(int j=0; j<L; j++)
		{
			if(current->ptr[word[j]-'a'] == NULL)	current->ptr[word[j]-'a'] = new letter();
			current = current->ptr[word[j]-'a'];
		}
	}
	
	
	for(int i=0; i<N; i++)
	{
		fin>>gow;
		fout<<"Case #"<<i+1<<": "<<go(0,0,trie)<<"\n";
	}
	
	return 0;
}
