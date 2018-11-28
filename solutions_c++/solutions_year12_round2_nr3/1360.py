#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <map>
#include <cstdio>
#include <set>
#include <ctime>
#include <queue>
#include <climits>
#include <iomanip>
#include <iterator>
#define LOCAL
#ifdef ONLINE_JUDGE
#undef LOCAL
#endif
 
#ifdef LOCAL
#define cin in
#define cout out
#endif
#define FOREACH(i, n) for (typeof(n.begin()) i = n.begin(); i != n.end(); ++i)
#define MEMSET(p, c) memset(p, c, sizeof(p))
 
using namespace std;
map<int,int> m;
ofstream out;
 
bool bfs(vector<int> &v,int c,int tot,int precedent,bool modif)
{
    if(c<5)
    printf("%d %d %d\n",c,tot,(modif?1:0));
    if(m.find(tot)!=m.end())
    {
        if(c<5)
        printf("tot trouve\n");
    }
    if(m.find(tot)!=m.end()&&modif==true)
    {
        int tot2=tot;
        while(m[tot2]!=-1)
        {
            cout<<m[tot2]<<" ";
            tot2=tot2-m[tot2];
        }
        cout<<endl<<precedent<<" ";
        tot=tot-precedent;
        while(m[tot]!=-1)
        {
            cout<<m[tot]<<" ";
            tot=tot-m[tot];
        }
        return true;
    }
    m[tot]=precedent;
    if(c>=v.size())
        return false;
    if(bfs(v,c+1,tot+v[c],v[c],true))
        return true;
    if(bfs(v,c+1,tot,precedent,false))
        return true;
    return false;
}
 
int main()
{
#ifdef LOCAL
    ifstream in("input.txt");
    out.open("output.txt");
#endif
    int nb_cas;
    cin>>nb_cas;
    for(int c=0;c<nb_cas;c++)
    {
        int n;
        cin>>n;
        vector<int> v(n);
        for(int c2=0;c2<n;c2++)
            cin>>v[c2];
        cout<<"Case #"<<c+1<<": "<<endl;
        m.clear();
        if(!bfs(v,0,0,-1,false))
            cout<<"Impossible";
        cout<<endl;
    }
}
