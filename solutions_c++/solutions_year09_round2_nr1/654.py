#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
using namespace std;

struct Node
{
	string feature;
	double prob;
	Node *left;
	Node *right;
} root;

struct Animal
{
	string name;
	set<string> fs;
};

istringstream iss;

void init(string input, Node* node)
{
	string left = "";
	string right = "";
	
	int count = 0;
	int from, to;
	int i;
	int index = input.find('(');
	input[index] = ' ';
	index = input.find_last_of(')');
	input[index] = ' ';

	index = input.find('(');
	if(index != input.npos)
	{
		count = 1;
		for(i = index+1; i < input.length(); ++i)
		{
			if(input[i] == '(')
				count++;
			else if(input[i] == ')')
			{
				count--;
				if(count == 0)
				{
					left = input.substr(index, i - index + 1);
					right = input.substr(i+1);
					break;
				}
			}
		}
		
	}

		iss.clear();
		iss.str(input);
		iss >> node->prob;
		if(left != "")
		{
			iss >> node->feature;
			node->left = new Node();
			node->right = new Node();
			init(left, node->left);
			init(right, node->right);
		}
		else
		{
			node->feature = "";
			node->left = NULL;
			node->right = NULL;
		}
}

double cal(Animal ani)
{
	double res = 1.0;
	
	Node* p = &root;
	while(p != NULL)
	{
		res *= p->prob;
		if(p->feature != "")
		{
			if(ani.fs.count(p->feature) > 0)
			{
				p = p->left;
			}
			else p = p->right;
		}
		else break;
	}

	return res;
}

int main()
{
	ifstream ifs("A-small-attempt1.in");
	ofstream ofs("A-small-attempt1.out");

	int T;
	ifs >> T;
	int L, A, n;
	for(int caseNo = 1; caseNo <= T; ++caseNo)
	{
		ifs >> L;
		string buf = "";
		char cs[100];
		ifs.getline(cs, 100);
		for(int i = 0; i < L; ++i)
		{
			ifs.getline(cs, 100);
			buf += cs;
		}
		init(buf, &root);
		ifs >> A;
		Animal ani;
		ofs << "Case #" << caseNo << ":" << endl;
		for(int i = 0; i < A; ++i)
		{
			ifs >> ani.name;
			ifs >> n;
			ani.fs.clear();
			for(int k = 0; k < n; ++k)
			{
				ifs >> buf;
				ani.fs.insert(buf);
			}
			ofs.precision(7);
			ofs << cal(ani) << endl;
		}
		
	}

	ifs.close();
	ofs.close();
	
	return 0;
}