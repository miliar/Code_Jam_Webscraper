#include <iostream>
#include <algorithm>
#include <stdio.h>
#define WH(a)   while(a)
#define REP(i,a,b)  for(int i = a;i<b;i++)
#define FOR(i,a)    for(int i = 0;i<a;i++)


using namespace std;

int main()
{
    freopen("input.txt","r", stdin);
    freopen("output.txt","w", stdout);
    int a[1011];
    int t;
    int caseno = 0;
    cin>>t;
    FOR(i,t)
    {
        int n,p,s;
        caseno++;
        cin>>n>>s>>p;
        FOR(i,n)    cin>>a[i];
        sort(a,a+n);
        int s1 = s;
        int ans = 0;
        for(int i = n-1;i>=0;i--)
        {
            int check1 = a[i]/3 + (a[i]%3!=0);
            int check2 = (a[i]>=2)?((a[i]-2)/3 + 2):a[i];
            if(check1>=p)   ans++;
            else if(check2>=p&&s1)  ans++,s1--;
        }
        cout<<"Case #"<<caseno<<": "<<ans<<"\n";
    }

    return 0;
}
