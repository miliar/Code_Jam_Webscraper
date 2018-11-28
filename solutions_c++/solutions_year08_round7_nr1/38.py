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
#include<set>

using namespace std;

//=========================================================
// libs:
//
//=========================================================
// program:
//
int N;

string names[1000];
string reqs[1000][10];
int    M[1000];

inline void init(){}

map<string,int> nameid;

int rec(int i)
{
    int n=M[i];
    if(n==0) return 1;
    
    int childs[n];
    int minim=0;

    
    for (int j=0;j<n;j++)
        childs[j]=rec(nameid[reqs[i][j] ]) ;
        
    minim=1e8;
        
    sort(childs,childs+n);
    do
    {
        int av=childs[0]-1;
        int creq=childs[0];
        
        for (int j=1;j<n;j++)
        {
            int r=childs[j]-av;
            if(r>=0)
                creq+=r;
            av=creq-j-1;
        }
        if(!av) creq++;
        minim<?=creq;

    }
    while(next_permutation(childs,childs+n));
    return minim;
    
}

int solve()
{
    for (int i=0;i<N;i++)
        nameid[names[i]]=i;
    return rec(0);
}

//=========================================================
// I/O:
//
bool lowerCase(const string s)
{
    for (int i=0;i<s.length();i++) if(( s[i]<'a' ) || (s[i]>'z'))
         return false;
    return true;
}

int main()
{
    init();
    
    int C; cin>>C;
    for (int r=1;r<=C;r++)
    {
        cin >> N;
        for (int i=0;i<N; i++)
        {
            cin >> names[i];
            cin >> M[i];
            int t=M[i];
            M[i]=0;
            for (int j=0;j<t;j++)
            {
                string x;
                cin>>x;
                if(! lowerCase(x))
                    reqs[i][M[i]++]=x;
            }
        }
        int rs=solve();
        cerr<<"["<<r<<" / "<<C<<"]"<<endl;
        cout<<"Case #"<<r<<": "<<rs   << endl;

        
    }
    return 0;
}
