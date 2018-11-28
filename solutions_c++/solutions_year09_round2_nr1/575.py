#include <iostream>
#include <fstream>
#include <sstream>
#include <boost/format.hpp>
#include <boost/lexical_cast.hpp>
#include <map>
#include <list>
#include <string>
#include <stack>
#include <set>
#include <vector>
#include "matrix.h"
#include <algorithm>

struct Node
{
	Node() : name(""), left(NULL), right(NULL)
	{

	}
	double weight;
	std::string name;
	Node *left, *right;
};

size_t parse_tree(std::list<Node> & nodes, Node * root, std::stringstream &buf,
				const std::string & tree, size_t pos, const std::map<size_t, size_t> & paren_pairs)
{
	;
	size_t i = tree.find_first_of('(',pos);

	size_t end_paren = paren_pairs.find(i)->second;
	std::string myelem = tree.substr(i+1, end_paren-i-1);

	buf.clear();
	buf.str(myelem);

	buf >> root->weight;

	std::string temp;

	buf >> temp;

	if(buf)
	{
		root->name = temp;

		nodes.push_back(Node());
		root->left = &nodes.back();
		nodes.push_back(Node());
		root->right = &nodes.back();
		i = parse_tree(nodes, root->left, buf, tree, i+1, paren_pairs);
		i = parse_tree(nodes, root->right, buf, tree, i+1, paren_pairs);				
	}
	else
	{
		i = end_paren;
	}

	return i;
}

double descend_tree(Node * root, const std::set<std::string> & traits)
{
	double val = 1;
	while(root)
	{
		val *= root->weight;
		if(traits.find(root->name) != traits.end())
		{
			root = root->left;
		}
		else
		{
			root = root->right;
		}
	}

	return val;
}


int main(int argc, char *argv[])
{
	std::ofstream file("log.txt");

	std::string line;

	std::getline(std::cin, line);

	int N = boost::lexical_cast<int>(line);

	std::stringstream buf;

	for(int i = 0; i < N; ++i)
	{
		std::getline(std::cin, line);

		int L = boost::lexical_cast<int>(line);

		buf.clear();
		buf.str("");

		for(int j = 0; j < L; ++j)
		{
			std::getline(std::cin, line);
			buf << line;
		}

		std::string tree = buf.str();

		std::deque<size_t> paren_loc;
		std::map<size_t,size_t> paren_locf;

		for(size_t j = 0; j < tree.size(); ++j)
		{
			if(tree[j] == '(')
			{
				paren_loc.push_back(j);
			}
			if(tree[j] == ')')
			{
				paren_locf.insert(std::make_pair(paren_loc.back(), j));
				paren_loc.pop_back();
			}
		}

		std::list<Node> treemem;
		treemem.push_back(Node());

		Node * root = &treemem.back();
		parse_tree(treemem, root, buf, tree, 0, paren_locf);

		std::getline(std::cin, line);

		int A = boost::lexical_cast<int>(line);

		std::list<std::string> animals;

		buf.clear();
		buf.str("");
		buf << boost::format("Case #%d:\n") % int(i+1);
		
		std::cout << buf.str();
		file << buf.str();

		for(int j = 0; j < A; ++j)
		{
			std::getline(std::cin, line);

			buf.clear();
			buf.str(line);

			std::string name;
			std::string temp;
			int Ntr;
			std::set<std::string> traits;

			buf >> name >> Ntr;

			for(int k = 0; k < Ntr; ++k)
			{
				buf >> temp;
				traits.insert(temp);
			}

			double ans = descend_tree(root, traits);

			buf.clear();
			buf.str("");
			buf << boost::format("%.7f\n") % ans;

			std::cout << buf.str();
			file << buf.str();
		}
	}
}