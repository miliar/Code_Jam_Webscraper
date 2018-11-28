#include <iostream>
#include <string>
#include <set>

using namespace std;

struct node
{
	int words;
	node** edges;
};

class Trie
{
	private:
		node* root;
		void init( node* n )
		{
			n->words = 0;
			n->edges = new node*[26];
		}
		
		void deleteNode( node* n )
		{
			for (int i = 0; i < 26; ++i)
				if (n->edges[i])
					deleteNode(n->edges[i]);
			delete n;
		}
		
		void addWord( node* n, string word )
		{
			if (word.length() <= 0)
				(n->words)++;			
			else
			{
				int c = word[0] - 'a';
				if ( !(n->edges[c]) )
				{
					node* child = new node;
					init(child);
					n->edges[c] = child;
				}
				addWord( n->edges[c], word.substr(1) );				
			}		
		}
		
		int count( node* n, string word )
		{
			if (word.length() == 0)
				return n->words;
			int c = word[0] - 'a';
			if (!n->edges[c])
				return 0;
			return count(n->edges[c], word.substr(1));
		}
		
		bool prefix( node* n, string pre )
		{
			if (pre.length() == 0)
				return true;
			int c = pre[0] - 'a';
			if (!n->edges[c])
				return false;
			return prefix(n->edges[c], pre.substr(1));
		}
		
	public:
		Trie()
		{
			root = new node;
			init(root);
		}
		
		~Trie()
		{
			deleteNode(root);
		}
		
		bool prefix( string pre )
		{
			return prefix(root,pre);
		}
		
		int count( string word )
		{
			return count(root,word);
		}
		
		void addWord( string word )
		{			
			addWord(root,word);
		}
			
};

int main()
{
	
	int L,D,N;
	cin >> L >> D >> N;
	Trie t;
	for (int i = 0; i < D; ++i)
	{
		string s;
		cin >> s;
		t.addWord(s);
	}
	for (int i = 0; i < N; ++i)
	{
		string s;
		cin >> s;
		set<string> words;
		bool first = true;
		for (int j = 0; j < s.length(); ++j)
		{
			char c = s[j];
			bool emp = words.size() == 0;			
			if (!first && emp)
				break;
			string toAdd = "";
			if (c == '(')
			{							
				while (++j < s.length() && s[j] != ')')
					toAdd += s[j];				
			}
			else
				toAdd += c;
			
			set<string> nextWords;
			for (int k = 0; k < toAdd.length(); ++k)
			{
				if (emp) 
				{				
					string a = "";
					a += toAdd[k];
					if (t.prefix(a))
						nextWords.insert(a);	
				}								
				else
				{
					set<string>::iterator itr = words.begin();
					for (; itr != words.end(); ++itr)
					{
						string a = *itr;
						string b = a + toAdd[k];
						if (t.prefix(b))
							nextWords.insert(b);
					}
				}
			} 								
			first = false;
			words.clear();
			for (set<string>::iterator itr = nextWords.begin(); itr != nextWords.end(); ++itr)
				words.insert(*itr);
		}				
		cout << "Case #" << (i+1) << ": " << words.size() << endl;
	}
	return 0;
}
