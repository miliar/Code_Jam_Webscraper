#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <iterator>
#include <numeric>
#include <set>
#include <cmath>
#include <iomanip>

#include <boost/lexical_cast.hpp>

//const std::string setName = "A-test";
//const std::string setName = "A-small-practice";
//const std::string setName = "A-small-attempt0";
//const std::string setName = "A-small-attempt1";
const std::string setName = "A-large";
//const std::string setName = "A-large-practice";

class DTree
{
public:
	class Node
	{
	public:
		Node() : weight(0), attrib(""), first(0), second(0) {}
		Node(const Node & n) : weight(n.weight), attrib(n.attrib), first(n.first), second(n.second) {}
		Node & operator=(const Node & n)
		{
			weight = n.weight;
			attrib = n.attrib;
			first = n.first;
			second = n.second;
			return *this;
		}
		double weight;
		std::string attrib;
		Node * first;
		Node * second;
		
		void print() const
		{
			std::cout << "(" << weight;
			if(attrib!="")
			{
				std::cout << " " << attrib << "\n";
				first->print();
				second->print();
			}
			std::cout << ")\n";
		}
	};
	
	DTree(std::istream & is)
		: root(parse(is))
	{}
		
	Node * parse(std::istream & is)
	{
		Node * node = new Node();
		is >> std::ws;
		if(is.get() != '(')
			std::cout << "crap" << std::endl;
		is >> node->weight;
		
		is >> std::ws;
		if(is.peek() != ')')
		{
			is >> node->attrib;
			node->first = parse(is);
			node->second = parse(is);
		}		
		
		is >> std::ws;
		if(is.get() != ')')
			std::cout << "crap" << std::endl;
		return node;
	}
	
	Node * root;
};

double calc_cuteness(const DTree & dtree, std::set<std::string> attributes)
{
	double val = 1;
	DTree::Node * node = dtree.root;
	
	while(node != 0)
	{
		val *= node->weight;
		if(node->attrib == "")
		{
			node = 0;
		}
		else
		{
			auto it = attributes.find(node->attrib);
			if(it!=attributes.end())
				node = node->first;
			else
				node = node->second;
		}
	}
	
	return val;
}


int main() 
{
    const std::string inputFileName  = setName + ".in";
    const std::string outputFileName = setName + ".out";

    std::ifstream ifs( inputFileName.c_str() );
    std::ofstream ofs( outputFileName.c_str() );

    if(!ifs || ! ofs) 
    {
        std::cerr << "Openeing the files went wrong" << std::endl;
        return 1;
    }

    int T;
    ifs >> T;
    
    for(int t=0; t<T; ++t)
    {
		int lines;
		ifs >> lines;
		DTree dtree(ifs);
		
		//dtree.root->print();
		
		ofs       << "Case #" << (t+1) << ":\n";
        std::cout << "Case #" << (t+1) << ":" << std::endl;
        
		int animals;
		ifs >> animals;
		for(int i=0; i<animals; ++i)
		{
			std::string name;
			ifs >> name;
			int attrib_count;
			ifs >> attrib_count;
			std::set<std::string> attributes;
			for(int j=0; j<attrib_count; ++j)
			{
				std::string attrib;
				ifs >> attrib;
				attributes.insert(attrib);
			}
			
			double cuteness = calc_cuteness(dtree, attributes);
			ofs       << std::setprecision(7) << std::fixed << cuteness << "\n";
			std::cout << std::setprecision(7) << std::fixed << cuteness << std::endl;
		}
    }


    ifs.close();
    ofs.close();
    std::cout << "Done." << std::endl;

    return 0;
}
