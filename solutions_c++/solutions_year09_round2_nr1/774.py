#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

class Tree
{
public:
	double prob;
	string feature;
	Tree * first;
	Tree * second;

	Tree()
	{
		prob = 0;
		feature = "";
		first = second = NULL;
	}

	void fillTree(ifstream * input_source, int &depth)
	{
		depth++;
		string probability;
		stringstream probability_translator(stringstream::in | stringstream::out);
		bool has_feature = true;
		*input_source >> probability;
		probability = probability.substr(1,probability.size()-1);
		while(probability.at(probability.size()-1) == ')')
		{
			has_feature = false;
			probability = probability.substr(0,probability.size()-1);
			depth--;
		}
		//probability_translator.clear();
		prob = 0;
		probability_translator << probability;
		probability_translator >> prob;
		//const char * c_prob = probability.c_str();
		//prob = atof(c_prob);

		if(has_feature)
		{
			*input_source >> feature;
			first = new Tree;
			second= new Tree;

			first->fillTree(input_source, depth);
			second->fillTree(input_source, depth);

			if(depth > 0)
			{
				string temp;
				*input_source >> temp;
				depth--;
			}
		}
		
	}
	double getProbability(vector<string> features, double current_prob)
	{
		current_prob *= prob;
		if(feature != "")
		{
			for(int i = 0; i < features.size(); i++)
			{
				if(features.at(i) == feature)
				{
					current_prob = first->getProbability(features, current_prob);
					return current_prob;
				}
			}
			current_prob = second->getProbability(features, current_prob);
			return current_prob;
		}
		else
		{
			return current_prob;
		}
	}
	~Tree()
	{
		delete first;
		delete second;
	}
};

int main(int argc, char ** argv)
{
	ifstream input_file;
	ofstream output_file;
	input_file.open(argv[1]);
	output_file.open(argv[2]);

	int cases, lines, animals, features;
	string animal;
	vector<string> feature_list;
	Tree * tree = NULL;
	input_file >> cases;
	for(int i = 0; i < cases; i++)
	{
		delete tree;
		tree = new Tree();
		input_file >> lines;
		int depth = 0;
		tree->fillTree(&input_file,depth);
		input_file >> animals;
		output_file << "Case #" << i+1 << ":" << endl;
		for(int j = 0; j < animals; j++)
		{
			input_file >> animal;
			input_file >> features;
			feature_list.clear();
			for(int k = 0; k < features; k++)
			{
				string feature;
				input_file >> feature;
				feature_list.push_back(feature);
			}
			double probability = tree->getProbability(feature_list, 1.0);
			output_file << probability << endl;
		}
	}
}