#include <string>
#include <fstream>
#include <iostream>
using namespace std;

struct TSTreeNode
{
	bool isLeaf;
	char *content;
	TSTreeNode *branch[26];
};

struct TSTree
{
	TSTreeNode *root;
	TSTree()
	{
		root = new TSTreeNode();
		root->isLeaf = false;
	}

	void addNode(const char *cont);
	void continueAddNode(const char *cont, int depth, TSTreeNode *parent);
	int search(string str, int index,int depth,TSTreeNode *parent);
};

int TSTree::search(string str, int index,int depth,TSTreeNode *parent)
{
	int end;
	string temp;
	if(str[index] == '(')
	{
		end = str.find(")",index);
		temp = str.substr(index+1,end-index-1);
		index = end+1;
	}
	else
	{
		temp = str.substr(index,1);
		index ++;
	}
	int res = 0;
	for( int i = 0; i < temp.length(); i++ )
		if(parent->branch[temp[i]-'a'] == NULL)
			continue;
		else if(parent->branch[temp[i]-'a']->isLeaf)
			res++;
		else
			res +=search(str,index,depth+1,parent->branch[temp[i]-'a']);
	return res;
}

void TSTree::addNode(const char *cont)
{
	if(strlen(cont) > 15)
		return;
	int depth = 0;
	continueAddNode(cont,1,this->root);
}

void TSTree::continueAddNode(const char *cont, int depth, TSTreeNode *parent)
{
	if( parent->branch[cont[depth-1]-'a'] == NULL)
	{
		parent->branch[cont[depth-1]-'a'] = new TSTreeNode();
	}
	TSTreeNode *now = parent->branch[cont[depth-1]-'a'];
	if( depth == strlen(cont) )
	{
		now->isLeaf = true;
		now->content = new char[strlen(cont)];
		strcpy(now->content,cont);
	}
	else
	{
		now->isLeaf = false;
		continueAddNode(cont,depth+1,now);
	}
}

void main()
{
	ifstream inf("E:\\A-large.in");
	ofstream ouf("E:\\A-large.out");

	string str;
	if(inf)
	{
		TSTree tree;
		getline(inf,str);
		int blank1 = str.find(" ",0);
		int L = atoi(str.substr(0,blank1).c_str());
		int blank2 = str.find(" ",blank1 + 1);
		int D = atoi(str.substr(blank1+1,blank2-blank1-1).c_str());
		int N = atoi(str.substr(blank2+1,str.length()-blank2-1).c_str());
		int i = 1;
		while(i <= D&&getline(inf,str))
		{
			const char * cstr = str.c_str();
			tree.addNode(cstr);
			i ++;
		}
		i = 1;
		int res = 0;
		while(i <= N&&getline(inf,str))
		{
			res = tree.search(str, 0,0,tree.root);
			ouf<<"Case #"<<i<<": "<<res<<endl;
			i ++;
		}
	}
}