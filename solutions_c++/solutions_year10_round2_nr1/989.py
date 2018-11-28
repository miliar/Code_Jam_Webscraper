#include <iostream>
#include <fstream>
#include <map>
#include <boost/format.hpp>
#include <vector>
#include <boost/algorithm/string.hpp>
#include <cassert>

typedef std::vector<std::string> PathList;

struct Node
{
	typedef std::map<std::string, Node> NodeMap;
	NodeMap subnodes;

	std::pair<Node *, PathList::const_iterator> find_path(PathList::const_iterator itr, PathList::const_iterator end)
	{
		if(itr == end)
		{
			return std::make_pair(this, itr);
		}

		NodeMap::iterator litr = subnodes.find(*itr);

		if(litr == subnodes.end())
		{
			return std::make_pair(this, itr);
		}

		return litr->second.find_path(++itr, end);
	}

	int add_path(const std::string & str)
	{
		PathList list;

		boost::split(list, str, boost::is_any_of("/"));

		return add_path_recurse(++list.begin(), list.end());
	}
private:
	int add_path_recurse(PathList::const_iterator itr, PathList::const_iterator end)
	{
		std::pair<Node*, PathList::const_iterator> p = find_path(itr, end);

		if(p.second == end)
		{
			return 0;
		}

		if(p.first != this)
		{
			return p.first->add_path_recurse(p.second, end);
		}

		std::pair<NodeMap::iterator, bool> ret = subnodes.insert(std::make_pair(*itr, Node()));

		assert(ret.second);
		if(++itr == end)
		{
			return 1;
		}
		else
		{
			return 1+ret.first->second.add_path_recurse(itr, end);
		}
	}
};


int main(int argc, char *argv[])
{
	int T;

	std::cin >> T;

	for(int t = 0; t < T; ++t)
	{
		int N, M;
		std::cin >> N >> M;
		std::cin.ignore(80, '\n');

		Node root;

		if(M == 0)
		{
			std::cout << boost::format("Case #%d: 0\n") % (t+1);
			continue;
		}

		std::string str;
		for(int i = 0; i < N; i++)
		{
			std::getline(std::cin, str);
			root.add_path(str);
		}

		int count = 0;

		for(int i = 0; i < M; i++)
		{
			std::getline(std::cin, str);
			count += root.add_path(str);
		}

		std::cout << boost::format("Case #%d: %d\n") % (t+1) % count;
	}
}
