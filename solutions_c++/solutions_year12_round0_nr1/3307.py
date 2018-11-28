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
    char c['z'+1],s[1000];
    c['a']='y';
    c['b']='h';
    c['c']='e';
    c['d']='s';
    c['e']='o';
    c['f']='c';
    c['g']='v';
    c['h']='x';
    c['i']='d';
    c['j']='u';
    c['k']='i';
    c['l']='g';
    c['m']='l';
    c['n']='b';
    c['o']='k';
    c['p']='r';
    c['q']='z';
    c['r']='t';
    c['s']='n';
    c['t']='w';
    c['u']='j';
    c['v']='p';
    c['w']='f';
    c['x']='m';
    c['y']='a';
    c['z']='q';
    int n;
    cin>>n;
    cin.getline(s,999);
    for(int i=0;i<n;++i){
        cout<<"Case #"<<i+1<<": ";
        cin.getline(s,999);
        for(int j=0;j<strlen(s);++j)
         if(s[j]!=' ') cout<<c[s[j]];
         else cout<<" ";
        cout<<endl;
    }
}
