#include <algorithm>
#include <iostream>
#include <string>
#include<sstream>
#include<string.h>
#include <cstdio>
#include <vector>
#include <bitset>
#include <cmath>
#include <queue>
#include<stack>
#include <set>
#include <map>
#include<ctime>
#include "euler.h"

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef pair<double,double> pdd;
typedef unsigned long long ull;

#define FOR(i,a,b) for (int i(a); i < (b); i++)
#define REP(i,n) FOR(i,0,n)
#define SORT(v) sort((v).begin(),(v).end())
#define UN(v) sort((v).begin(),(v).end()),v.erase(unique(v.begin(),v.end()),v.end())
#define CL(a,b) memset(a,b,sizeof(a))
#define pb push_back

int main()
{
    long long i,j,answer,max,min,n,m,pD,pG,g,k;
    cin>>m;
    for (i=0;i<m;i++)
    {
        cin>>n>>pD>>pG;
        if (pD!=0) g=gcd(100,pD);
        else g=0;
        if (pD!=0) min=100/g;
        else min=1;
        max=min-(min*pD/100);
        k=n-min;
        /*cout<<g<<" ";
        cout<<min<<" ";
        cout<<max<<" ";*/
        if ((k<0) || ((max>0) && (pG==100)) || ((min-max>0) && (pG==0)))
        {
            cout<<"Case #"<<i+1<<": Broken"<<endl;
        }
        else
        {
            cout<<"Case #"<<i+1<<": Possible"<<endl;
        }
    }
}
