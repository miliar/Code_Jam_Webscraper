#include<string>
#include<iostream>
#include<sstream>
#include<assert.h>
#include<cstdio>
#include<map>
#include<algorithm>
#include<bitset>
#include<cmath>
#include<queue>
#include<functional>


using namespace std;

int solve(int k, string s)
{
    int p[k];
    for (int i=0;i<k;i++) p[i]=i;
    int best=s.length();
    do
    {
        string ns=s;
        char last='?';
        int x=0;
        for (int i=0;i<s.length();i++)
        {
            ns[i]=s[ (i-i%k) + p[i%k] ];
            if(last!=ns[i])
                last=ns[i],
                x++;
        }
        //for (int i=0;i<k;i++) cout<<p[i]<<" "; cout<<ns<<" : "<<x<<endl;
        best<?=x;
    }
    while (next_permutation(p,p+k) );
    return best;
}


//=========================================================
// I/O:
//
int main()
{
    int N; cin>>N;
    for (int i=1;i<=N;i++)
    {
        string s;
        int k;
        cin>>k>>s;
        int r=solve(k,s);
        assert(s.length()%k==0);

        cout<<"Case #"<<i<<": "<<r<<endl;
    }
    return 0;
}
