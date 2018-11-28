#include <set>
#include <vector>
#include <string>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <sstream>
using namespace std;

struct Node
{
	double weight;
	string feature;
	Node * left;
	Node * right;
	Node()
	{
		weight = 1;
		feature = "";
		left = right = NULL;
	}
	double Travel(double value, const set<string> & fset)
	{
		double ret = weight * value;
		if(fset.count(feature) || feature.size() == 0)
		{
			if(left)
				return left->Travel(ret, fset);
			return ret;
		}
		else
		{
			if(right)
				return right->Travel(ret, fset);
			return ret;
		}
		return ret;
	}
	~Node()
	{
		delete left;
		delete right;
	}
};

bool IsDouble(const string & str)
{
	for(int i = 0; i < str.size(); i++)
		if(str[i] == '.' || (str[i] >= '0' && str[i] <= '9'))
			continue;
		else return false;
	return true;
}

Node * BuildTree(const string & str)
{
	string tree;
	tree.reserve(2000);
	for(int i = 0; i < str.size(); i++)
		if(str[i] == '(')
		{
			tree += " ( ";
		}
		else if(str[i] == ')')
		{
			tree += " ) ";
		}
		else tree += str[i];
	stringstream ss;
	ss << tree;
	Node * root = new Node();
	root->feature = "";
	root->weight = 1;
	vector<Node*> stack;
	stack.push_back(root);
	string buf;
	while(ss >> buf)
	{
		if(buf == ")")
		{
			stack.pop_back();
			continue;
		}
		if(buf == "(")
		{
			Node * top = stack.back();
			Node * next = new Node();
			if(top->left == 0)
				top->left = next;
			else
				top->right = next;
			stack.push_back(next);
			continue;
		}
		if(IsDouble(buf))
		{
			stringstream tmp;
			tmp.clear();
			tmp << buf;
			tmp >> stack.back()->weight;
			continue;
		}
		stack.back()->feature = buf;
	}
	return root;
}

int main()
{
	string buf;
	ifstream in("in.txt");
	getline(in, buf);	
	int tests = atoi(buf.c_str());
	string tree;
	tree.reserve(2000);
	for(int t = 1;t  <= tests; t++)
	{
		getline(in, buf);
		int lines = atoi(buf.c_str());
		tree.clear();
		for(int i = 0; i < lines; i++)
		{
			getline(in, buf);
			tree += buf;
			tree += ' ';
		}
		Node * root = BuildTree(tree);
		getline(in, buf);
		int animals = atoi(buf.c_str());
		cout << "Case #" << t << ":" << endl;
		for(int i = 0; i < animals; i++)
		{
			getline(in, buf);
			stringstream ss;
			ss.clear();
			ss << buf;
			ss >> buf;
			int features;
			ss >> features;
			set<string> fset;
			fset.clear();
			for(int j = 0; j < features; j++)
			{
				ss >> buf;
				fset.insert(buf);
			}
			cout.setf(cout.fixed);
			cout.precision(7);
			cout << root->Travel(1, fset) << endl;
		}
		delete root;
		
	}
	return 0;
}