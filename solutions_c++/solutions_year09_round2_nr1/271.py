#include <iostream>

using namespace std;

struct Node
{
	double weight;
	char feature[11];
	Node* t;
	Node* f;
};

char* s[82];
char c;
char animal[11];
char anFeatures[100][11];

void Parse(Node* node, int& linesRead, int l)
{
	node->weight = 0;
	while(c != '(') scanf("%c", &c);
	while((c < '0' || c>'9') && c!='.') scanf("%c", &c);
	bool beforedot = true;
	double dec = 1;
	while((c>='0' && c<='9') || c=='.')
	{
		if(c=='.')
		{
			beforedot = false;
		}
		else
		{
			if(beforedot)
			{
				node->weight*=10;
				node->weight+=c-'0';
			}
			else
			{
				dec/=10;
				node->weight+=dec*(c-'0');
			}
		}
		scanf("%c", &c);
	}
	while((c < 'a' || c>'z') && c!=')') scanf("%c", &c);
	if(c!=')')
	{
		int cc = 0;
		while(c>='a' && c<='z')
		{
			node->feature[cc++] = c;
			scanf("%c", &c);
		}
		node->t = new Node();
		Parse(node->t, linesRead, l);
		node->f = new Node();
		Parse(node->f, linesRead, l);
		while(c != ')') scanf("%c", &c);
	}
	else
	{
		//Terminal Node
		node->t = NULL;
		node->f = NULL;
		node->feature[0] = 0;
	}
	scanf("%c", &c);
}

int main()
{
    FILE* in = freopen("A-large.in", "r", stdin);
    FILE* out = freopen("A-large.out", "w+", stdout);

	int tests = 0;
	cin>>tests;

	for(int t=1; t<=tests;++t)
	{
		int an,l;
		cin>>l;
		Node* root = new Node();
		int linesRead = 0;
		scanf("%c", &c);
		Parse(root, linesRead,l);

		cout<<"Case #"<<t<<":\n";
		cin>>an;
		for(int i=0;i<an;i++)
		{
			scanf("%s",animal);
			int fc;
			cin>>fc;
			for(int j=0;j<fc;j++)
			{
				scanf("%s",anFeatures[j]);
			}
			Node* curNode = root;
			double p = 1;
			while(true)
			{
				p*=curNode->weight;
				if(curNode->feature[0] == 0)
					break;
				bool found = false;
				for(int j=0;j<fc;j++)
				{
					if(0 == strcmp(anFeatures[j], curNode->feature))
					{
						curNode = curNode->t;
						found = true;
						break;
					}
				}
				if(!found)
					curNode = curNode->f;
			}
			printf("%.7f\n", float(p));

			//cout<<p<<"\n";
		}


	}

	//cout<<"Hello world";
	return 0;
}