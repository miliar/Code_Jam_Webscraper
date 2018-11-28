#include "stdafx.h"

#include <string>
#include <vector>
#include <fstream>
#include <set>
#include <algorithm>
#include <iostream>
#include <sstream>

using namespace std;

struct TreeNode
{
	TreeNode* left;
	TreeNode* right;
	string	name;
	double probability;

	TreeNode() {}

	TreeNode(TreeNode* _left, TreeNode* _right, string _name, double _prob) :
	left(_left), right(_right), name(_name), probability(_prob) {}
};

TreeNode* parseString(string& line)
{

	TreeNode* node = new TreeNode;
	bool has_subtrees = count(line.begin(), line.end(), '(') > 1;
	bool has_name = count_if(line.begin(), line.end(), isalpha) > 0;

	//bool weightIsParsed = false;
	if (!has_subtrees)
	{
		node->left = NULL;
		node->right = NULL;
	}
	else
	{
		size_t left_node_begin, left_node_end, right_node_begin, right_node_end;
		left_node_begin = line.find('(', 1);

		int openBracketsCount = 1, closedBracketsCount = 0;
		
		int position = left_node_begin + 1;
		while (openBracketsCount != closedBracketsCount)
		{
			if (line[position] == '(') {++openBracketsCount; ++position; continue; }
			else if (line[position] == ')') {++closedBracketsCount; ++position; continue; }

			++position;
		}
		left_node_end = position - 1;

		while (line[position] != '(')
		{
				++position;
		}

		right_node_begin = position + 1;
		openBracketsCount = 1, closedBracketsCount = 0;

		while (openBracketsCount != closedBracketsCount)
		{
			if (line[position] == '(') {++openBracketsCount; ++position; continue; }
			else if (line[position] == ')') {++closedBracketsCount; ++position; continue; }

			++position;
		}
		right_node_end = position - 1;

		node->left = parseString(line.substr(left_node_begin, left_node_end - left_node_begin + 1));
		node->right = parseString(line.substr(right_node_begin, right_node_end - right_node_begin + 1));
	}

	string weight = "";
	int position = 0;
	// parse weight
	while(true) {												
		if (line[position] == '(') 
		{
			++position;
			continue;
		}
		else if (line[position] == ')')
		{
			++position;
			break;
		}
		else if (line[position] == ' ' && weight.size() != 0) {
			++position;
			break;
		}

		weight += line[position];
		++position;					
	}
	node->probability = atof(weight.c_str());

	if (has_name) {
		// parse name
		while (line[position] == ' ')
		{
			++position;
		}
		string name;
		while(true) {												
			if (line[position] != ' ') 
			{
				name += line[position];
				++position;
			}
			else {
				++position;
				break;				
			}						
		}
		node->name = name;					
	}	

	return node;
}

double calcProbability(TreeNode* node, double p, set<string>& features)
{
	if (node->left == NULL) return p * node->probability;
	else if (features.find(node->name) != features.end()) {
		return calcProbability(node->left, p * node->probability, features);
	}
	else
	{
		return calcProbability(node->right, p * node->probability, features);
	}
}

void task1(const char* in_filename, const char* out_filename)
{
	ifstream in(in_filename);
	ofstream out(out_filename);

	if (in.is_open())
	{
		unsigned int N, L;
		string line;

		//in >> N;		
		getline(in, line);
		N = atoi(line.c_str());
		// N - cases count		
		for (unsigned int caseNumber = 1; caseNumber <= N; ++caseNumber) {
			
			//in >> L;	
			getline(in, line);
			L = atoi(line.c_str());
			string treeLine = "";
			for (unsigned int lineNumber = 0; lineNumber < L; ++lineNumber) {
				getline(in, line);
				treeLine += line + " ";				
			}

			TreeNode* root = parseString(treeLine);
			getline(in, line);
			L = atoi(line.c_str());
			
			out << "Case #" << caseNumber << ": " << endl;
			for (int i = 0; i < L; ++i) {
				getline(in, line);
				stringstream stream(line);				
				int n;
				string animalName;
				stream >> animalName >> n;
				set<string> features;
				string f;
				for (int j = 0; j < L; ++j) {
					stream >> f;
					features.insert(f);
				}
				
				out << calcProbability(root, 1, features) << endl;											
			}		
		}
	}
	else
	{
		throw "File not found";
	}
	in.close();
	out.close();
}


int _tmain(int argc, _TCHAR* argv[])
{
	//task1("D:\\C-large.in", "D:\\C-large.out");
	task1("D:\\A-small-attempt0.in", "D:\\A-small-attempt0.out");
	return 0;
}

