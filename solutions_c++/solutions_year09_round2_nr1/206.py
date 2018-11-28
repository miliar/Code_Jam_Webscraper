#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <queue>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>


#define SZ size()
#define PB push_back
#define ALL(v) v.begin(),v.end()
#define MP make_pair
#define x first
#define y second

#define LL long long
#define UI unsigned int
#define ULL unsigned long long
#define PI pair<int,int>
#define PD pair<double,double>
#define PLL pair<LL,LL>
#define PULL pair<ULL,ULL>
#define VI vector<int>
#define VD vector<double>
#define VS vector<string>
#define SI set<int>
#define PQ priority_queue
#define VVI vector<vector<int> >
#define IT iterator

#define ABS(x) (((x)>0)?(x):(-(x)))
#define MIN(a,b) (((a)<(b))?(a):(b))
#define MAX(a,b) (((a)>(b))?(a):(b))
#define sign(a) ((a)>0)-((a)<0)
#define sqr(a) ((a)*(a))
#define Repi(n) for (int i=0; i<n; i++)
#define Repj(n) for (int j=0; j<n; j++)
#define Repk(n) for (int k=0; k<n; k++)
#define F(i,n) for (int i=0;i<n;i++)

#define INF 2000000000
#define EPS 1e-6

#define Time ((double)clock()/CLOCKS_PER_SEC)
#define pause system("pause")

using namespace std;

struct node
{
        double prob;
        string prr;
        string feat;
        node *left;
        node *right;
};

node *root;

void erase(node *tree)
{
    if (tree->left!=NULL)
     {
                erase(tree->left);
                erase(tree->right);
                delete tree->left;
                delete tree->right;
        }
}

void read(node *tree)
{
        int at=0;
        string s;
        char c;
        tree->prr=tree->feat="";
        while(1)
         {
                cin>>c;
               // cout<<c;
                if (at==0)
                 {
                        if ((c>='0' && c<='9') || c=='.')
                         {
                                tree->prr+=c;
                         }
                        else
                         if (tree->prr.SZ)
                         {
                                at=1;
                                istringstream ss(tree->prr);
                                ss>>tree->prob;
                             //   cout<<"\n                 "<<tree->prob<<"\n";
                                if (c>='a' && c<='z')
                                    tree->feat+=c;
                                else
                                 {
                                 //       cout<<"                     ret\n";
                                        tree->left=tree->right=NULL;
                                        return;
                                    }
                         }
                 }
                else
                 {
                        if (c>='a' && c<='z')
                         tree->feat+=c;
                        else
                         {
                                  //  cout<<"\n                   "<<tree->feat<<" ("<<tree->prob<<")\n";
                                    tree->left=new node;
                                    tree->right=new node;
                                    at=2;
                                    read(tree->left);
                                    read(tree->right);
                                    cin>>c;
                                    return;
                            }
                 }
         }
}

set<string> f;

double res(node *tree)
{
        if (tree==NULL) return 1.;
        if (f.find(tree->feat)!=f.end())
         {
           return tree->prob*res(tree->left);
         }
        else
         return tree->prob*res(tree->right);
}

int main()
{
    root=new node;
    int T,L;
    cin>>T;
    F(xx,T)
    {
            cin>>L;
            read(root);
            cout<<"Case #"<<xx+1<<":\n";
            int N;
            
            cin>>N;
           // cout<<"dffdg "<<N<<"\n";
            Repi(N)
             {
                    string s;
                    cin>>s;
                  //  cout<<s<<"\n";
                    int t;
                    cin>>t;
                    f.clear();
                    Repj(t)
                     {
                            cin>>s;
                        //    cout<<"                 feature  "<<s<<"\n";
                            f.insert(s);
                     }
                    // cout<<"\n\n";
                     cout<<setprecision(8)<<fixed<<res(root)<<"\n";
             }
          //  cout<<"\n\n\n\n\n";
            erase(root);
    }
    return 0;
}

