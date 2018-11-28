#include "stdio.h"
#include "stdlib.h"
#include "string.h"


class CTree
{
public:
	int nCnt;
	CTree *subTree[26];
	CTree()
	{
		nCnt = 0;
		for (int i=0;i<26;++i)
			subTree[i] = 0;
	}
};

CTree root;

void add(char *line, CTree *pNode)
{
	int index = line[0]-'a';
	++pNode->nCnt;
	if (line[1] != 0)
	{
		if (pNode->subTree[index] == 0)
			pNode->subTree[index] = new CTree();
		add(line+1, pNode->subTree[index]);
	}
}

int solve(char *line, CTree *pNode)
{
	int nRes = 0;
	if (pNode == 0)
		return 0;
	if (line[0]==0 || line[0]==0x0A || line[0]==0x0D)
	{
		return pNode->nCnt;
	}
	if (line[0]=='(')
	{
		char a[26];
		int n = 0;
		++line;
		while(line[0]!=')')
		{
			a[n]=line[0]-'a';
			++n;
			++line;
		}
		++line;
		for (int i=0;i<n;++i)
		{
			nRes += solve(line, pNode->subTree[a[i]]);
		}
	}
	else
	{
		nRes += solve(line+1,pNode->subTree[line[0]-'a']);
	}
	return nRes;
}

void main()
{
	FILE *fin,*fout;
	int i;
	int l,d,n;
	char line[1024];
	fopen_s(&fin, "A-large.in", "rt");
	fopen_s(&fout, "A-large.out", "wb");

	fscanf_s(fin,"%d %d %d\n", &l, &d, &n);
	for (i=0;i<d;++i)
	{
		fgets(line, 1024, fin);
		add(line, &root);
	}
	for (i=0;i<n;++i)
	{
		fgets(line, 1024, fin);
		fprintf(fout, "Case #%d: %d\n", i+1, solve(line,&root));
	}
	fclose(fin);
	fclose(fout);
}