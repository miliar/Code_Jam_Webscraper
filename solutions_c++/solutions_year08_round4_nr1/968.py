#include <algorithm>
//#include <iostream>
#include <vector>
//#include <string>
#include <fstream>
//#include "math.h"
using namespace std;

typedef struct  
{
	int G;
	int C;
	int V;
}node;

int compute(vector<node>& tree, int i);
int main()
{
	ifstream infile;
	infile.open("A-large.in.txt");
	ofstream outfile;
	outfile.open("A-large.out.txt");
	
	int N, M, V;
	size_t count;
	vector<node> tree;
	node temp;
	int i, j;

	infile>>N;

	i = 0;
	while (i<N)
	{
		tree.clear();
		count = 0;
		infile>>M>>V;
		int x = (M-1)/2;
		for (j=0; j<x; j++)
		{
			infile>>temp.G>>temp.C;
			tree.push_back(temp);
		}
		for (j=x; j<M; j++)
		{
			infile>>temp.V;
			temp.C = temp.G = -1;
			tree.push_back(temp);
		}

		//count first
		for (j=x-1; j>=0; j--)
		{
			if (tree[j].G == 1)
				tree[j].V = tree[2*j+1].V & tree[2*j+2].V;
			else
				tree[j].V = tree[2*j+1].V | tree[2*j+2].V;
		}
		if (tree[0].V != V)
		{
			count = compute(tree, 0);
			
		}
		if (count < tree.size())
		{
			outfile<<"Case #"<<i+1<<": "<<count<<endl;
		} 
		else
		{
			outfile<<"Case #"<<i+1<<": "<<"IMPOSSIBLE"<<endl;
		}
		
		i++;
	}
	infile.close();
	outfile.close();

	return 0;
}

int compute(vector<node>& tree, int i)
{
	if (tree[i].G == -1) //leaf
		return tree.size();

	int lv = tree[2*i+1].V;
	int rv = tree[2*i+2].V;
	int lc = compute(tree, 2*i+1);
	int rc = compute(tree, 2*i+2);
	if (tree[i].V == 0)//V=1
	{
		if (tree[i].G == 1) //and l or r = 0
		{
			if (tree[i].C == 0)
			{
				int temp = 0;
				if (lv == 0) temp += lc;
				if (rv == 0) temp += rc;
				return temp;
			}
			else//C=1
			{
				if (lv == 1 || rv == 1)
					return 1;
				return lc > rc ? rc+1 : lc+1;
			}
		}
		else//or  l = r = 0
		{
			return lc > rc ? rc : lc;
		}
	}
	else//V=0
	{
		if (tree[i].G == 1) //and l and r = 1
		{
			return lc > rc ? rc : lc;
		}
		else//or  
		{
			if ( tree[i].C == 1)
			{
				if (lv == 1 && rv == 1)
					return lc > rc ? rc+1:lc+1;
				else
					return 1;
			}
			else
			{
				int temp = 0;
				if (lv == 1) temp += lc;
				if (rv == 1) temp += rc;
				return temp;
			}
		}
	}
}