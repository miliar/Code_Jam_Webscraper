#include <cstdio>
#include <string>
#include <set>
using namespace std;

int L, A;

struct Node
{
    char f[32];
    double weight;
    Node *l, *r;
}nodes[100000];
int loc;

char buf[1024];

Node* build()
{
    Node* node = nodes + loc++;


    scanf(" ( %lf", &node->weight);
    
    if(scanf(" %[)]", buf) != 1)
    {
	scanf("%s", node->f);
        node->l = build();
	node->r = build();
	scanf(" )");
    }
    else
    {
        node->l = node->r = NULL;
    }
    
    return node;
}

double go(Node* node, set<string>& feat, double p)
{
    if(!node->l)
	    return p * node->weight;
    else if(feat.find(node->f) != feat.end())
	    return go(node->l, feat, p *  node->weight);
    else
	    return go(node->r, feat, p * node->weight);
}

int main()
{
    int T;
    scanf("%d", &T);

    for(int t = 1; t <= T; t++)
    {	
	    printf("Case #%d:\n", t);
        scanf("%d", &L);
	loc = 0;
        Node* root = build();

        scanf("%d", &A);
        while(A--)
	{
            set<string> feat;
	    scanf("%s", buf);
	    int n;
	    scanf("%d", &n);
	    while(n--)
	    {
                scanf("%s", buf);
		feat.insert(buf);
	    }
            printf("%.7lf\n", go(root, feat, 1.0));
	}	
    }


    return 0;
}
