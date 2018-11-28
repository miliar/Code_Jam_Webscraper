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

int main()
{
    //ifstream f("input.txt");
    //ofstream u("output.txt");
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int i,ii,n,jj,k,T,a,b;
    vector <int> v;
    cin>>T;
    for(i=0;i<T;++i){
        cin>>a>>b;
        k=0;
        for(ii=a;ii<=b;++ii)
            for(jj=ii+1;jj<=b;++jj){
                v.clear();
                n=jj;
                while(n) v.push_back(n%10),n/=10;
                for(size_t t=0;t<v.size()/2;++t) swap(v[t],v[v.size()-1-t]);
                while(n!=jj){
                    n=0;
                    int s=v[0];
                    for(size_t t=0;t<v.size()-1;++t) v[t]=v[t+1];
                    v[v.size()-1]=s;
                    for(size_t t=0;t<v.size();++t) n+=v[t],n*=10;
                    n/=10;
                    if(n==ii) ++k;
                }
            }
        cout<<"Case #"<<i+1<<": "<<k<<endl;
    }
}
