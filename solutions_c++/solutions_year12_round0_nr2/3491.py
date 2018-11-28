#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <fstream>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

#define S(X) ((int)(X.size()))
#define LENGTH(X) ((int)(X.length()))
#define MP(X,Y) make_pair(X,Y)
#define two(X) (1<<(X))
#define twoL(X) (((ull)(1))<<(X))

const double pi=acos(-1.0);
const double eps=1e-11;

template<class T> inline T sqr(T x){return x*x;}

void ck(int b,int &s,int &k)
{
        if(b<2) ++k;
        else
            if(b<3 && s) --s,++k;
}

int main()
{
    //ifstream f("input.txt");
    //ofstream u("output.txt");
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int T,i,n,j,k,s,p,b;
    cin>>T;
    for(i=0;i<T;++i){
        cin>>n>>s>>p;
        k=0;
        for(j=0;j<n;++j){
            cin>>b;
            if(b>=p) ck(p-(b-p)/2,s,k);
        }
        cout<<"Case #"<<i+1<<": "<<k<<endl;
    }
}
