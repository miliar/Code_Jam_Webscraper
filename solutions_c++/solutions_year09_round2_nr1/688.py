#include "stdafx.h"

#include <iostream>
#include <fstream>
#include <stdio.h>
#include <string>
#include <vector>
#include <sstream>
#include <map>

using namespace std;

typedef long long ll;
typedef vector <int> vi;
typedef vector <vi> vvi;

int nextFeature = 1;
map<string, int> featureMap;
struct TreeNode {
	double probability;
	int featureNum;
	int left, right;
	TreeNode() {
		probability = 0.0;
		featureNum = 0;
		left = right = 0;
	}
};
vector<TreeNode> tree;

int buildTree(ifstream& fin)
{
	tree.push_back(TreeNode());
	int curId = tree.size() - 1;
	string tmp;
	fin >> tmp; // "("
	fin >> tree[curId].probability;
	fin >> tmp; // ")" or feature
	if (tmp != ")") {
		if (featureMap.find(tmp) != featureMap.end()) {
			tree[curId].featureNum = featureMap.find(tmp)->second;
		}
		else {
			tree[curId].featureNum = featureMap[tmp] = nextFeature++;
		}
		int k = buildTree(fin);
		tree[curId].left = k;
		k = buildTree(fin);
		tree[curId].right = k;
		fin >> tmp;  // ")"
	}
	return curId;
}

void parseTree(int curNode, vi& featureList, double& probability)
{
	probability *= tree[curNode].probability;
	if (tree[curNode].featureNum) {
		if (featureList[tree[curNode].featureNum])
			parseTree(tree[curNode].left, featureList, probability);
		else
			parseTree(tree[curNode].right, featureList, probability);
	}
}

int main()
{
	ifstream fin("A-large(2).in");
	ofstream fout("file.out");
	
	fout.precision(7);
	int T;
	fin >> T;
	for (int testCase = 1; testCase <= T; ++testCase) {
		int ntmp;
		fin >> ntmp;
		fout << "Case #" << testCase << ":" << endl;
		tree.clear();
		featureMap.clear();
		nextFeature = 1;
		buildTree(fin);
		int numAnimals;
		fin >> numAnimals;
		for (int i = 0; i < numAnimals; ++i) {
			double probability = 1.0;
			string animalName;
			fin >> animalName;
			int numFeatures;
			fin >> numFeatures;
			vector<int> featuresList(featureMap.size() + 1);
			for (int j = 0; j < numFeatures; ++j) {
				string tmp;
				fin >> tmp;
				if (featureMap.find(tmp) != featureMap.end()) {
					featuresList[featureMap.find(tmp)->second] = 1;
				}
			}
			parseTree(0, featuresList, probability);
			fout << fixed << probability << endl;
		}
	}

	return 0;
}
