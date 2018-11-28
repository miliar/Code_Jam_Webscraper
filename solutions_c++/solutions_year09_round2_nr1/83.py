#include <stdio.h>
#include <string>
#include <map>
#include <set>
#include <vector>

struct Tree
{
    Tree()
        : weight(0), id(0), left(0), right(0)
    {
    }

    double weight;
    int id;
    Tree *left, *right;
};

typedef std::map<std::string, int> IDs;
IDs ids;
int nextid;

Tree *readTree()
{
    Tree *res = new Tree;

    char c;
    do
    {
        c = getchar();
    }
    while (c != '(');

    scanf("%lf", &res->weight);

    do
    {
        c = getchar();
    }
    while (c == ' ' || c == '\n' || c == '\r');

    ungetc(c, stdin);
    if (c != ')')
    {
        char feature[100];
        scanf("%s", feature);
        ids[feature] = nextid;
        res->id = nextid++;

        res->left = readTree();
        res->right = readTree();
    }

    do
    {
        c = getchar();
    }
    while (c != ')');

    return res;
}

int main()
{
    std::vector<bool> props(100000);
    int N;
    scanf("%d", &N);
    for (int n = 1 ; n <= N ; ++n)
    {
        printf("Case #%d:\n", n);

        ids.clear();
        nextid = 1;

        int L;
        scanf("%d", &L);
        Tree *dict = readTree();

        int A;
        scanf("%d", &A);
        while (A--)
        {
            props.clear();
            props.resize(nextid);
            char x[100];
            scanf("%s", x);
            int num;
            scanf("%d", &num);
            while (num--)
            {
                scanf("%s", x);
                props[ids[x]] = true;
            }

            Tree *check = dict;
            double p = 1;
            while (check)
            {
                p *= check->weight;
                if (check->id)
                {
                    if (props[check->id])
                        check = check->left;
                    else
                        check = check->right;
                }
                else
                    check = NULL;
            }
            printf("%.7lf\n", p);
        }
    }
    return 0;
}
