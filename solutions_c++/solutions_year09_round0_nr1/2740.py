#include <string>
#include <list>
#include <iostream>

using std::cin;
using std::cout;
using std::endl;

using std::string;

class Letter
{
public:
	Letter(string new_letters)
	{
		for(int i = 0; i < new_letters.size(); i++)
		{
			letters.push_back(new_letters.at(i));
		}
		letters.sort();
		reset();
	}
	Letter(const Letter &old)
	{
		for(std::list<char>::const_iterator iter = old.letters.begin();
			iter != old.letters.end(); iter++)
		{
			letters.push_back(*iter);
		}
		l_iter = letters.begin();
		option = 0;
	}
	Letter(char new_letter)
	{
		letters.push_back(new_letter);
		reset();
	}
	char getCurrent()
	{
		return *l_iter;
	}
	void advance()
	{
		l_iter++;
		option++;
	}
	bool hasMore()
	{
		return (option != letters.size()-1);
	}
	void reset()
	{
		option = 0;
		l_iter = letters.begin();
	}
	int option;
	std::list<char>::iterator l_iter;
	std::list<char> letters;
};

class Word
{
public:
	Word(string new_letters)
	{
		for(int i = 0; i < new_letters.size(); i++)
		{
			if(new_letters.at(i) != '(') 
				letter_combos.push_back(new Letter(new_letters.at(i)));
			else
			{
				int j = 1;
				while(new_letters.at(i+j) != ')') j++;
				string temp = new_letters.substr(i+1, j-1);
				letter_combos.push_back(new Letter(temp));
				//letter_combos.end()->reset();
				i += j;
			}
		}
		length = 1;
		big_letter = letter_combos.begin();
		at_length = letter_combos.begin();
	}
	string getPartialWord()
	{
		string temp = string(length,' ');
		int filled = 0;
		big_letter = letter_combos.begin();
		while(filled < length)
		{
			temp.at(filled) = (*big_letter)->getCurrent();
			filled++;
			big_letter++;
		}
		return temp;
	}
	void increaseLength()
	{
		length++;
		at_length++;
	}
	void nextOption()
	{
		while((*at_length)->hasMore()==false)
		{
			(*at_length)->reset();
			length--;
			at_length--;
		}
		(*at_length)->advance();
	}
	bool hasOptions()
	{
		std::list<Letter*>::iterator at_length_plus = at_length;
		at_length_plus++;
		for(std::list<Letter*>::iterator iter = letter_combos.begin();
			iter != at_length_plus; iter++)
		{
			if((*iter)->hasMore()) return true;
		}
		return false;
	}
	int length;
	std::list<Letter*>::iterator at_length;
	std::list<Letter*>::iterator big_letter;
	std::list<Letter*> letter_combos;
};

class Dictionary
{
public:
	Dictionary(){};
	void addWord(string new_word)
	{
		words.push_back(new_word);
	}
	void sort()
	{
		words.sort();
	}
	std::list<string>::iterator find(std::list<string>::iterator start, string target)
	{
		while(start != words.end())
		{
			string temp = start->substr(0,target.size());
			if(temp == target) return start;
			else if(temp > target) return words.end();
			else start++;
		}
		return words.end();
	}
	std::list<string> words;
};

int main(char ** argv, int argc)
{
	int letter_limit, num_words, cases;
	Dictionary dictionary;
	std::list<Word*> words;

	cin >> letter_limit;
	
	
	cin >> num_words;
	cin >> cases;

	for(int i = 0; i<num_words; i++)
	{
		string temp;
		cin >> temp;
		dictionary.addWord(temp);
	}
	dictionary.sort();

	for(int i = 0; i<cases; i++)
	{
		string temp;
		cin >> temp;
		words.push_back(new Word(temp));
	}

	////set letter limit
	//int letter_limit = 3;
	////fill dictionary
	//Dictionary dictionary;
	//dictionary.addWord("abc");
	//dictionary.addWord("bca");
	//dictionary.addWord("dac");
	//dictionary.addWord("dbc");
	//dictionary.addWord("cba");
	//dictionary.sort();
	////fill word set
	//std::list<Word*> words;
	//words.push_back(new Word("(ab)(bc)(ca)"));
	//words.push_back(new Word("abc"));
	//words.push_back(new Word("(abc)(abc)(abc)"));
	//words.push_back(new Word("(zyx)bc"));
	//check words!
	std::list<int> possibilities;
	std::list<string>::iterator match;
	for(std::list<Word*>::iterator iter = words.begin();
		iter != words.end(); iter++)
	{
		int matches = 0;
		//check the word, letter by letter, against the dictionary
		while(1)
		{
			//if the length is one, then we are just starting, must search from 
			//  the beginning
			string partial = (*iter)->getPartialWord();
			if((*iter)->length == 1)
				match = dictionary.find(dictionary.words.begin(),partial);
			//otherwise, we're working on it
			else
				match = dictionary.find(match,partial);

			//if there is no match
			if(match == dictionary.words.end())
			{
				//if there are options, go to the next one
				if((*iter)->hasOptions()) 
				{
					(*iter)->nextOption();
					match = dictionary.words.begin();
				}
				//if no match and no option, move on to the next word
				else 
				{
					possibilities.push_back(matches);				
					break;
				}
			}
			//if there is a match, then increase the length or change option
			else
			{
				//if the word is already at max length, add one to the matches
				if((*iter)->length == letter_limit)
				{
					matches++;
					//if there are options, go to the next one
					if((*iter)->hasOptions())
					{
						(*iter)->nextOption();
						match++;
					}
					else
					{
						possibilities.push_back(matches);
						break;
					}
				}
				else (*iter)->increaseLength();
			}
		}
	}
	int index = 0;
	for(std::list<int>::iterator iter = possibilities.begin();
		iter != possibilities.end(); iter++)
	{
		index++;
		cout << "Case #" << index << ": " << *iter << endl;
	}
	return 0;
}