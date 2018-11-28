// testcpp.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include "windows.h"


#include "stdio.h"
#include "stdlib.h"
#include "signal.h"
#include "process.h"
#include "malloc.h"

#include "fstream"
#include "list"
#include "vector"
#include "algorithm"
#include "time.h"

#include "queue"
#include "stack"

using namespace std;


typedef unsigned __int64 uint64;

typedef struct Node
{
Node * child, *sibling;
char name[105];

Node(char* n)
{
	strcpy(name, n);
	child = sibling = 0;
}

} Node;

Node * root = 0;

int ins1(char * nm)
{
	int ret = 0;
	char *ps = nm+1;
	char tmp[105] = {0};

	Node * pre = root;
	Node * cur = root;

	while (*ps){
		int k = 0;		
		while (*ps != '/' && *ps)
		{
			tmp[k++] = *ps++;
		}
		tmp[k] = 0;

		if (k)
		{
			pre = cur;
			cur = cur->child;
			if (!cur){
				++ret;
				cur = pre->child = new Node(tmp);
			}
			else 
			{
				while (cur && strcmp(cur->name, tmp))
				{
					pre = cur;
					cur = cur->sibling;
				}
				if (!cur){ cur = pre->sibling = new Node(tmp); ++ret;}
			}

		}
		if (*ps) ps++;
	}

	return ret;
}

int main()
{
	char tmp[105];

	int T;
	cin >> T;

	int M, N;
	for(int t = 1; t <= T; ++t)
	{
		int cnt = 0;
		cin >> N >> M;
		cout << "Case #" <<t <<": ";

		root = new Node("/");

		for (int i =0; i < N; ++i)
		{
			memset(tmp,0,sizeof tmp);
			cin >> tmp;
			ins1(tmp);
		}

		for (int i =0; i < M; ++i)
		{
			memset(tmp,0,sizeof tmp);
			cin >> tmp;
			cnt+=ins1(tmp);
		}
		cout << cnt;
		if (t < T)
			cout << endl;
	}


	return 0;
} 