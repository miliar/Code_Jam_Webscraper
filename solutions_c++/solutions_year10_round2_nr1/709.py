#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <complex>
#include <climits>
#include <queue>
#include <ctime>
#include <ext/numeric>
#include <ext/hash_map>
#include <ext/hash_set>

using namespace std;
using namespace __gnu_cxx;

#define PB push_back
#define ALL(x) (x).begin(),(x).end()
#define rep(i,x,n) for(int i = (x) ; i < (n) ; ++i)
#define repit(it,x,n) for(__typeof(x) it = (x) ; it!=(n) ;++it)


int res=0;

struct node{
    map<string,node*> child;
    
    void insert(deque<string>&nod,const int&fl=0){
        if(nod.size()==0)
            return;
        if(child.count(nod.front())==0)
        {
            child[nod.front()]=new node();
            if(fl)
                res++;
        }
        string s= nod.front();
        nod.pop_front();
        child[s]->insert(nod,fl);
    }
};

void parse(const string&s,deque<string>&names)
{
    int ind = 0;
    string cur = "";
    while(ind<s.size()){
        if(s[ind] == '/'){
            ind++;
            while(ind<s.size()&&s[ind]!='/')
                cur+=s[ind],ind++;
            names.PB(cur);
            cur="";
        }
    }
}

char a[1000001];

int main()
{
    int t,tt,n,m;
    freopen("in.in","rt",stdin);
    freopen("out.out","wt",stdout);
    scanf("%d",&t);
    rep(tt,0,t){
        scanf("%d %d ",&n,&m);
        node*tree = new node();
        res=0;
        rep(i,0,n){
            gets(a);
            deque<string> names;
            parse(a,names);
            tree->insert(names);
        }
        rep(i,0,m){
            gets(a);
            deque<string>names;
            parse(a,names);
            tree->insert(names,1);
        }
        printf("Case #%d: %d\n",tt+1,res);
    }
    return 0;
}


