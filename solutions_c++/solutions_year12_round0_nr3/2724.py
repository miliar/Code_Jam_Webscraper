//Bismillahir Rahmanir Rahim
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <cstring>
#include <vector>
#include <stack>
#include <queue>
#include <deque>
#include <bitset>
#include <utility>
#include <set>
#include <map>
#include <cmath>

using namespace std;

#define pi 2.0*acos(0.0)
#define pb push_back
#define MAX 2147483647
#define MIN -2147483647
#define rep(i,n) for(int i(0),_n(n);i<_n;i++)
#define reps(i,s,n) for(int i(s),_n(n);i<_n;i++)
#define mp make_pair


typedef long long ll;
typedef vector<int> VI;
typedef set<int>SI;
typedef pair<int,int>PAR;
typedef vector<PAR>VP;
typedef map<string,int>MSI;

int A,B;

int cycle(int n)
{
    int x=n,p=0;
    while(n>0){
        n/=10;
        p++;
    }

    n=x;
    int ret=0;
    while(1){
        int a = n%10;
        n/=10;
        a*=pow(10.0,p-1);
        n+=a;
        if(n==x)break;
        if(n>=A&&n<=B)ret++;

    }

    return ret;
}


int main()
{
#ifndef ONLINE_JUDGE
   freopen("C_large.txt", "rt", stdin);
   freopen("output.txt", "wt", stdout);
#endif

    int kas;
    cin>>kas;
    rep(cas,kas){
        cin>>A>>B;
        ll pass=0;
        reps(i,A,B+1){
                pass+=cycle(i);
        }
        //cout<<pass/2<<endl;
        printf("Case #%d: %I64d\n",cas+1,pass/2);
    }
return 0;
}
