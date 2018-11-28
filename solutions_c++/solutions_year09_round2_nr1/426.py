#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <string>
#include <stack>
#include <vector>
using namespace std;

int TestN;


class TreeNode
{
public:
	TreeNode() { name = ""; weight = 1.0; Left = Right = 0;}
	TreeNode(string _name, double _weight): name(_name), weight(_weight) { Left = Right = 0; }

	TreeNode(string _name, double _weight, TreeNode *l, TreeNode *r): name(_name), weight(_weight) { Left = l; Right = r; }

	string name;
	double weight;
	TreeNode *Left, *Right;
};

char buf[2048];

TreeNode *ReadNode(void)
{
	int c = getc(stdin);
	while(c!=EOF && c!= '(') c = getc(stdin);

	double p;
	char feature[128];
	int j = 0;
	scanf("%lf", &p);
	c = getc(stdin);
	while(c!=EOF && (c==' ' || c =='\n' || c== '\t')) c = getc(stdin);
	feature[0] = c;

	if(feature[0] == ')')
	{
		return new TreeNode("", p);
	}
	else
	{
		ungetc(c, stdin);
		scanf("%s", &feature[0]);

		TreeNode *l = ReadNode(), 
				 *r = ReadNode();

		int c = getc(stdin);
		while(c!=EOF && c!= ')') c = getc(stdin);

		return new TreeNode(feature, p, l, r);
		
	}
}

FILE *f;
int main(void)
{
	f = stdin;
	//freopen("input.txt", "rt", stdin);
	//freopen("A-small-attempt0.in", "rt", stdin);
	//freopen("A-small-attempt1.in", "rt", stdin);
	freopen("A-large.in", "rt", stdin);
	
	freopen("outputA.txt", "wt+", stdout);
	scanf("%d", &TestN);
	for(int Test = 0; Test < TestN; Test++)
	{
		int L;
		printf("Case #%d:\n", Test+1);
		scanf("%d\n", &L);

		stack<TreeNode *> TreeStack;
		TreeNode *root = ReadNode();
		scanf("%d\n", &L);

		for(int i = 0; i < L; i++)
		{
			int featuresNum;
			vector<string> Features;
			scanf("%s", buf);
			scanf("%d", &featuresNum);
			Features.reserve(featuresNum);
			for(int j = 0; j < featuresNum; j++)
			{
				scanf("%s", buf);
				Features.push_back(string(buf));
			}
			TreeNode *cur = root;
			double p = 1.0;

			do
			{
				p *= cur->weight;
				if(cur->name == string("")) break;
				bool found = false;
				for(int j = 0; j < featuresNum; j++)
				{
					if(Features[j] == cur->name)
					{
						cur = cur->Left;
						found = true;
						break;
					}
				}
				if(!found)
				{
					cur = cur->Right;
				}
			}
			while(cur);
			printf("%.6lf\n", p);
		}

	}
	return 0;
}