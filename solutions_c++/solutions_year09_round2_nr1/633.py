#include <iostream>
#include <vector>
#include <list>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <math.h>
#include <map>
#include <set>
#include <iomanip>

#define ull_int unsigned long long int 
#define ll_int long long int 


std::string itos(int a)
{
	char buf[10];
	itoa(a, buf, 10);
	return std::string(buf);
}

std::string ftos(float f)
{
	std::ostringstream oss;
	oss << f;
	return oss.str();
}
int					stoi(std::string s)
{
	return atoi(s.c_str());
}

float				stof(std::string s)
{
	return atof(s.c_str());
}

inline bool space(char c)
{
	return c == ' ' || c == '\t' || c == '\n';
}

inline bool notspace(char c)
{
	return !space(c);
}

//break a sentence into words
std::vector<std::string> split(const std::string& s)
{
	std::vector<std::string> ret;
	std::string::const_iterator i = s.begin();
	while(i != s.end())
	{
		i = std::find_if(i, s.end(), notspace); // find the beginning of a word
		std::string::const_iterator j = std::find_if(i, s.end(), space); // find the end of the same word
		if(i != s.end())
		{
			ret.push_back(std::string(i, j)); //insert the word into std::vector
			i = j; // repeat 1,2,3 on the rest of the line.
		}
	}
	return ret;
}



struct s_tree
{
	bool leaf;
	std::string feature;
	float value;
};

s_tree g_tree[200];

std::set<std::string> g_features;

int createTree(int idx, std::vector<std::string> tree, int idx_firstWord)
{
	int lastWord;

	int nbWordCurTree = 0;
	int count = 0;
	while (1)
	{
		if (tree[idx_firstWord + nbWordCurTree] == std::string("["))
			count++;
		if (tree[idx_firstWord + nbWordCurTree] == std::string("]"))
			count--;
		nbWordCurTree++;
		if (count == 0)
			break;
	}

	if (nbWordCurTree == 3) // [ value ]
	{
		g_tree[idx].leaf = true;
		g_tree[idx].value = stof(tree[idx_firstWord + 1]);
	}
	else 
	{
		// tree ::= [ weight feature tree tree ]
		g_tree[idx].leaf = false;
		g_tree[idx].value = stof(tree[idx_firstWord + 1]);
		g_tree[idx].feature = tree[ idx_firstWord + 2];

		int last_word_done = createTree(2 * idx + 1, tree, idx_firstWord + 3);
		createTree(2 * idx + 2, tree, last_word_done);
	}

	return idx_firstWord + nbWordCurTree;
}

void createTreeWrapper(std::string tree)
{
	int pos;
	while ( (pos = tree.find("(")) != std::string::npos)
	{
		tree.replace(pos, 1, " [ ");
	}
	while ( (pos = tree.find(")")) != std::string::npos)
	{
		tree.replace(pos, 1, " ] ");
	}

	std::vector<std::string> vec_tree = split(tree);

	createTree(0, vec_tree, 0);
}

double computeProba()
{
	int idx_node = 0;
	double proba = 1;

	while (1)
	{
		proba = proba * g_tree[idx_node].value;

		if (g_tree[idx_node].leaf == true)
			break;
		else
		{
			if (g_features.find(g_tree[idx_node].feature) != g_features.end())
				idx_node = 2 * idx_node + 1;
			else
				idx_node = 2 * idx_node + 2;
		}
	}
	return proba;
}

int main(int argc, char *argv[])
{

	std::ifstream input(argv[1]);

	int nbCases;

	input >> nbCases;

	for (int iter_case = 0; iter_case < nbCases; iter_case++)
	{

		int nbLines;

		input >> nbLines;
		//FIXME


		std::stringstream sstr;
		char buf[5000];
		input.getline(buf, 5000);
		for (int i = 0; i < nbLines; i++)
		{
			input.getline(buf, 5000);

			sstr << buf;
		}

		std::string tree = sstr.str();

		createTreeWrapper(tree);

		int nbAnimals;

		input >> nbAnimals;
		std::cout << "Case #" << iter_case + 1 << ": "<< std::endl;		
		for (int i = 0; i < nbAnimals; i++)
		{
			g_features.clear();

			std::string animalName;
			int nbFeature;

			input >> animalName;
			input >> nbFeature;

			for (int idx_feature = 0; idx_feature < nbFeature; idx_feature++)
			{
				std::string cur_feature;
				input >> cur_feature;
				g_features.insert(cur_feature);
			}

			double res = computeProba();
			std::cout << std::fixed << std::setprecision (7) << res << std::endl;		
		}
	}
}
