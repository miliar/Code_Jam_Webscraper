#include <iostream>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <vector>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
using namespace std;

#define FOR(A, I, B) for(int A = (int)I; A < (int)B; A++)
#define SZ(A) (int)(A).size()
#define vs vector<string>
#define vi vector<int>
#define pb push_back
#define pii pair<int, int>
#define ll long long
#define ERRO 1e-12
#define DEQ(X,Y) ( fabs((X) - (Y)) < ERRO)

int p; // log teams = p
int teams;
int m[1<<11];
int prices[1<<16];
int resp = 0;

struct node {
    node(int _l, int _r){
        l = _l;
        r = _r;
        left = NULL;
        right = NULL;
        bought = false;
    }
    bool bought;
    int l, r;
    node * left, * right;
};

node * head;

void buy(node * h, int team, int see)
{
    if(see == 0) return;
    
    if(!h->bought)
        resp++;
    
    h->bought = true;

    see--;

    if(h->left == NULL) return;

    if(team >= h->left->l && team <= h->left->r)
        buy(h->left, team, see);
    else 
        buy(h->right, team, see);
}

void construct(node * h)
{
    if(h->r == h->l + 1)
        return;
    int mid = (h->l + h->r)/2;
    h->left = new node(h->l, mid);
    h->right = new node(mid + 1, h->r);
    construct(h->left);
    construct(h->right);
}

int solve()
{
    head = new node(0, teams - 1);
    construct(head);
    resp = 0;
    FOR(i, 0, teams){
        buy(head, i, p - m[i]);     
    }
    return resp;
}

int main()
{
    int cases;
    scanf("%d", &cases);
    FOR(testcase, 0, cases){
        scanf("%d", &p);
        teams = 1<<p;
        FOR(i, 0, teams)
            scanf("%d", &m[i]);
        int lixo;
        FOR(i, 0, teams - 1) scanf("%d", &lixo);

        printf("Case #%d: %d\n", testcase + 1, solve());
    }
    return 0;
}

