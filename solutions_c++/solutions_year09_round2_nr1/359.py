#include <cstdio>
#include <string>
#include <set>
#include <vector>
using namespace std;
class tree
{
    public:
    string feat;
    long double w;
    tree* first;
    tree* second;
        tree()
        {
            first = second = NULL;
        }

    void print()
    {
        printf("( %Lf",w);
        if(first!=NULL)
        {
            printf(" %s\n",feat.c_str());
            first->print();
            second->print();
        }
        printf(")");
    }
    long double eval(set<string>& traits)
    {
        if(first == NULL)
            return w;
        if(traits.find(feat)!=traits.end())
            return first->eval(traits)*w;
        else
            return second->eval(traits)*w;
    }
};

tree* parse()
{
    tree* node = new tree;
    scanf(" %Lf",&node->w);
    char c;
    scanf(" %c",&c);
    if(c==')')
    {
        return node;
    }
    while(c >= 'a' && c <= 'z')
    {
        node->feat += c;
        scanf(" %c",&c);
    }
    node->first = parse();
    scanf(" %c",&c);
    node->second = parse();
    scanf(" %c",&c);
    return node;
}
int main()
{
    char c;
    int n;
    scanf("%d",&n);
    for(int i=1;i<=n;i++)
    {
        printf("Case #%d:\n",i);
        scanf("%*d");
        scanf(" %c",&c);
        tree* p = parse();
        int ans;
        scanf(" %d",&ans);
        for(;ans--;)
        {
            char an[1000];
            scanf(" %s",an);
            set<string> traits;
            int t;
            scanf(" %d",&t);
            for(int k=0;k<t;k++)
            {
                char tr[1000];
                scanf(" %s",tr);
                traits.insert(string(tr));
            }
            printf("%.7Lf\n",p->eval(traits));
        }

    }

}
