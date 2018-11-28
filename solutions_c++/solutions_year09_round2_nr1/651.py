#include<iostream>
#include<vector>
#include<algorithm>
#include<stdlib.h>
#include<sstream>
#include<iomanip>
using namespace std;


struct node
{
	double weight;
	string feature;
	node * hasFeature;
	node * noFeature;
	
	node()
	{
		feature = "";
	}
};

void parse(vector<string> in, node * root)
{
	//cout << "WORDS IN MY TREE " << endl;
	
	//for(int i = 0; i < in.size();i++)
	//	cout << in[i] << endl;
	int pos = 0;
	
	//remove preceding '('
	if(in[0][0] == '(')
	{
		if(in[0].size() == 1)
		{
			pos++;
		}
		else
		{
			in[0] = in[0].substr(1);
		}
	}
	
	//cout << "weight string is " << in[pos] << endl;
	double weight = atof(in[pos].data());
	root->weight = weight;
	//cout << "weight is " << weight << endl;
	pos++;
	
	if(pos == in.size())
		return;
	//if the node has a feature
	if(in[pos][0] != '(' && in[pos][0] != ')')
	{
		//cout << "wtf " << in[pos] << endl;
		root->feature = in[pos];
		//cout << "feature is " << root->feature << endl;
		int parenCount = 0;
		vector<string> leftTree;
		pos++;
		for(; pos < in.size();pos++)
		{
			leftTree.push_back(in[pos]);
			if(in[pos][0] == '(')
			{
				parenCount++;
				
			}
			if(in[pos][in[pos].size()-1] == ')')
			{
				parenCount--;
				if(parenCount == 0)
				{
					break;
				}
			}
		}
		pos++;
		parenCount = 0;
		vector<string> rightTree;
		for(; pos < in.size();pos++)
		{
			rightTree.push_back(in[pos]);
			if(in[pos][0] == '(')
			{
				parenCount++;
				
			}
			if(in[pos][in[pos].size()-1] == ')')
			{
				parenCount--;
				if(parenCount == 0)
				{
					break;
				}
			}
		}
				
	
		node * left = new node;
		node * right = new node;
		root->hasFeature = left;
		root->noFeature = right;
		parse(leftTree, root->hasFeature);
		parse(rightTree, root->noFeature);
	}




}

int find(vector<string> v, string a)
{
	for(int i = 0; i < v.size();i++)
	{
		if(v[i] == a)
			return i;
	}
	return -1;
}

double getVal(node * root, vector<string> features)
{

	if(root->feature == "")
		return root->weight;
	
	if(find(features, root->feature) != -1)
		return root->weight * getVal(root->hasFeature, features);
	
	return root->weight * getVal(root->noFeature, features);
}


int main()
{
	int testCases;
	cin >> testCases;
	
	for(int test = 0; test < testCases;test++)
	{
		int lines;
		cin >> lines;
		string g;
		getline(cin,g);
		vector<string> tree;
		vector<string> words;
		stringstream s;
		for(int i = 0; i < lines;i++)
		{
			getline(cin,g);
			s << g;
			words.push_back(g);
		}
		while(s >> g)
		{
			//cout << "g is " << g << endl;
			while(g.size() > 0 && (g[0] == '(' || g[0] == ')') )
			{
				string b;
				b.push_back(g[0]);
				tree.push_back(b);
				g = g.substr(1);
			}
			vector<string> temp;
			while(g.size() > 0 &&  g[g.size()-1] == ')')
			{
				string b;
				b.push_back(')');
				temp.push_back(b);
				
				g = g.substr(0,g.size()-1);	
			}
			if(g.size() > 0)
			{
				tree.push_back(g);
				//cout << "g is here " << g << endl;
			}
			for(int j = 0; j < temp.size();j++)
			{
			//	cout << "temp is " << temp[j] << endl;
				tree.push_back(temp[j]);
			}
		}
		node * root = new node;
		parse(tree, root);
		int numAnimals;
		cin >> numAnimals;
		
		cout << "Case #" << (test+1) << ": " << endl;
		for(int i = 0; i < numAnimals;i++)
		{
			cin >> g;
			int numFeatures;
			vector<string> features;
			cin >> numFeatures;
			for(int j = 0; j < numFeatures;j++)
			{
				cin >> g;
				features.push_back(g);
				//cout << "g is " << g << endl;
			}
			
			cout << fixed << setprecision(7) << getVal(root,features) << endl;
		}

	}


}






















