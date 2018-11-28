#include <iostream>
#include <iomanip>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <algorithm>
#include <string>

#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <cctype>
#include <climits>

#define NAME_VAL(a) cerr<<#a<<" = "<<(a)<<endl;
#define SWAPi(a,b) { int t=a;a=b;b=t; }
#define SWAPd(a,b) { double t=a;a=b;b=t; }
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))
#define FORab(i,a,b) for(i=(a);i<=(b);i++)
#define FOR(i,n) FORab(i,0,(n)-1)
#define FOR1(i,n) FORab(i,1,n)

using namespace std;

struct NODE{
    int pos;
    int v;
};

void preprocess()
{

}

int mycmp(const void *a,const void *b)
{
    struct NODE *na=(struct NODE *) a;
    struct NODE *nb=(struct NODE *) b;
    return (na->pos)-(nb->pos);
}

void main2(int c) {
    struct NODE nodes[300];
    int n,vn,middle;
    long long d;
    cin>>n>>d;
    int i,j,k;
    vn=0;
    long long inmax=LONG_LONG_MIN;
    long long inmin=LONG_LONG_MAX;
    FOR(i,n)
    {
        cin>>nodes[i].pos>>nodes[i].v;
        vn+=nodes[i].v;
    }
    qsort(nodes,n,sizeof(struct NODE),mycmp);
    long long rpos=0,lpos=0,maxdist=LONG_LONG_MIN;
    int vv=0;
    //int flag=0;
    FOR(i,n)
    {
        if(i==0)
        {
            lpos=nodes[0].pos;
            rpos=nodes[0].pos+((long long)nodes[0].v-1)*d;
            inmax=LONG_LONG_MIN;
            inmin=LONG_LONG_MAX;
        }
        else
        {
            lpos=rpos+d;
            rpos=rpos+((long long)nodes[i].v)*d;
            if(rpos< (long long)nodes[i].pos)
            {
                if(inmax-inmin>maxdist) maxdist=inmax-inmin;
                lpos=nodes[i].pos;
                rpos=nodes[i].pos+((long long)nodes[i].v-1)*d;
                inmax=LONG_LONG_MIN;
                inmin=LONG_LONG_MAX;
            }
        }
        if(inmax< (rpos-nodes[i].pos) ) inmax = (rpos-nodes[i].pos);
        if(inmin> (lpos-nodes[i].pos) ) inmin = (lpos-nodes[i].pos);
    }
    if(inmax-inmin>maxdist) maxdist=inmax-inmin;
    cout<<maxdist/2;
    if(maxdist%2==1) cout<<".5";
    cout<<endl;
}

int main() {
    int c,cases;
    preprocess();
    cin>>cases;
    FOR1(c,cases) {
        cout<<"Case #"<<c<<": ";
        main2(c);
    }
    return 0;
}
