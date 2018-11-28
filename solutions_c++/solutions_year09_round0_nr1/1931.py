#include <iostream>
#include <vector>
#include <cassert>

using namespace std;
const int LEN_MAX = 1024;
const int LETTERS_NUM = 30;

int len, numWords, numPatterns;

struct Node
{
	int isEnd;
	int seenOnStep;

	Node * nodes[LETTERS_NUM];
	
	Node(int the_isEnd=0)
		:isEnd(the_isEnd),seenOnStep(0)
	{
		memset( nodes,0,sizeof(nodes) );
	}
	~Node()
	{
		for(int i=0; i<LETTERS_NUM; i++)
		{
			if( nodes[i] )
			{
				delete nodes[i];
				nodes[i] = 0;
			}
		}
	}

	void dfsMark(int depth, vector<int> &idLetters, int step)
	{
		if( depth==0 )
		{
			seenOnStep = step;
			return;
		}
		if( step != seenOnStep ) return;

		if( depth==1 )	// then mark by current letters
		{
			for(int i=0; i<(int)idLetters.size(); i++)
			{
				int id = idLetters[i];
				if( nodes[id] )
				{
					nodes[id]->dfsMark(depth-1,idLetters,step);
				}
			}
			return;
		}

		// go depth
		for(int i=0; i<LETTERS_NUM; i++)
		{
			if( nodes[i] )
			{
				nodes[i]->dfsMark(depth-1,idLetters,step);
			}
		}
	}

	int dfsSum(int step)
	{
		if( step != seenOnStep ) return 0;
		int sum = isEnd;
		for(int i=0; i<LETTERS_NUM; i++)
		{
			if( nodes[i] )
			{
				sum += nodes[i]->dfsSum(step);
			}
		}
		return sum;
	}

	void dfsPrint(int depth, char letter)
	{
		for(int i=0; i<depth; i++)
		{
			cout << " ";
		}
		cout << letter;
		if( isEnd )
			cout << isEnd;
		if( seenOnStep )
			cout << "(" << seenOnStep << ")";

		cout << endl;
		for(int i=0; i<LETTERS_NUM; i++)
		{
			if( nodes[i] )
			{
				nodes[i]->dfsPrint(depth+1, 'a'+i);
			}
		}
	}
};

class Trie
{
	Node root;

public:
	void pushWord( const char *word )
	{
		Node *curNode = &root;
		const char *curLetter = word;

		while( *curLetter )
		{
			int idCurLetter = *curLetter-'a';
			if( !curNode->nodes[idCurLetter] )
			{
				curNode->nodes[idCurLetter] = new Node();
			}
			++curLetter;
			curNode = curNode->nodes[idCurLetter];
		}

		curNode->isEnd++;
	}

	int calcMatches( const char *pattern, int step )
	{
		const char *curPos = pattern;
		int idPatternPos = 0;
		root.seenOnStep = step;
		while( idPatternPos<len )
		{
			// prepare vector of letters
			vector<int> idLetters;
			if( *curPos=='(' )
			{
				curPos++;
				while( *curPos!=')' && *curPos )
				{
					idLetters.push_back( *curPos-'a' );
					curPos++;
				}
				curPos++;
			}
			else
			{
				idLetters.push_back( *curPos-'a' );
				curPos++;
			}

			// make dfs stepping deeper on current depth
			root.dfsMark(idPatternPos+1, idLetters, step);

			idPatternPos++;
		}
		assert( *curPos==0 && pattern+strlen(pattern)==curPos );

		return root.dfsSum(step);
	}

	void print()
	{
		root.dfsPrint(0,'+');
	}
};


Trie trie;


void input()
{
	cin >> len >> numWords >> numPatterns;

	char word[LEN_MAX];
	for(int i=0; i<numWords; i++)
	{
		cin >> word;
		assert( strlen(word)==len );
		trie.pushWord( word );
	}
}

void solve()
{
	char pattern[LEN_MAX];
	for(int step=1; step<=numPatterns; step++)
	{
		cin >> pattern;
		int result = trie.calcMatches(pattern, step);
		//trie.print();
		cout << "Case #"<< step <<": "<< result << endl;
	}
}

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	input();	
	solve();
	return 0;
}

