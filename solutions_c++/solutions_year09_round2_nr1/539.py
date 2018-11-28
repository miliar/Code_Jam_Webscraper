// gcj20091bta.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string>
#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

ifstream input_file;
char c;

struct tree
{
	double weight;
	string feature;
	tree* has;
	tree* hasnt;
	tree()
	{
		weight = 0;
		feature = "";
		has = NULL;
		hasnt = NULL;
	}
	~tree()
	{
		if (has)
			delete has;
		if (hasnt)
			delete hasnt;
	}
};

void ReadTree(tree* t)
{
	string aa;
	while (c != '(')
		input_file >> c;
	input_file >> t->weight;
	input_file >> c;
	while (true)
	{
		if (c == ')')
			return;
		if ((c >= 'a') && (c <= 'z'))
			t->feature.push_back(c);
		else
			break;
		input_file >> c;
	}
	if (t->feature.size())
	{
		t->has = new tree;
		t->hasnt = new tree;
		ReadTree(t->has);
		ReadTree(t->hasnt);

	}
	input_file >> c;
	while (c != ')')
		input_file >> c;
}

int _tmain(int argc, _TCHAR* argv[])
{
	FILE* output_file;
	input_file.open("A-large.in");
	output_file = fopen ("A-large.out","w");
	int n_tests;
	input_file >> n_tests;
	string aa;
	getline(input_file, aa);
	getline(input_file, aa);
	input_file >> c;
	for (int test = 1; test <= n_tests; ++test)
	{
		fprintf(output_file, "%s%d%s\n", "Case #", test, ": ");
		tree* root = new tree; 
		ReadTree(root);
		getline(input_file, aa);
		int n_animals;
		input_file >> n_animals;
		getline(input_file, aa);
		for (int animal = 0; animal < n_animals; ++animal)
		{
			int n_features = 0;
			getline(input_file, aa);
			string::iterator it = aa.begin();
			while ((*it++) != ' ');
			while (((*it) != ' ') && (it + 1 != aa.end()))
			{
				n_features = n_features * 10 + ((*it) - '0');
				++it;
			}
			if (n_features)
				++it;
			vector<string> features;
			for (int feature = 0; feature < n_features; ++feature)
			{
				string ff;
				while ((*it) != ' ')
				{
					ff.push_back(*it);
					if (it + 1 == aa.end())
						break;
					++it;
				}
				features.push_back(ff);
				if (it != aa.end())
					++it;
			}
			double p = 1;
			tree* cur = root;
			while (true)
			{
				p *= cur->weight;
				bool has = false;
				if (cur->feature.size())
				{
					vector<string>::iterator it = features.begin();
					for (; it < features.end(); ++it)
						if (!(*it).compare(cur->feature))
						{
							has = true;
							break;
						}
					if (has)
						cur = cur->has;
					else
						cur = cur->hasnt;
				}
				else
					break;
			}
			fprintf(output_file, "%.7f \n", p);
		}
	}

	input_file.close();
	fclose(output_file);
	return 0;
}

