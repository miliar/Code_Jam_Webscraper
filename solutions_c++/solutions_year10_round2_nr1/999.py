#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <vector>
#include <iostream>
using namespace std;

struct Node
{
	vector<Node*> pChild;
	string dir_name;
};

Node* Exist(Node* r, const string& dir_name)
{
	for (int i=0; i<r->pChild.size(); ++i)
	{
		Node* h = r->pChild[i];
		if (h->dir_name == dir_name)
			return h;
	}
	return NULL;
}

Node* Create(Node* r, const string& dir_name)
{
	Node* h = new Node;
	h->dir_name = dir_name;
	r->pChild.push_back(h);
	return h;
}

int main()
{
	int T;
// 	freopen("Asmall.in","r",stdin);
// 	freopen("A.txt","w",stdout);
	scanf("%d",&T);
	for (int iCase=1; iCase<=T; ++iCase)
	{
		Node * root = new Node;
		root->dir_name = "/";
		int N,M;
		cin>>N>>M;
		char line[10001];
		char* d = "/";
		for (int i = 0; i<N; ++i)
		{
			cin>>line;
			char *p;
			p = strtok(line,d);
			Node* pa = root;
			Node* pb ;
			while (p){
				string t(p);
				pb = Exist(pa,t);
				if (pb == NULL)
					pb = Create(pa,t);
				pa = pb;
				p=strtok(NULL,d);
			}
		}
		int cnt = 0;
		for (int i = 0; i<M; ++i)
		{
			cin>>line;
			char *p;
			p = strtok(line,d);
			Node* pa = root;
			Node* pb ;
			while (p){
				string t(p);
				pb = Exist(pa,t);
				if (pb == NULL){
					pb = Create(pa,t);
					++cnt;
				}
				pa = pb;
				p=strtok(NULL,d);
			}
		}
		printf("Case #%d: %d\n",iCase,cnt);
	}	
}
