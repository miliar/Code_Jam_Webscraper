/*
PROG: A
LANG: C++
*/
#include <iostream>
#include <fstream>
#include <algorithm>
#include <queue>

using namespace std;

#define SUBMIT
#define _DSP(X)
#   define DV(Var) #Var<<"="<<Var<<' '
#ifdef SUBMIT
    ofstream fout ("A.out");ifstream fin ("A.in");
#   define cin fin
#   define cout fout
#endif

const int MAXN=10000+200;
int d[MAXN],l[MAXN];

int lgst[MAXN];bool inq[MAXN];
int furst(int n)
{int i;
    for(i=0;i<n;++i)
        lgst[i]=0,inq[i]=false;
    queue<int> q;
    q.push(0);lgst[0]=d[0];inq[0]=true;

    while(!q.empty())
    {
        int now=q.front();
        for(i=now+1;i<n;i++)
        {
            if(d[i]>d[now]+lgst[now])
                break;
            if(lgst[i]<min(d[i]-d[now],l[i]))
            {
                lgst[i]=min(d[i]-d[now],l[i]);
                if(!inq[i]){q.push(i);inq[i]=true;}
            }
        }
        for(i=now-1;i>=0;--i)
        {
            if(d[i]<d[now]-lgst[now])
                break;
            if(lgst[i]<min(-d[i]+d[now],l[i]))
            {
                lgst[i]=min(-d[i]+d[now],l[i]);
                if(!inq[i]){q.push(i);inq[i]=true;}
            }
        }

        q.pop();inq[now]=false;
    }

    int m=0;
    for(i=0;i<n;++i)
        m=max(m,d[i]+lgst[i]);

    return m;
}

int main()
{
    int T;
    cin>>T;cin.ignore();
    for(int t=1;t<=T;++t)
    {int i;
        int N,D;
        cin>>N;
        for(i=0;i<N;++i)
            cin>>d[i]>>l[i];
        cin>>D;

        bool ans=furst(N)>=D;
        cout<<"Case #"<<t<<": "
            <<(ans?"YES":"NO")
            <<endl;
    }

    return 0;
}
