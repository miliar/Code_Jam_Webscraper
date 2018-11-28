// park.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "stdio.h"
#include "stdlib.h"
#include <vector>
#include <map>

using std::vector;
using std::map;

class Node
{
public:
	int num;
	Node* next;
};

int _tmain(int argc, _TCHAR* argv[])
{
	FILE* fin = fopen("b.in","r");
	FILE* fout = fopen("b.out","w");
	int line;
	fscanf(fin,"%d\n",&line);
	for(int i = 0; i < line; i++)
	{
		int r, k, n;
		fscanf(fin,"%d %d %d\n",&r, &k, &n);
		Node* phead = new Node();
		Node* pcurrent = phead;
		for(int j = 0; j < n; j++)
		{
			int num;
			if(j != n-1)
				fscanf(fin,"%d",&num);
			else
				fscanf(fin,"%d\n",&num);

			if(j != 0)
			{
				pcurrent->next = new Node();
				pcurrent = pcurrent->next;
			}
			pcurrent->num = num;
		}
		pcurrent->next = phead;
		pcurrent = phead;
		
		vector<int> count;
		count.push_back(0);
		map<Node*, int> nodemap;

		int round = r;
		bool found = false;
		Node* pfound = NULL;
		while(round != 0)
		{
			if(k < pcurrent->num)break;

			int remain = k;
			Node* pfirst = pcurrent;
			while(remain >= pcurrent->num)
			{
				remain -= pcurrent->num;
				pcurrent = pcurrent->next;
				if(pcurrent == pfirst)break;
			}
			count.push_back(k - remain + count.back());
			round --;
			map<Node*, int>::iterator it = nodemap.find(pcurrent);
			if(it != nodemap.end())
			{
				pfound = pfirst;
				found = true;
			}else{
				nodemap[pfirst] = count.size() - 1;
			}
		}

		if(round == 0 || !found)
		{
			fprintf(fout,"Case #%d: %d\n",i+1,count.back());
		}else{
			int begin = nodemap[pfound];
			int index = (r-begin) % (count.size() - 1);
			int result = ((r-begin)/(count.size() - 1)) * count.back() + count[index] + count[begin];
			fprintf(fout,"Case #%d: %d\n",i+1,result);
		}
	}
	return 0;
}

