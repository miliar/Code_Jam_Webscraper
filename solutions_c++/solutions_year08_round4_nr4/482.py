#include <iostream>
using namespace std;
int N,k;
int total;
string S;
int t[20];
bool flag[20];
void check()
{
    int i,j,o;
    char tmp[2000];
    //cout<<"ok";
    /*for (i=0;i<k;i++)
        cout<<t[i]<<' ';
    cout<<endl;*/
    for (i=0;i<S.size()/k;i++)
        for (j=0;j<k;j++)
            tmp[i*k+j]=S[i*k+t[j]];
    o=1;
    for (i=0;i<S.size()-1;i++)
        if (tmp[i]!=tmp[i+1])
            o++;

    //cout<<tmp<<endl;
    if (o<total)
        total=o;
}
void DFS(int dep)
{
    if (dep==k)
        check();
    else
    {
        int i;
        for (i=0;i<k;i++)
            if (flag[i])
            {
                flag[i]=false;
                t[dep]=i;
                DFS(dep+1);
                flag[i]=true;
            }
    }
}
int main()
{
    int Ni;
    freopen("D-small-attempt0.in","r",stdin);
    freopen("D-small-attempt0.out","w",stdout);
    cin>>N;
    for (Ni=1;Ni<=N;Ni++)
    {
        cin>>k;
        cin>>S;
        total=S.size();
        memset(t,0,sizeof(t));
        memset(flag,true,sizeof(flag));
        DFS(0);
        cout<<"Case #"<<Ni<<": "<<total<<endl;
    }
    return 0;
}
