#pragma once

#include <list>
#include <boost/unordered_map.hpp>

typedef unsigned char element;

class TestCase {
	static bool elementMap[256];
	static bool inited;

	static void init();

	typedef boost::unordered_map<std::string, element> CombineMap;
	CombineMap combines;

	typedef std::list<element> OppositeList;
	OppositeList opposites[256];

	std::string combine(element e1, element e2);
	void updateOppositeMap(bool *map, element el, bool remove);

public:
	typedef std::list<element> Output;

	TestCase();
	~TestCase();

	void addCombine(element base1, element base2, element combined);
	void addOpposite(element base1, element base2);
	
	void solve(const std::string& input, Output& output);

};
