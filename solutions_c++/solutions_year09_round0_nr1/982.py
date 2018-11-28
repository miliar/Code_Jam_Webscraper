#include <iostream>
#include <cstdlib>
#include <string>
#include <algorithm>
#include <numeric>
#include <sstream>
#include <complex>
#include <cmath>
#include <deque>
#include <stack>
#include <queue>
#include <ctime>
#include <list>
#include <map>
#include <set>
using namespace std;

typedef long long ll;

const int INF=0x3C3C3C3C;
#define mset(a,x) memset(a,x,sizeof(a))
#define Abs(a) ((a) >= 0 ? (a) : -(a))
#define dbg(x) cerr<<#x<<" : "<<x<<endl
#define For(I,N) for(int I=0;I<(N);I++)
#define For2(I,A,B) for(int I=(A); (A)<=(B)?(I<=(B)):(I>=(B)); (A)<=(B)?(I++):(I--))
#define ArrSize(x) (sizeof(x)/sizeof(x[0]))

template<class T> void In(T& x){cin>>x;}
template<class T> void In(T arr[], int n){for(int i=0;i<n;i++)cin>>arr[i];}
template<class T> void Out(T arr[], int n){ if(n>0) { cout<<arr[0]; for(int i=1;i<n;i++)cout<<" "<<arr[i];  cout<<endl;} }
ll gcd(ll a,ll b){ll r;while(b){r=a%b;a=b;b=r;}return a;}

struct TrieNode
{
    TrieNode* child[128];
    int flag;

    TrieNode():flag(0)
    {
        memset(child,0,sizeof(child));
    }
};

TrieNode* root;

void Insert(TrieNode* root, const char* str)
{
    TrieNode* p = root;
    const char* q = str;
    for( ; *q; ++q)
    {
        if(p->child[*q] == NULL)
        {
            p->child[*q] = new TrieNode();                
        }
        p = p->child[*q];
    }
    p->flag = 1;
}

struct QNode
{
    TrieNode* p;
    int d;
    QNode(){}
    QNode(TrieNode* pp, int dd)
    {
        p = pp;
        d = dd;
    }
};

int L,D,N;

int main()
{
    int kcase = 0;
    In(L);
    In(D);
    In(N);
    root = new TrieNode();
    string buf;
    For(i,D)
    {
        In(buf);
        Insert(root,buf.c_str());
    }

    For(i,N)
    {
        In(buf);
        const char* pbuf = buf.c_str();
        vector<char> V[20];
        int d = 0;
        int lock = 0;
        for(int i = 0;pbuf[i];i++)
        {
            if(pbuf[i]=='(')lock = 1;
            if(pbuf[i]==')')lock = 0;
            V[d].push_back(pbuf[i]);
            if(!lock) d++;
        }

        ll res = 0;

        queue<QNode> Q;
        QNode qnode(root,0);
        Q.push(qnode);

        while(!Q.empty())
        {
            qnode = Q.front();
            Q.pop();
            
            int d = qnode.d;
            for(int i = 0;i<V[d].size();i++)
            {
                char next = V[d][i];
                if(qnode.p->child[next])
                {
                    if(qnode.p->child[next]->flag)
                    {
                        res++;
                    }
                    Q.push(QNode(qnode.p->child[next], d+1));
                }
            }
        }

        cout<<"Case #"<<++kcase<<": "<<res<<endl;
    }
}
