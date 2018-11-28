#include <iostream>
#include <vector>
#include <queue>
#include <set>
#include <algorithm>
#include <sstream>
#include <cmath>
#include <string>
#include <stdio.h>
using namespace std;
int N,M;
vector<int> E[50];
int D[50];
int T[50];
queue<int> Q;
vector<int> S[50];

int nas=0;
int A[50];
int R[50];
void rec(int x)
{
    if(D[x]==0)
    {
        int i,I=D[0],j,J,a;

        for(i=0;i<N;i++) R[i]=0;
        for(i=0;i<I;i++)
        {
            R[A[i]]=1;
            a=A[i];
            J=E[a].size();
            for(j=0;j<J;j++)
                if(R[E[a][j]]==0)
                    R[E[a][j]]=-1;
        }
        a=0; for(i=0;i<N;i++) if(R[i]==-1) a++;
        if(a>nas) nas=a;
        return ;
    }

    A[T[x]]=x;
    int i,I=E[x].size();
        for(i=0;i<I;i++)
            if(D[E[x][i]]==D[x]-1)
            {
                rec(E[x][i]);
            }
}
void test()
{
    int i,j,a,b,I;
    char c;
    cin>>N>>M;
    for(i=0;i<N;i++)
    {
        E[i].clear();
        S[i].clear();
        D[i]=-1;
        T[i]=-1;
    }
    for(i=0;i<M;i++)
    {
        cin>>a>>c>>b;
        E[a].push_back(b);
        E[b].push_back(a);
        //cout<<a<<" "<<b<<endl;
    }

    D[1]=0;
    Q.push(1);
    while(!Q.empty())
    {
        a=Q.front(); Q.pop();
        I=E[a].size();
        for(i=0;i<I;i++)
            if(D[E[a][i]]==-1)
            {
                D[E[a][i]]=D[a]+1;
                Q.push(E[a][i]);
            }
    }

    T[0]=0;
    Q.push(0);
    while(!Q.empty())
    {

        a=Q.front(); Q.pop();
        S[T[a]].push_back(a);

        I=E[a].size();
        for(i=0;i<I;i++)
            if(T[E[a][i]]==-1&&D[E[a][i]]==D[a]-1)
            {
                T[E[a][i]]=T[a]+1;
                Q.push(E[a][i]);
            }
    }

    cout<<D[0]-1;

    nas=0;

    rec(0);
    cout<<" "<<nas;
}
int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    int i,T;
    cin>>T;
    for(i=0;i<T;i++)
    {
      cout<<"Case #"<<i+1<<": ";
      test();
      cout<<endl;
    }
    return 0;
}
