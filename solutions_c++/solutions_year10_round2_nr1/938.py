#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>

using namespace std;


ifstream fin("in.txt");
#define cin fin

ofstream fout("out.txt");
#define cout fout


struct node
{
	string val;
	map<string, node*>children;
};

// /home/gcj/finals
vector<string> getDirectoriesInPath(string s)
{
	vector<string>vec;
	int i;
	string tmp = "";
	for(i=0; i<s.size(); i++)
	{
		if(s[i] == '/')
		{
			if(tmp.size())
			{
				vec.push_back(tmp);
				tmp = "";
				continue;
			}
		}
		else
		{
			tmp += s[i];
		}
	}

	if(tmp.size())
	{
		vec.push_back(tmp);
		tmp = "";
	}
	return vec;
}

int makeGraph(vector<string> paths, vector<string> nPaths)
{
	int allocated = 0;

	node* root = new node();
	root->val = "root";
	node* n = root;

	int i, j;
	for(i=0; i<paths.size(); i++)
	{
		n = root;
		vector<string> vec = getDirectoriesInPath(paths[i]);
		for(j=0; j<vec.size(); j++)
		{
			if(n->children.find(vec[j]) == n->children.end())
			{
				node* nn = new node();
				nn->val = vec[j];
				n->children[vec[j]] = nn;
			}
			n = n->children[vec[j]];
		}
	}

	for(i=0; i<nPaths.size(); i++)
	{
		n = root;
		vector<string> vec = getDirectoriesInPath(nPaths[i]);
		for(j=0; j<vec.size(); j++)
		{
			if(n->children.find(vec[j]) == n->children.end())
			{
				node* nn = new node();
				nn->val = vec[j];
				n->children[vec[j]] = nn;

				allocated++;
			}
			n = n->children[vec[j]];
		}
	}
	return allocated;
}

int main()
{
	int t, i, j, k;
	cin>>t;
	for(k=0; k<t; k++)
	{
		int n, m;
		cin>>n>>m;
		vector<string>v1(n);
		vector<string>v2(m);
		for(i=0; i<n; i++)
		{
			cin>>v1[i];
		}
		for(i=0; i<m; i++)
		{
			cin>>v2[i];
		}
		int a = makeGraph(v1, v2);
		cout<<"Case #"<<k+1<<": "<<a<<endl;
	}
	return 0;
}