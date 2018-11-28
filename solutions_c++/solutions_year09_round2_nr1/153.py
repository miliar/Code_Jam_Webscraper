#include <cstdio>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cstdlib>

#include <iostream>
#include <memory>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <vector>

#define TASK "a"

using namespace std;

#define PB(x) push_back(x)
#define MP(x, y) make_pair(x, y)

typedef long long int64;
typedef unsigned long long unt64;

int T, L, l, tree_len, A;
string tree;
vector< pair< double, string> > node;
vector< pair< int, int> > childs;

int add_node(double t_weight, string t_name, int child1, int child2)
{
    int result = node.size();
    node.PB(MP(t_weight, t_name));
    childs.PB(MP(child1, child2));
    return result;
}

int read_tree()
{
    while (l < tree_len && tree[l] == ' ') l++;

    if (l == tree_len || tree[l] != '(') 
    {
        cerr << "AAA1\n";
        return -1;
    }


    l++;

    int result = -1, first_child = -1, second_child = -1;
    double t_weight;
    string t_name = "";

    sscanf(tree.substr(l).c_str(), "%lf", &t_weight);

    while (l < tree_len && (isdigit(tree[l]) || tree[l] == '.' | tree[l] == ' '))
        l++;
    
    if (tree[l] != '(' && tree[l] != ')')
    {        
        while (l < tree_len && tree[l] != ' ' && tree[l] != '(' && tree[l] != ')')
            t_name = t_name + tree[l], l++;
        while (l < tree_len && tree[l] == ' ')
            l++;
    }

    if (tree[l] == '(')
    {
        first_child = read_tree();
        while (l < tree_len && tree[l] == ' ') 
            l++;

        second_child = read_tree();
        while (l < tree_len && tree[l] == ' ') 
            l++;
    }

    while (l < tree_len && tree[l] == ' ')
        l++;
    
    if (tree[l] != ')')
        cerr << "AAA2\n";
    l++;
    
    result = add_node(t_weight, t_name, first_child, second_child);

    return result;
}

set<string> features;

double dfs(int start)
{
    //printf("come to (%d, %.5lf, %s)\n", start, node[start].first, node[start].second.c_str());
                                                    

    double result = node[start].first;

    if (childs[start].first == -1 || childs[start].second == -1)
        return result;

    if (features.find(node[start].second) != features.end())
        result *= dfs(childs[start].first);
    else
        result *= dfs(childs[start].second);
    return result;
}

int main()
{
    freopen(TASK ".in", "rt", stdin);
    freopen(TASK ".out", "wt", stdout);

    scanf("%d", &T);
    for (int t = 1; t <= T; t++)
    {
        scanf("%d\n", &L);
        tree = "";
        for (int i = 0; i < L; i++)
        {
            char ch;
            while (scanf("%c", &ch) == 1 && ch != '\n')
                tree = tree + ch;
        }

        node.clear();
        childs.clear();
        l = 0;
        tree_len = tree.length();

        int root = read_tree(); 

        scanf("%d", &A);

        printf("Case #%d:\n", t);
        for (int i = 0; i < A; i++)
        {
            int num_f;
            char buf[1000];
            scanf("%s %d", buf, &num_f);
            features.clear();

            for (int j = 0; j < num_f; j++)
            {
                char buf2[1000];
                scanf("%s", buf2);
                features.insert((string) buf2);
            }
            double result = dfs(root);

            printf("%.7lf\n", result);
        }

    }
    return 0;
}

