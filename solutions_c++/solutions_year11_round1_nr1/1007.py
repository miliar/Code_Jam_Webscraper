//La Ilaha Illallahhu Muhammadur Rasulullah (Sm)


#pragma comment(linker,"/STACK:16777216")
#pragma  warning ( disable: 4786)
#include<iostream>
#include<cstdio>
#include<cmath>
#include<vector>
#include<queue>
#include<set>
#include<map>
#include<cctype>
#include<string>
#include<cstring>
#include<algorithm>
#include<stack>
#include<cassert>
#include<list>
#include<utility>
#include<bitset>
#include<cstdlib>
#define ll long long ///for code_blocks
//#define ll int ///for vcc
#define filer() freopen("A-large (1).in","r",stdin)
#define filew() freopen("outA.txt","w",stdout)
#define min(a,b) ((a)>(b)?(b):(a))
#define max(a,b) ((a)<(b)?(b):(a))
#define inf 1<<29
#define MAXS 100007
using namespace std;


ll gcd(ll a,ll b)
{
    if(!a)return b;
    return gcd(b%a,a);
}
//vector<ll>V;
int main()
{
    ll cnt=0;
    ll T;
    filer();
    filew();
    ll N,PD,PG;
    int ks=0;
    cin>>T;

    while(T--)
    {
        ks++;
        printf("Case #%d: ",ks);
        //scanf("%d%d%d",&N,&PD,&PG);
        cin>>N>>PD>>PG;
        if(!PD&&!PG)
        {
            printf("Possible\n");
            continue;
        }

        if(PD&&!PG)
        {
            printf("Broken\n");
            continue;
        }

        if(PD!=100&&PG==100)
        {
            printf("Broken\n");
            continue;
        }



        ll gc=gcd(PD,100);
        ll div=100/gc;

        if(N>=div)
        {
          //  V.push_back(ks);
            cnt++;
            printf("Possible");
        }

        else printf("Broken");

        printf("\n");
    }
  //  for(ll i=0;i<V.size();i++)cout<<V[i]<<endl;
//    printf("%d\n",cnt);
    return 0;
}

/*
2
5
14
20
26
30
36
37
47
48
53
61
62
68
75
79
83
84
94
98
*/
