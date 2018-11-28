#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <map>
#include <algorithm>
#include <set>
#include <sstream>
using namespace std;

int n, m, cc;

typedef struct node {
    string name;
    vector <node> child;
    node (string st){name = st; child.clear();}
};

node root("/");

void add_dir(istringstream iss, node &dir){
    string s;
    if (iss >> s) {
        cout<<dir.name<<" "<<dir.child.size()<<endl;
        
        bool found = false;
        for (int i =0;i<dir.child.size();i++){
            cout<<"'"<<dir.child[i].name<<"'"<<endl;
            if (dir.child[i].name == s) {
 //               add_dir(iss, dir.child[i]);
                found = true;
                break;
            }
        }
        if (!found){
            node tmp(s);
            dir.child.push_back(tmp);
            cc++;
  //          add_dir(iss, tmp);
        }
    }
}

void add(string st){
    for(int i=0;i<st.length();i++)
        if (st[i] == '/') st[i] = ' ';
//    cout<<" ADD "<<st<<endl;
    istringstream iss(st);

//    add_dir(iss, root);

    string s;
    node *dir = &root;
    while (iss >> s){
 //       cout<<" -- DIR "<<s<<endl;
        bool found = false;
 //       cout<<"CUR DIR: "<<dir->name<<" "<<dir->child.size()<<endl;
        for (int i =0;i<dir->child.size();i++){
            if (dir->child[i].name == s) {
                dir = &dir->child[i];
                found = true;
                break;
            }
        }
  //      cout<<" -- -- FOUND "<<found<<endl;
        if (!found){
            // new child;
            node tmp(s);
            dir->child.push_back(tmp);
            cc++;
            dir = &(dir->child[dir->child.size()-1]);
        }
    }

}

int main(){

    freopen("A-large.in","r",stdin);
    freopen("a.out","w",stdout);

    int ntest;
    cin>>ntest;
    for(int test=1;test<=ntest;test++){
        root.child.clear();
        cc = 0;

        cin>>n>>m;
        string st;
        for (int i=0;i<n;i++){
            cin>>st;
            add(st);
        }
        int exist = cc;
 //       cout<<cc<<endl;
        for (int i=0;i<m;i++){
            cin>>st;
            add(st);
        }
  //      cout<<cc<<endl;
        cout<<"Case #"<<test<<": "<<cc-exist<<endl;
    }

    return 0;
}
