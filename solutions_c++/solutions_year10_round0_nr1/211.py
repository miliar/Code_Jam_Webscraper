#include<iostream>
#include<vector>
#include<string>
#include<map>
#include<queue>
#include<cstdlib>
#include<time.h>
#include<string.h>
#include<list>
#include<sstream>
#include<algorithm>
using namespace std;
#define ps system("pause")
int main()
{
    long long a[100];
    a[1]=1;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    for(int i=2;i<40;i++) 
    {
        a[i]=a[i-1]*2+1;
    }
    long long n,k;
    int t;
    cin>>t;
    for(int cas=1;cas<=t;cas++)
    {
        cin>>n>>k;
        cout<<"Case #"<<cas<<": ";
        if(k%(a[n]+1)==a[n]) cout<<"ON"<<endl;
        else cout<<"OFF"<<endl;
    }
    return 0;
}
