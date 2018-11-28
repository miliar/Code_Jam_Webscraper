#include <iostream>
//#include <stdio.h>
using namespace std;
class Tree
{
public:
    double prob;
    string feature;
    Tree* left;
    Tree* right;
    Tree* parent;
    
    Tree(Tree* parent)
        {
            this->prob = 0;
            this->feature = "";
            this->parent = parent;
            left = NULL;
            right = NULL;
        }
};
int len;
string features[105];

double cal(Tree* node)
{
    double p = node->prob;
    if (node->feature != ""){
        bool q = false;
        for (int i=0;i<len;++i)
            if (node->feature == features[i])
                q = true;
        if (q) p = p*cal(node->left);
        else p = p*cal(node->right);
    }
    return p;
}

int main()
{
    int inputs;
    cin>> inputs;
    for (int i = 0;i<inputs; ++i)
    {
        int n;
        cin >> n;
        char t;
        string feature;
        Tree* root = new Tree(NULL);
        Tree* trans = root;
        
        do{
            t = cin.get();
            if (t==' ' || t=='\n')
                continue;
            if (t=='('){
                if (trans->left == NULL){
                    trans->left = new Tree(trans);
                    trans = trans->left;
                }
                else{
                    trans->right = new Tree(trans);
                    trans = trans->right;
                }
                cin >> trans->prob;
            }
            else if (t==')')
                trans = trans->parent;
            else trans->feature = trans->feature+t;
            //cout<< (trans!=root) <<" "<< ((root->left)!=NULL) <<endl;
            
        } while (trans!=root || (root->left)==NULL);

        cout<<"Case #"<<i+1<<": "<<endl;
        
        cin >> n;
        for (int j = 0; j<n; ++j){
            string temp;
            
            cin>>temp>>len;
            for (int k=0; k<len; ++k)
                cin>>features[k];
            trans = root->left;
            double p = cal(trans);
            printf("%.7f\n",p);
            
        }
    }
    
}

