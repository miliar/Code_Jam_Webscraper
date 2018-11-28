#include <cstdio>
#include <string>
#include <set>

using namespace std;

class node
{
    public:
        double prob;
        string s;
        node *yes;
        node *no;
};

int n;

void getobrack()
{
    while (true)
        if (getchar() == '(')
            return;
}

bool getcbrack()
{
    while (true)
    {
        char c = getchar();
        if (c == ')')
            return true;
        if (!isspace(c))
        {
            ungetc(c, stdin);
            return false;
        }
    }
}

char cs[100];

node *get_node()
{
    node *ret = new node();

    getobrack();
    scanf("%lf", &ret->prob);

    if (getcbrack())
        ret->s = "";
    else
    {
        scanf("%s", cs);
        ret->s = cs;
        ret->yes = get_node();
        ret->no = get_node();
        if (!getcbrack())
            fprintf(stderr, "ZLE1\n");
    }

    return ret;
}

int main()
{
    scanf("%d", &n);

    for (int casenum = 1; casenum <= n; ++casenum)
    {
        printf("Case #%d:\n", casenum);

        int l;
        scanf("%d", &l);

        node *root = get_node();

        int a;
        scanf("%d", &a);
        while (--a >= 0)
        {
            set<string> features;
            int f;
            scanf("%s%d", cs, &f);

            while (--f >= 0)
            {
                scanf("%s", cs);
                features.insert(cs);
            }

            double prob = 1;
            node *curr = root;

            while (curr->s != "")
            {
                prob *= curr->prob;
                if (features.find(curr->s) != features.end())
                    curr = curr->yes;
                else
                    curr = curr->no;
            }
            prob *= curr->prob;

            printf("%.7lf\n", prob);
        }
    }

    return 0;
}

