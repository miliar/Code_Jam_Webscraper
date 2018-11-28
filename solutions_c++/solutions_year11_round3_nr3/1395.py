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
int p[10000]={};
int pn=0;
void preprocess()
{
  /*  int i,j;
    bool flag;
    FORab(i,2,10000)
    {
        flag=true;
        FOR(j,pn)
        {
            if(i%p[j]==0)
            {
                flag=false;
                break;
            }
        }
        if(flag){
        p[pn]=i;
        pn++;
        }
    }*/
}

void main2(int c) {
    int n,l,h;
    int freq[10000];
    int i,j,k;

    cin>>n>>l>>h;
    FOR(i,n) cin>>freq[i];

    int ans=-1;
    bool flag;

    FORab(i,l,h)
    {
        flag=true;
        FOR(j,n)
        {
            if(( (i>freq[j]) && (i%freq[j]==0) ) || ( (i<=freq[j]) && (freq[j]%i==0) ) )
            ;
            else
            {
                flag=false;
                break;
            }
        }
        if(flag==true)
        {
            ans=i;
            break;
        }
    }
    if(ans>0) cout<<ans<<endl;
    else cout<<"NO"<<endl;
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
