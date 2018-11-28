#include <assert.h> 
#include <ctype.h> 
#include <float.h> 
#include <math.h> 
#include <stdio.h> 
#include <string> 
#include <stdlib.h> 
#include <time.h> 
#include <algorithm> 
#include <numeric> 
#include <functional> 
#include <utility> 
#include <vector> 
#include <list> 
#include <set> 
#include <map> 
#include <queue> 
#include <stack> 
#include <sstream> 
#include <iostream> 

using namespace std; 

#define rep(i,n) for(int i=0;i<(n);++i)
#define clr(a,b) memset(a,b,sizeof(a)); 
#define all(c) (c).begin(), (c).end() 
#define inf 1000000000 

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<string> vs;
typedef vector<int> vi;

char line[100000];

struct Node
{
	Node()
	{
		left = right = 0;
	}
	double p;
	string feature;

	Node* left;
	Node* right;
};

Node* parse(char*& pos)
{
	while (*pos != '(')
		pos++;
	
	Node* pNode = new Node();
	pos++;

	while (*pos == ' ')
		pos++;
	
	double p = 0;
	p = *pos - '0';
	pos++; 

	double c = 0.1;
	
	if (*pos == '.')
	{
		pos++;
		while (isdigit(*pos))
		{
			p += c * (*pos - '0');
			c *= 0.1;
			pos ++;
		}
	}
	pNode->p = p;

	while (*pos == ' ')
		pos++;

	if (*pos == ')')
	{
		pos++;
		return pNode;
	}
	while (*pos != ' ' && *pos != '(' && *pos != ')')
	{
		pNode->feature += *pos;
		pos++;
	}

	pNode->left = parse(pos);
	pNode->right = parse(pos);
	return pNode;
}

set<string> features;

double Travel(Node* pNode, double cur)
{
	if (!pNode)
		return cur;

	cur *= pNode->p;

	if (features.find(pNode->feature) != features.end())
		return Travel(pNode->left, cur);

	return Travel(pNode->right, cur);
		

}

int main(int argc, char* argv[])
{
	freopen("Test.in", "r", stdin);
	//freopen("C:\\out", "w", stdout);

	gets(line);
	int caseCount;
	sscanf(line, "%d", &caseCount);

	for (int nCase = 1; nCase <= caseCount; nCase++)
	{
		gets(line);
		int L;
		sscanf(line, "%d", &L);

		string s;

		for (int i = 0; i < L; i++)
		{
			gets(line);			

			s += line;
		}

		char* pos = &s[0];
		Node* root = parse(pos);

		gets(line);
		int Q;
		sscanf(line, "%d", &Q);

		printf("Case #%i:\n", nCase);

		while (Q--)
		{
			gets(line);
			istringstream iss(line);
			string name;
			iss >> name;
			int cnt;
			iss >> cnt;

			features.clear();
			while (cnt--)
			{
				string f;
				iss >> f;
				features.insert(f);
			}

			double p = Travel(root, 1);
			printf("%.7lf\n",p);
		}



		fflush(stdout);
	}


	return 0;
}


