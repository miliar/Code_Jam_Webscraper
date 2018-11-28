#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <fstream>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>

using namespace std;

struct Node
{
	double weight;
	string feature;
	int left;
	int right;

	Node(double w = 0 , string f = "", int l = -1, int r = -1)
	{
		weight = w;
		feature = f;
		left = l;
		right = r;
	}
};

void BuildTree(string treeDesc, vector<Node> & tree)
{
	int  pos0 = 0;
	while (treeDesc[pos0] != '(') pos0++;

	int pos = pos0 + 1;
	while (treeDesc[pos] != '(' && treeDesc[pos] != ')' ) pos++;

	int cur = tree.size();
	tree.push_back( Node() );
	
	istringstream iss( treeDesc.substr(pos0 + 1, pos - 1) );
	iss >> tree[cur].weight;

	if (treeDesc[pos] == '(' )
	{
		iss >> tree[cur].feature;
		int sum = 1;
		int i = pos;
		while (sum > 0)
		{
			i++;
			if (treeDesc[i] == '(') sum++;
			if (treeDesc[i] == ')') sum--;
		}

		tree[cur].left = tree.size();
		BuildTree(treeDesc.substr(pos, i - pos + 1), tree);

		while (treeDesc[i] != '(' ) i++;
		int j =  treeDesc.length() - 1;
		while (treeDesc[j] != ')' ) j--;

		tree[cur].right = tree.size();
		BuildTree(treeDesc.substr(i, j - i), tree );
		
	}

}

double Classify(const vector<Node> tree, const set<string> features)
{
	double prob = 1;

	int pos = 0;
	while (tree[pos].left != -1)
	{
		prob *= tree[pos].weight;
		if (features.find(tree[pos].feature) == features.end() )
			pos = tree[pos].right;
		else
			pos = tree[pos].left;
	}

	return prob * tree[pos].weight;
}

vector<double> SolveTestCase( )
{
	

	int L;
	cin >> L;
	
	string str;
	getline(cin, str);
	string treeDesc;
	for (int i = 0; i < L; i++)
	{
		getline(cin, str);
		treeDesc = treeDesc + " " + str;
	}

	vector<Node> tree;
	BuildTree(treeDesc, tree);

	int numAnimals;
	cin >> numAnimals;
	getline(cin, str);

	vector<double> ans(numAnimals, 0);
	for (int i = 0; i < numAnimals; i++)
	{
		string animal, name;
		int numFeatures;
		getline(cin, animal);
		istringstream iss(animal);
		iss >> name >> numFeatures;

		set<string> features;
		for (int j = 0; j < numFeatures; j++)
		{
			string temp;
			iss >> temp;
			features.insert(temp);
		}
		ans[i] = Classify(tree, features);
	}
	
	return ans;
}

void PrintAnswerToTestCase(int caseNumber,vector<double> ans )
{
	cout << "Case #" << caseNumber << ":"  << endl;
	for (int i  = 0; i < ans.size(); i++)
		cout << ans[i] << endl;
}

int main()
{
	freopen("large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	cout.setf(ios_base::fixed);
	cout.precision(9);
	int numCases;
	cin >> numCases;

	for (int caseNumber = 1; caseNumber <= numCases; caseNumber++)
		PrintAnswerToTestCase(caseNumber, SolveTestCase() );

	return 0;
}