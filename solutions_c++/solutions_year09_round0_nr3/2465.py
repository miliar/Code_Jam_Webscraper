#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cassert>
#include<queue>
#include<stack>
#include<sstream>
#include<cmath>
#include<cstring>
#include<string>
#include<algorithm>
#include<map>
#include<vector>
#include<set>
#include<list>
#include<cctype>
#include<iterator>

using namespace std;

#define sz size()
#define pb push_back
#define ppb pop_back
#define mp make_pair
#define ii pair< int, int >
#define dd pair< double , double >
#define ll long long
#define vi vector< int > 
#define vvi vector< vi > 
#define v(x) vector< x > 
#define vs v(string)
#define vc v(char)
#define all(x) x.begin(),x.end()
#define fr(i,start,end) for(int i=start;i<end;i++)
#define fz(i,x) fr(i,0,x.sz)
#define ss stringstream
#define gi(i) scanf("%d",&i)
#define gl(i) scanf("%lld",&i)
#define dbgc(x) cout<<"Hello world - "<<#x<<endl;
#define dbg(x) cout<<#x<<"-->"<<x<<endl

ll search(string &input, int iindex , string &pattern , int pindex)
{
    if(pindex==pattern.sz)
        return 1;
    ll temp=0;
    int t=input.sz-pattern.sz+pindex,tt;
    for(int i=iindex;i<=t;i++)
    {
        if(input[i]==pattern[pindex])
            temp=temp+search(input,i+1,pattern , pindex+1);    
    }
    return temp;
}

int main()
{
    int n;
    scanf("%d\n",&n);
    char input[505];
    string str,pattern("welcome to code jam");
    fr(i,0,n)
    {
        cin.getline(input,500,'\n');
        str = string(input);
        printf("Case #%d: ",i+1);
        ll ans = search(str,0,pattern,0);
        if(ans<10) printf("000%d\n",ans);
        else if(ans<100) printf("00%d\n",ans);
        else if(ans<1000) printf("0%d\n",ans);
        else printf("%d\n",ans%10000);
    }
    return 0;    
}
