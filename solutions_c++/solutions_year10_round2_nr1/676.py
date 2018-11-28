#include <iostream>
#include <string>
#include <vector>
using namespace std;

struct node
{
	string name;
	vector<struct node *> ch;
};



bool search(struct node * tree, string path)
{
	//cout << "search called" << endl;
	if(path.empty()) return true;
	int i = 1,j;
	string temp;
	while(path[i]!='/' && i!=path.length())
	{
		temp.push_back(path[i]);
		i++;	
	}
	for(j=0;j<(tree->ch).size();j++)
	{
		if((tree->ch)[j]->name.compare(temp)==0)
			return search((tree->ch)[j],path.substr(i));
	}
	return false;
}

int create(struct node *tree, string path)
{
	//cout << "Create called" << endl;
	if(path.empty()) return 0;
	int i = 1,j;
	string temp;
	while(path[i]!='/' && i!=path.length())
	{
		temp.push_back(path[i]);	
		i++;	
	}
	for(j=0;j<(tree->ch).size();j++)
	{
		if((tree->ch)[j]->name.compare(temp)==0)
		{
			return create((tree->ch)[j],path.substr(i));
		}
	}	
		
		struct node * n = new struct node;
		n->name = temp;
		(tree->ch).push_back(n);
		return 1 + create((tree->ch)[(tree->ch).size()-1],path.substr(i));	
}



int main()
{
	int T,I;
	cin >> T;
	for(I=1;I<=T;I++)
	{
		int n,m,i,ret=0;

		struct node * tree = new struct node;
		tree->name = "/";

		cin >> n >> m;

		for(i=0;i<n;i++)
		{
			string in;
			cin >> in;
			if(!search(tree,in)) create(tree,in);
		}
		for(i=0;i<m;i++)
		{
			string in;
			cin >> in;
			if(!search(tree,in)) ret += create(tree,in);
		}
		cout << "Case #" << I << ": " << ret << endl;		
	}
}

