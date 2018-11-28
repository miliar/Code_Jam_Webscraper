#include <map>
#include <string>
#include <cstdio>
#include <iostream>
#include <sstream>
#include <fstream>
#include <boost/format.hpp>
#include <list>
#include <set>

struct Node
{
	typedef std::map<char, Node> tree_t;
	Node() : c(0) {};
	Node(char c) : c(c) {};
	tree_t more;
	char c;
};

typedef std::vector<std::set<char> > charmap_t;

void add_word(Node & root, const std::string & str)
{
	Node * cur = &root;
	for(std::string::const_iterator i = str.begin(); i != str.end(); ++i)
	{

		Node::tree_t::iterator next = cur->more.find(*i);

		if(next == cur->more.end())
		{
			// No words with this next character, make a new node
			cur->more.insert(std::make_pair(*i, Node(*i)));
			next = cur->more.find(*i);
		}

		cur = &next->second;
	}
}

bool is_word(Node & root, const std::string & str)
{
	Node * cur = &root;
	for(std::string::const_iterator i = str.begin(); i != str.end(); ++i)
	{
		Node::tree_t::iterator next = cur->more.find(*i);

		if(next == cur->more.end())
		{
			return false;
		}

		cur = &next->second;
	}
	return true;
}


typedef std::list<std::list<char> > outer_t;
typedef outer_t::value_type inner_t;

outer_t::iterator next_block(outer_t & l)
{
	l.push_back(inner_t());

	return --l.end();
}

int descend_words(const Node::tree_t & cur_node, const outer_t & parse_word, outer_t::const_iterator cur_place)
{
	if(cur_place == parse_word.end())
	{
		return 1;
	}
	int acc = 0;
	for(inner_t::const_iterator i = cur_place->begin(); i != cur_place->end(); ++i)
	{
		Node::tree_t::const_iterator next_node = cur_node.find(*i);
		if(next_node == cur_node.end())
		{
			continue;
		}
		outer_t::const_iterator next_place = cur_place;

		acc += descend_words(next_node->second.more, parse_word, ++next_place);
	}
	return acc;
}

int count_words(const Node::tree_t & root_node, const std::string & str)
{
	outer_t parse_word;

	outer_t::iterator place = next_block(parse_word);

	bool in_paren = false;

	for(std::string::const_iterator i = str.begin(); i != str.end(); ++i)
	{
		if(in_paren)
		{
			if(*i == ')')
			{
				in_paren = false;
				place = next_block(parse_word);
			}
			else
			{
				place->push_back(*i);
			}
		}
		else
		{
			if(*i == '(')
			{
				in_paren = true;
			}
			else
			{
				place->push_back(*i);
				place = next_block(parse_word);
			}
		}
	}

	if(parse_word.back().empty())
	{
		parse_word.pop_back();
	}

	return descend_words(root_node, parse_word, parse_word.begin());
}

int main(int argc, char * argv[])
{
	std::ofstream file("log.txt");

	std::string line;
	std::stringstream buf;

	std::getline(std::cin, line);
	buf.str(line);

	int L, D, N;

	buf >> L >> D >> N;

	Node root;

	for(int i = 0; i < D; ++i)
	{
		std::getline(std::cin, line);
		add_word(root, line);
	}


	for(int i = 0; i < N; ++i)
	{
		std::getline(std::cin, line);
		buf.str("");
		buf.clear();
		buf << boost::format("Case #%1%: %2%\n") % int(i+1) % count_words(root.more, line);
		std::cout << buf.str();
		file << buf.str();

	}


}
