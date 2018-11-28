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

int canchange[10001];
int value[10001];
int  M;
int  V;

int mem[10001][2];

int rec(int p, int req)
{
    if(p>(M-1)/2) //leaf
        return ((value[p]==req)?0:-2);

    int &res= mem[p][req];
    //cout<<"?"<<endl;
    if(res!=-1) return res;
    res=-2;
    
    for (int k=0;k<2;k++) if( (canchange[p]) || (k==value[p]) )
    {
        int x=0;
        if(k!=value[p]) x++;
        if(k==1) //AND
        {
            if(req)
            {
                int a=rec(p*2,1), b= rec(p*2+1,1);
                if( (a!=-2) && (b!=-2) ) x+=a+b;
                else x=-2;
            }
            else
            {
                int a=rec(p*2,0), b= rec(p*2+1,0);
                if( (a!=-2) && (b!=-2) ) x+=(a<?b);
                else if (a!=-2) x+=a;
                else if (b!=-2) x+=b;
                else x=-2;
            }
        }
        else //OR
        {
            if(!req)
            {
                int a=rec(p*2,0), b= rec(p*2+1,0);
                if( (a!=-2) && (b!=-2) ) x+=a+b;
                else x=-2;
            }
            else
            {
                int a=rec(p*2,1), b= rec(p*2+1,1);
                if( (a!=-2) && (b!=-2) ) x+=(a<?b);
                else if (a!=-2) x+=a;
                else if (b!=-2) x+=b;
                else x=-2;
            }

        }
        //cout<<"*("<<p<<","<<req<<")"<<x<<endl;
        if(x!=-2)
        {
            if((res==-2) || (res>x) ) res=x;
        }
    }
    //cout<<"("<<p<<","<<req<<")"<<res<<endl;
    return res;
}

int solve()
{
    memset(mem,-1,sizeof(mem));
    return rec(1,V);
}

//=========================================================
// I/O:
//
int main()
{
    int N; cin>>N;
    for (int c=1;c<=N;c++)
    {
        cin>>M>>V;
        for (int i=1;i<=(M-1)/2;i++)
            cin>>value[i]>>canchange[i];

        for (int i=1;i<=(M+1)/2;i++)
            cin>>value[ ((M-1)/2)+i],
            canchange[ ((M-1)/2)+ i]=false;
        
        int r=solve();
        cout<<"Case #"<<c<<": ";
        if(r==-2) cout<<"IMPOSSIBLE";
        else      cout<<r;
        cout<<endl;       
    }
    return 0;
}
