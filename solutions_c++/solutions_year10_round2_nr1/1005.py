#include <map>
#include <set>
#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#define EPS 1e-9
#define EQ(a,b) (fabs((a)-(b)) <= EPS)
using namespace std;

typedef long long int64;

struct Node
{
    map<string, Node*> child;
    string name;
    int exist;
    Node(string n, int e)
    {
        name=n;
        exist=e;
        //clog<<"Creating "<<n<<" with "<<e<<endl;
    }
};

int ans;
void traverse(Node* root)
{
    ans+=root->exist;
    //if(root->exist) cout<<"Create "<<root->name<<endl;
    map<string, Node*>::iterator it;
    for(it=root->child.begin(); it!=root->child.end();it++)
    {
        traverse(it->second);
    }
}

vector<Node*> creations;
int main()
{
    freopen("a-large.in", "r", stdin);
    freopen("a-large.out", "w", stdout);
    int t, c;
    cin>>t;
    for(c=1;c<=t;c++)
    {
        Node root("", 0);
        int no_available, no_need;
        cin>>no_available>>no_need;

        string path;
        getline(cin, path);
        while(no_available--)
        {
            getline(cin, path);
            //clog<<"Got "<<path<<", no_available="<<no_available<<endl;
            int i=0;
            Node *now=&root;
            while(i<path.size())
            {
                int start;
                for(start=++i;i<path.size() && path[i]!='/';i++);
                string dir=path.substr(start, i-start);
                map<string, Node*>::iterator it=now->child.find(dir);
                if(it == now->child.end())
                {
                    Node *n=new Node(dir, 0);
                    creations.push_back(n);
                    now->child[dir]=n;
                    now = n;
                }
                else now=it->second;
            }
        }

        //cout<<no_need<<endl;
        while(no_need--)
        {
            getline(cin, path);
            //clog<<"Got "<<path<<", no_need="<<no_need<<endl;
            int i=0;
            Node *now=&root;
            while(i<path.size())
            {
                int start;
                for(start=++i;i<path.size() && path[i]!='/';i++);
                string dir=path.substr(start, i-start);
                //cout<<"Processing "<<dir<<endl;
                map<string, Node*>::iterator it=now->child.find(dir);
                if(it == now->child.end())
                {
                    Node *n=new Node(dir, 1);
                    creations.push_back(n);
                    now->child[dir]=n;
                    now = n;
                }
                else now=it->second;
            }
        }

        ans=0;
        traverse(&root);
        cout<<"Case #"<<c<<": "<<ans<<endl;
        int i;
        for(i=0;i<creations.size();i++) delete creations[i];
        creations.clear();
    }
	return 0;
}
