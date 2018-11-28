#include <iostream>
#include <cstdlib>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <set>

using namespace std;

typedef struct
{
    string name;
    set <string> features;
} ANIMAL;

struct _DECISION_TREE;

typedef struct _DECISION_TREE
{
    double weight;
    char feature[256];
    _DECISION_TREE *left, *right;
} DECISION_TREE;

DECISION_TREE *root=0;
double p;

void calculate(DECISION_TREE *dtree, ANIMAL a)
{
    p*=dtree->weight;
    if(dtree->left!=0 && dtree->right!=0)
    {
        if(a.features.find(dtree->feature)!=a.features.end()) calculate(dtree->left, a);
        else calculate(dtree->right, a);
    }
}

DECISION_TREE *get_decision_tree(string tree_str)
{
    DECISION_TREE *tree=(DECISION_TREE*)malloc(sizeof(DECISION_TREE));
    if(root==0) root=tree;
    int i=0;
    while(tree_str[i]!='(') i++;
    istringstream sin(tree_str);
    sin.seekg(i+1);
    double weight;
    sin >> weight;
    tree->weight=weight;
    i=sin.tellg();
    while(tree_str[i]==' ') i++;
    if(tree_str[i]==')')
    {
        tree->left=0;
        tree->right=0;
        return tree;
    }
    else
    {
        string feature;
        sin.seekg(i);
        sin >> feature;
        strcpy(tree->feature, feature.c_str());
        while(tree_str[i]!='(') i++;
        tree->left=get_decision_tree(tree_str.substr(i, tree_str.size()-i));
        i++;
        int in_count=1;
        while(in_count!=0)
        {
            if(tree_str[i]=='(') in_count++;
            if(tree_str[i]==')') in_count--;
            i++;
        }
        while(tree_str[i]!='(') i++;
        tree->right=get_decision_tree(tree_str.substr(i, tree_str.size()-i));
        return tree;
    }
}

int main()
{
    int N;
    ifstream fin("a-input.in");
    ofstream fout("a-output.out");
    fin >> N;
    for(int i=0; i<N; i++)
    {
        string tree;
        int L, A;
        fin >> L;
        fin.get();
        string line;
        for(int j=0; j<L; j++)
        {
            getline(fin, line);
            tree+=line+" ";
        }
        root=0;
        get_decision_tree(tree);
        DECISION_TREE *dtree=root;
        fin >> A;
        vector <ANIMAL> animals;
        for(int j=0; j<A; j++)
        {
            ANIMAL a;
            string name;
            fin >> name;
            int n;
            fin >> n;
            a.name=name;
            for(int k=0; k<n; k++)
            {
                string feature;
                fin >> feature;
                a.features.insert(feature);
            }
            animals.push_back(a);
        }
        fout << "Case #" << i+1 << ":" << endl;
        for(int j=0; j<A; j++)
        {
            p=1.0;
            calculate(dtree, animals[j]);
            fout << (double)p << endl;
        }
    }
    fin.close();
    fout.close();
    return 0;
}
