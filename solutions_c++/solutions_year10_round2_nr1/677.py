#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <bitset>

using namespace std;


struct Node{
public:
    Node(){}
    vector<string> vs;
    vector<Node *>next;  
};

vector<string> divide(string str)
{
    char const * p = str.c_str();
    while (*p == '/')   p++;
    vector<string> res;
    while (*p != 0){
        char const * q = p;
        while (*q != '/' && *q != 0){
            q++;
        }
        string xx = string(p,q);
        res.push_back(xx);
        if (*q == 0)
            break;
        while (*q == '/')   q++;
        
        p = q;
        
    }
    return res;
}
int creat_tree(Node *(&root),vector<string> xx,int st)
{
    int res;
    if (st >= xx.size()){
     //   root = NULL;
        return 0;
    }
    if (root == NULL){
        root = new Node();
        root->vs.push_back(xx[st]);
        Node * xnode = NULL;
        res = creat_tree(xnode,xx,st+1)+1;
        root->next.push_back(xnode);
        return res;
    }else{
        int i;
        for (i = 0 ;i < root->vs.size() ;i++){
            if (xx[st] == root->vs[i])
                break;
        }
        if (i < root->vs.size()){
            res = creat_tree(root->next[i],xx,st+1);
        }else{
            root->vs.push_back(xx[st]);
            Node * xnode = NULL;
            res = creat_tree(xnode,xx,st+1)+1;
            root->next.push_back(xnode);
        }
        return res;
    }
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int tt;
    cin >> tt;
    for (int t = 1 ;t <= tt ;t++){
        int n,m;
        cin >> n >> m;
        Node *root = NULL;
        string str;
        for (int i = 0 ;i < n ;i++){
            cin >> str;
            vector<string> vs = divide(str);
         //   for (int j = 0 ;j < vs.size() ;j++)
           //     cout << vs[j] << endl;
            creat_tree(root,vs,0);
        }
        int num = 0;
        for (int i = 0 ;i < m ;i++){
            cin >> str;
            vector<string> vs = divide(str);
            num += creat_tree(root,vs,0);
            //for (int j = 0 ;j < vs.size() ;j++)
             //   cout << vs[j] << endl;
           // cout << "num " << num << endl;
        }
        cout << "Case #" << t << ": " << num  << endl;
    }
}
