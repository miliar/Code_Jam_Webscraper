// qualification.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <string>
#include <map>
#include <list>
#include <vector>

#include <algorithm>

std::list<std::string> words;

class WordTree
{
private:
	std::map<char, WordTree>	subTree;
public:
	typedef std::map<char, WordTree>::iterator	iterator;

	WordTree& operator[]( char c ) { return subTree[c]; }
	iterator find( char c ) { return subTree.find(c); }
	iterator end() { return subTree.end(); }
};

typedef std::vector<std::string>	WordSearch;

WordTree	wordTree;

void InsertWord( const std::string& word, WordTree& wordLeaf = wordTree, unsigned short index = 0 )
{
	WordTree* leaf = &wordLeaf;
	while ( index < word.length() )
		leaf = &(*leaf)[word[index++]];
}

/*
unsigned int CheckWord( WordSearch& wordSearch, WordTree& leaf = wordTree )
{
	if ( wordSearch.empty() ) return 0;

	std::string cases = wordSearch.front();
	wordSearch.pop_front();

	int count = 0;
	std::string::iterator cit;
	for ( cit = cases.begin(); cit != cases.end(); cit++ )
	{
		WordTree::iterator wit;
		if ( ( wit = leaf.find( *cit ) ) != leaf.end() )
		{
			if ( wordSearch.size() == 0 )
				count++;
			else
				count += CheckWord( wordSearch, wit->second );
		}
	}

	return count;
}
*/
class RemPred
{
private:
	std::string chars_;
	short point_;
public:
	RemPred(std::string chars, short point): chars_(chars), point_(point) {}
	bool operator()( const std::string& str )
	{
		for ( short i = 0; i < chars_.size(); i++ )
			if ( str[point_] == chars_[i] ) return false;
		return true;
	}
};

unsigned int CheckWord2( WordSearch& wordSearch )
{
	std::list<std::string> words2(words);
	
	for (short i = 0; i < wordSearch.size(); i++)
		words2.erase( std::remove_if( words2.begin(), words2.end(), RemPred(wordSearch[i], i) ), words2.end() );

	return words2.size();
}

WordSearch CreateWordSearch( const std::string& regexp )
{
	WordSearch wordSearch;
	std::string	characters = "";
	bool isSet = false;
	for( unsigned short i = 0; i < regexp.length(); i++ )
	{
		switch(regexp[i])
		{
		case '(':
			isSet = true;
			characters = "";
			break;
		case ')':
			isSet = false;
			wordSearch.push_back( characters );
			break;
		default:
			if ( isSet )
			{
				if ( characters.find(regexp[i]) == -1 )
					characters += regexp[i];
			}
			else
				wordSearch.push_back( characters = regexp[i] );
		}
	}
	return wordSearch;
}

int _tmain(int argc, _TCHAR* argv[])
{
	unsigned int wordLength, wordsCount, inputCount;

	std::cin >> wordLength >> wordsCount >> inputCount;

	std::string word;
	for ( unsigned int i = 0; i < wordsCount; i++ )
	{
		std::cin >> word;
		if ( word.length() == wordLength )
		{
			InsertWord(word);
			words.push_back(word);
		}
	}

	for ( unsigned int i = 1; i <= inputCount; i++ )
	{
		std::cin >> word;
//		std::cout << "Case #" << i << ": " << CheckWord(CreateWordSearch(word)) << std::endl;
		std::cout << "Case #" << i << ": " << CheckWord2(CreateWordSearch(word)) << std::endl;
	}

	return 0;
}
