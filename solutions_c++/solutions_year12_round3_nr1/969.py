// CodeJam2012Round1BProblemA.cpp : Defines the entry point for the console application.
//
//Include some standard headers for windows/STL
#include <tchar.h>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
using namespace std;

struct node
{
	int id;
	vector <int> nodePtrs;
	int parsed;
};
int setChildren(vector <node> &tree,int thisNode,int set)
{
	if (tree[thisNode-1].parsed==set) 
		return true;
	tree[thisNode-1].parsed=set;
	for (int i=0;i<tree[thisNode-1].nodePtrs.size();i++)
	{
		if (setChildren(tree,tree[thisNode-1].nodePtrs[i],set)) return true;
	}
	return false;
}
string solve(vector <node> &tree)
{
	int treeSize = tree.size();
	for (int i=1;i<=treeSize;i++)
	{
		if (setChildren(tree,i,1))
			return "Yes";
		setChildren(tree,i,0); //unset children

	}
	return "No";

}

int _tmain(int argc, _TCHAR* argv[])
{
	std::ifstream infile("A-large.in");	
	std::ofstream outfile("A-large.out");
	outfile<<setprecision(10);


	int totalCases = 0;

	infile>>totalCases;
	for (int i = 1;i<=totalCases;i++)
	{
		int N, Mi;
		infile>>N;
		vector <node> classInheritanceTree;
		for (int j=1;j<=N;j++)
		{
			infile>>Mi;
			node newNode;
			newNode.id = j;
			for (int k=1;k<=Mi;k++)
			{
				int tmp;
				infile>>tmp;
				newNode.nodePtrs.push_back(tmp);
			}
			classInheritanceTree.push_back(newNode);


		}
		string result = solve(classInheritanceTree);


		cout<<"Case #"<<i<<": "<<result<<endl;
		outfile<<"Case #"<<i<<": "<<result<<endl;



	}
	return 0;

}