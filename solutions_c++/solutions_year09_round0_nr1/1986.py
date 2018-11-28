#include <iostream>
#include <string>
#include <iterator>

using namespace std;

#define rep(i,n) for(int i=0; i<(n); ++i)

class Node {
	public:
		Node *childs[26];
		Node()
		{
			rep(i,26) childs[i]=NULL;
		}
		~Node()
		{
			rep(i,26) if (childs[i]!=NULL) delete(childs[i]);
		}
		Node *add(char c)
		{
			Node* node = new Node();
			childs[c-'a']=node;
			return node;
		}
		Node *get(char c)
		{
			return childs[c-'a'];
		}
		Node *getOrAdd(char c)
		{
			if (childs[c-'a'] == NULL) return add(c);
			return childs[c-'a'];
		}
};

int L, D, N;
string word;
string pword;
int K;
Node header;
Node *aNode;

void dfs(int pos, Node* n)
{
	if (pos >= pword.size())
	{
		++K;
		return;
	}
	if (pword[pos]=='(')
	{
		int endpos = pword.find(')',pos+1);
		for (int p=pos+1; p<endpos; ++p)
		{
			if(n->get(pword[p])!=NULL)
				dfs(endpos+1, n->get(pword[p]));
		}
	}
	else
	{
		if(n->get(pword[pos])!=NULL)
		{
			dfs(pos+1,n->get(pword[pos]));
		}
	}
}

int main()
{

	cin >> L >> D >> N;
	
	rep(i, D)
	{
		cin >> word;
		Node* n = &header;
		for(string::iterator iter = word.begin(); iter!=word.end(); ++iter)
		{
			char c = (*iter);
			n = n->getOrAdd(c);
		}
	}
	
	rep(i, N)
	{
		K = 0;
		
		cin >> pword;
		dfs(0, &header);
		
		cout << "Case #" << (i+1) << ": " << K << endl;
	}

}
