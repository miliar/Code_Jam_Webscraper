#include <iostream>
#include <string>
#include <cassert>
#include <set>
#include <cstdio>

using namespace std;

char dummy;

class node
{
public:

    string feature;
    node *yes, *no;
    double weight;

    static node *read()
    {
        node *n = new node();

        cin >> ws;
        assert(cin.peek() == '(');
        cin >> dummy;
        cin >> n->weight;

        cin >> ws;
        if (cin.peek() == ')')
        {
            n->feature = "";
            n->yes = NULL;
            n->no = NULL;
        }
        else
        {
            cin >> n->feature;
            n->yes = read();
            n->no = read();
        }

        assert(cin.peek() == ')');
        cin >> dummy >> ws;

        return n;
    }

    ~node()
    {
        if (yes != NULL)
            delete yes;
        if (no != NULL)
            delete no;
    }
};

int main()
{
    int n;
    cin >> n;
    for (int caseNum = 1; caseNum <= n; caseNum++)
    {
        int l;
        cin >> l;

        node *tree = node::read();

        printf("Case #%d:\n", caseNum);

        int a;
        cin >> a;
        for (int i = 0; i < a; i++)
        {
            int featureCount;
            string animal;
            cin >> animal >> featureCount;
            set<string> features;
            for (int j = 0; j < featureCount; j++)
            {
                string feature;
                cin >> feature;
                features.insert(feature);
            }

            node *cur = tree;
            double cute = 1;
            while (cur != NULL)
            {
                cute *= cur->weight;
                if (cur->feature == "")
                    break;
                if (features.find(cur->feature) != features.end())
                    cur = cur->yes;
                else
                    cur = cur->no;
            }

            printf("%.7f\n", cute);
        }

        delete tree;
    }

    return 0;
}
