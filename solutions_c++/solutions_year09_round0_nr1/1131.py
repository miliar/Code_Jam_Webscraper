#include <iostream>
#include <vector>
#include <functional>
#include <algorithm>
#include <set>
#include <string>

using namespace std;
struct Node;
struct CompareNode
{
  bool operator()(const Node* s1, const Node* s2) const;
};

typedef std::set<Node*, CompareNode> TreeChildren;
struct Node
{
	Node(char letter):_letter(letter){}
	~Node(){ Cleanup(); }
	void Cleanup(){ std::for_each( _children.begin(), _children.end(), std::mem_fun(&Node::Cleanup));}
	char _letter;
	TreeChildren _children;
};
bool CompareNode::operator()(const Node* s1, const Node* s2) const
{
	return (s1->_letter < s2->_letter);
}

void Add(Node *root, char letter)
{
	root->_children.insert( new Node(letter) );
}

void AddChain(Node *root, const char *str, int index)
{
	for(;str[index]; ++index)
	{
		Node *me = new Node(str[index]);
		root->_children.insert(me);
		root = me;
	}
}

void Add(Node *root, const char *str, int index)
{
	if (str[index] == 0) return;
	Node node(str[index]);
	TreeChildren::iterator ii = root->_children.find( &node );
	if (ii == root->_children.end())
		AddChain(root, str, index);
	else
		Add(*ii, str, ++index);
}

int MatchCount(Node *root, const char *str, int index)
{
	if (str[index] == 0 && root->_children.size() == 0) return 1;
	if (str[index] == 0 || root->_children.size() == 0) return 0;

	int startIndex = index;
	int endIndex = index+1;
	if (str[index] == '(')
	{
		++startIndex;
		while(str[endIndex++] != ')');
	}
	Node node(0);
	int count = 0;
	for(;startIndex < endIndex; ++startIndex)
	{
		node._letter = str[ startIndex ];
		TreeChildren::iterator ii = root->_children.find( &node );
		if (ii == root->_children.end()) continue;
		count += MatchCount(*ii, str, endIndex);
	}
	return count;
}

int main()
{
	Node root(0);
	int L, D, N;
	std::cin >> L >> D >> N;
	std::string str;
	std::getline( std::cin, str);
	for (int i=0; i < D; ++i)
	{
		std::string str;
		std::getline( std::cin, str);
		Add(&root, str.c_str(), 0);
	}

	std::vector<std::string> strs;
	for (int j=0; j < N; ++j)
	{
		std::string str;
		std::getline( std::cin, str);
		strs.push_back(str);
	}
	for (size_t i=0; i < strs.size(); ++i)
		std::cout<< "Case #"<< i+1 << ": "<< MatchCount(&root, strs[i].c_str(), 0) << std::endl;

	return 0;
}

