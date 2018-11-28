#include <iostream>
#include <fstream>
#include <string>
#include <cstring>

using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

struct Node
{
	Node *Children[26];

	Node()
	{
		memset(Children, 0, sizeof(Children));
	}
};

Node *root;
int L, D, N;
int sum;

void AddWord(Node *current, string word, int position)
{
	if(position == word.size())
	{
		return;
	}

	int index = word[position] - 'a';
	if(current->Children[index] == NULL)
	{
		current->Children[index] = new Node();
	}

	AddWord(current->Children[index], word, position + 1);
}

void MatchPattern(Node *current, string pattern, int position, int length)
{
	if(length == L)
	{
		++sum;
		return;
	}

	int index;
	if(pattern[position] == '(')
	{
		int end = position + 1;
		while(end < pattern.size() && pattern[end] != ')')
		{
			++end;
		}

		for(int i = position + 1; i < end; ++i)
		{
			index = pattern[i] - 'a';
			if(current->Children[index] != NULL)
			{
				MatchPattern(current->Children[index], pattern, end + 1, length + 1);
			}
		}
	}
	else
	{
		index = pattern[position] - 'a';
		if(current->Children[index] != NULL)
		{
			MatchPattern(current->Children[index], pattern, position + 1, length + 1);
		}
	}
}

int Match(string pattern)
{
	sum = 0;

	MatchPattern(root, pattern, 0, 0);

	return sum;
}

int main()
{
	fin >> L >> D >> N;

	root = new Node();
	string str;
	for(int i = 0; i < D; ++i)
	{
		fin >> str;
		AddWord(root, str, 0);
	}

	int cnt = 0;
	while(cnt < N)
	{
		fin >> str;
		int matches = Match(str);
		fout << "Case #" << cnt + 1 << ": " << matches << endl;
		++cnt;
	}

	return 0;
}