// decision_tree.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


#include <fstream>
#include <sstream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <string>


typedef struct _animal_t {
	std::string name;
	std::set<std::string> features;
} animal_t;

typedef std::list<animal_t> animals_list_t;

typedef struct _node_t {
	double weight;
	std::string feature;
	struct _node_t *left;
	struct _node_t *right;
} node_t;

typedef struct _case_t {
	node_t *decision_tree;
	animals_list_t animals;
} case_t;
typedef std::list<case_t> cases_list_t;

double decide(node_t *tree, const animal_t &animal, double p)
{
	p *= tree->weight;

	if ((tree->left == 0) && (tree->right == 0)) {
		return p;
	} else {
		if (animal.features.find(tree->feature) != animal.features.end()) {
			if (tree->left != 0)
				return decide(tree->left, animal, p);
			else
				return decide(tree->right, animal, p);
		} else {
			if (tree->right != 0)
				return decide(tree->right, animal, p);
			else
				return p;
		}
	}
}

node_t *create_tree(std::string &s, std::string::size_type &i)
{
	node_t *root = new node_t;

	root->left = 0;
	root->right = 0;

	for ( ; i < s.length(); ) {
		switch (s[i]) {
			case ' ':
				{
					i++;
				}
				break;

			case '(':
				{
					std::string::size_type ii = s.find_first_not_of(" ", i + 1);
					std::string::size_type jj = s.find_first_of(" )", ii);
					root->weight = strtod(s.substr(ii, jj - ii).c_str(), NULL);
					i = jj;
				}
				break;

			case ')':
				{
					i++;
					return root;
				}
				break;

			default:
				{
					// feature tree tree
					std::string::size_type ii = s.find_first_not_of(" ", i);
					std::string::size_type jj = s.find_first_of(" )", ii);
					root->feature = s.substr(ii, jj - ii);
					i = jj;
					root->left    = create_tree(s, i);
					root->right   = create_tree(s, i);
				}
				break;
		}
	}

	return 0;
}

void load_data(std::istream &in, cases_list_t &cases)
{
	std::string sN;
	int N;

	std::getline(in, sN);
	N = strtoul(sN.c_str(), NULL, 10);

	for ( ; N > 0; N--) {
		//
		case_t c;

		//
		std::string sL;
		int L;

		std::getline(in, sL);
		L = strtoul(sL.c_str(), NULL, 10);

		//
		std::string dt;
		for ( ; L > 0; L--) {
			std::string s;
			std::getline(in, s);
			dt += s;
		}

		std::string::size_type dti = 0;
		c.decision_tree = create_tree(dt, dti);
		
		//
		std::string sA;
		int A;

		std::getline(in, sA);
		A = strtoul(sA.c_str(), NULL, 10);

		//
		for ( ; A > 0; A--) {
			std::string s;
			std::getline(in, s);

			animal_t animal;

			std::istringstream iss(s);

			iss >> animal.name;

			int K;
			iss >> K;

			for ( ; K > 0; K--) {
				std::string feature;

				iss >> feature;

				animal.features.insert(feature);
			}

			c.animals.push_back(animal);
		}

		//
		cases.push_back(c);
	}
}

void process(std::ostream &out, const case_t &c)
{
	for (animals_list_t::const_iterator i = c.animals.begin(); i != c.animals.end(); i++) {
		double p = decide(c.decision_tree, *i, 1.0);

		char aux[128];
		sprintf(aux, "%.7f", p);

		out << aux << std::endl;
	}
}

void process_data(std::ostream &out, cases_list_t &cases)
{
	for (int i = 0; cases.empty() == false; i++) {
		out << "Case #" << (i + 1) << ":" << std::endl;
		process(out, cases.front());

		cases.pop_front();
	}
}


int _tmain(int argc, _TCHAR* argv[])
{
// 	std::ifstream in("sample.in");
//	std::ofstream out("sample.out");
	std::ifstream in("A-small-attempt0.in");
	std::ofstream out("A-small-attempt0.out");
//	std::ifstream in("A-large.in");
//	std::ofstream out("A-large.out");

	cases_list_t cases;

	load_data(in, cases);
	process_data(out, cases);

	return 0;
}
