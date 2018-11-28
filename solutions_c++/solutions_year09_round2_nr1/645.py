#include<iostream>
#include<stdio.h>
#include <fstream>
#include <sstream>
#include <istream>
#include <vector>
#include <algorithm>
#include <map>
#include <string>

using namespace std;


#define LINT long long int
#define LUINT unsigned long long int
std::ifstream file;

void parse_tree(vector<pair<string, double> >& tree, int index)
{
	//std::cout << index << endl;
	char c;
	file >> std::ws >> c;
	if (c != '(')
		cout << "erreur (:" << c <<endl;

	double value;
	string token("");

	file >> std::ws >> value;
	file >> std::ws;
	if (file.peek() == ')')
	{
		file >> std::ws >> c;
		//std::cout << "leaf :"<< index << " "  << value << endl;
		tree[index] = pair<string, double>(token, value);
		return;
	}
	file >> std::ws >> token;
	
	//std::cout <<"Node: "<< index << " " << value << "," << token << endl; 
	tree[index] = pair<string, double>(token, value);

	parse_tree(tree, 2 * index + 1);
	parse_tree(tree, 2 * index + 2);

	file >> std::ws >> c;
	if (c != ')')
		cout << "erreur )" << endl;
}

double get_leaf(vector<pair<string, double> >& tree, int index, pair<string, vector<string> >& animal)
{
	//std::cout <<"index" << index<<" "<< tree[index].second << endl;
	if (tree[index].first.compare("") == 0)
		return tree[index].second;
	else
	{
		
		int i = 0;
		vector<string>::iterator iter;
		iter = find(animal.second.begin(), animal.second.end(), tree[index].first);
		if (iter == animal.second.end())
			return tree[index].second * get_leaf(tree , 2 * index + 2, animal);
		else
			return tree[index].second * get_leaf(tree , 2 * index + 1, animal);
	}
	std::cout << "IMPOSSIBLE" << endl;
	return 0;
}

int main(int argc, char** argv)
{
	
	file.open(argv[1]);
	int NbrCase;
	char str[2000];
	file >> NbrCase;
	for (int k = 1; k <= NbrCase; ++k)
	{
		LINT NbNode, NbAnimal;
		file >> NbNode;
		long long int total = 2;
		
		vector<pair<string, double> > tree(10000000);
		

		parse_tree(tree, 0);
		file >> NbAnimal;
		vector<pair<string, vector<string> > > animals(NbAnimal);
		for (int i = 0; i < NbAnimal; ++i)
		{
			string name;
			file >> name;
			int NbCarac;
			file >> NbCarac;
			vector<string> caracs;
			for (int j = 0; j < NbCarac; ++j)
			{
				string carac;
				file >> carac;
				caracs.push_back(carac);
			}
			animals[i] = pair<string, vector<string> >(name, caracs);
		}
		

		std::cout << "Case #" << k <<  ":"<<endl;
		for (int i = 0; i < animals.size(); i ++)
			printf("%.7f\n", get_leaf(tree, 0, animals[i]));
		
	}
	return 0;
}


/*
2
anteater 1 cool
cockroach 0*/