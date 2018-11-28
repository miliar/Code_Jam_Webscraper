// test.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <stdio.h>
#include <string.h>
#include <list>
#include <string>
using namespace std;
class TreeNode
{
public:
	list<TreeNode*> children;
	char* name;
	static int nodes;
	
	TreeNode(char* str)
	{
		name = new char[strlen(str)+1];
		strcpy(name, str);
	}
	~TreeNode()
	{
		if(name!=NULL)
			delete [] name;
	}
	TreeNode* goChild(char* s)
	{
		
		list<TreeNode*>::iterator end = children.end();
		for(list<TreeNode*>::iterator it = children.begin();it!=end;++it)
		{
			if(strcmp(s, (*it)->name)==0)return *it;
		}
		TreeNode * pNode = new TreeNode(s);
		children.push_back(pNode);
		nodes++;
		return pNode;
	}

	static void Insert(char* path, TreeNode* node)
	{
		char* p=path;
		do
		{
			p=p+1;
			char* pNext = strchr(p,'/');
			if(pNext!=NULL)
				*pNext = '\0';
			node = node->goChild(p);
			p=pNext;
		}while(p!=NULL);

	}
};
	int TreeNode::nodes=0;
#include <stdio.h>
#include <stdlib.h>
int main(int argc, char* argv[])
{
    if (argc<2)
	{
	  printf("input file name.\n");
	  exit(1);
	}

	FILE *file = fopen(argv[1], "r");

	if (file == NULL) {
	  printf("Can't open input file. \n");
	  exit(1);
	}

	int nTests= 0;
	if( fscanf(file, "%d", &nTests) == EOF)
	{
	  printf("Error File Format. \n");
	  exit(1);
	}

	for(int i=0;i<nTests;++i)
	{
		int n =0, m=0;
		if (fscanf(file, "%d %d", &n, &m) == EOF) {
	    printf("Error File Format. \n");
	    exit(1);
		}
		TreeNode* root=new TreeNode("");
		for(int i=0;i<n;++i)
		{
			char path[256];

			if (fscanf(file, "%s", path) == EOF) {
				printf("Error File Format. \n");
				exit(1);
			}
			TreeNode::Insert(path, root);
		}
		int oldNodes = root->nodes;
		for(int i=0;i<m;++i)
		{
			char path[256];

			if (fscanf(file, "%s", path) == EOF) {
				printf("Error File Format. \n");
				exit(1);
			}
			TreeNode::Insert(path, root);
		}
		int newNode = root->nodes - oldNodes;
	  //int n, k;
	  //if (fscanf(file, "%d %d", &n, &k) == EOF) {
	  //  printf("Error File Format. \n");
	  //  exit(1);
	  //}
	  //int temp = (1<<n) - 1;
	  ////printf("n %d k %d temp %x \n", n, k, temp);
	  //int temp2 = k&temp;
	  ////printf("n %d k %d temp %x \n", n, k, temp2);
	  ////printf("temp +1 %x \n", temp+1);


	  ////printf("temp&(temp + 1) %x \n", temp&(temp + 1));
	  ////if (temp&(temp + 1)) printf("hehe\n");
	  printf("Case #%d: %d\n", i+1, newNode);
	}
	return 0;
}
