#include <iostream>
#include <iomanip>
#include <sstream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <ctime>

#define MAX 32

using namespace std;
FILE *in; FILE *out;

struct Node
{
	int wordEndFlag;
	Node* next[MAX];
	
	Node()
	{
		wordEndFlag = 0;
		for (int i=0; i<MAX; i++) next[i] = NULL;
	}
};
Node root;


int numWords, wordLen, numTests;
vector < vector <char> > v;

void buildTree()
{
	char curWord[MAX];
	for (int i=0; i<numWords; i++)
	{
		fscanf(in, "%s", curWord);
		
		Node* cur = &root;
		for (int c=0; c<wordLen; c++)
		{
			if (cur->next[curWord[c]-'a'] == NULL)
				cur->next[curWord[c]-'a'] = new Node;
			
			cur = cur->next[curWord[c]-'a'];
		}
		cur->wordEndFlag = 1;
	}
}

int query(int index, Node* cur)
{
	if (index == wordLen)
		return cur->wordEndFlag;
	
	int ans = 0;
	for (int i=0; i<(int)v[index].size(); i++)
		if (cur->next[v[index][i]-'a'] != NULL)
			ans += query(index + 1, cur->next[v[index][i]-'a']);
	return ans;
}

int main(void)
{
	in = fopen("AlienLanguage.in", "rt");
	out = fopen("AlienLanguage.out", "wt");
	unsigned startTime = clock();
	
	fscanf(in, "%d %d %d", &wordLen, &numWords, &numTests);
	buildTree();

	char curWord[MAX*MAX];
	for (int test = 1; test <= numTests; test++)
	{
		cout << "Working on test " << test << "..." << endl;
		
		fscanf(in, "%s", curWord);
		int pos = 0; v.clear();
		for (int i=0; i<wordLen; i++)
		{
			vector <char> add;
			if (isalpha(curWord[pos]))
				add.push_back(curWord[pos++]);
			else
			{
				pos++;
				while (isalpha(curWord[pos]))
					add.push_back(curWord[pos++]);
				pos++;
			}
			v.push_back(add);
		}
		fprintf(out, "Case #%d: %d\n", test, query(0, &root));
	}
	fprintf(stdout, "Finished input for %.3lf sec.\n", (double)(clock() - startTime) / (double)CLOCKS_PER_SEC);
	system("pause");
	
	return 0;
}
