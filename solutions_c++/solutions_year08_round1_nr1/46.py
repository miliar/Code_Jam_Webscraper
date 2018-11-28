#include	<cstdio>
#include	<cstdlib>
#include	<cstring>
#include	<string>
#include	<vector>
#include	<cmath>
#include	<algorithm>
#include	<cassert>
#include	<set>
#include	<map>
#include	<queue>
#include	<iostream>
#include <fstream>
using namespace std;
#define pb push_back
#define REP(i,n) for(int i=0;i<(n);i++ ) 

typedef long long LL;
typedef pair<int,int> piii;

int a[10000],b[1000];

int main()
{
        int T;
        cin>>T;
        REP(t,T)
        {
                int n;
                cin>>n;
                REP(i,n)
                        cin>>a[i];
                REP(i,n)
                        cin>>b[i];
                LL res=0;
                sort(a,a+n,less<int>());
                sort(b,b+n,greater<int>());
                REP(i,n)
                        res+=LL(a[i])*b[i];
                cout<<"Case #"<<t+1<<": "<<res<<endl;
        }
}
