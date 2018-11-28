#include <iostream>
using namespace std;
#define INF 10000
int main()
{
        int n;
        cin>>n;
        for(int cn=1;cn<=n;cn++)
        {
                int m;
                int inter[1000][3];
                int v;
                cin>>m>>v;
                for(int i=1;i<=(m-1)/2;i++)
                        cin>>inter[i][0]>>inter[i][1];
                for(int i=(m-1)/2+1;i<=m;i++)
                {
                        cin>>inter[i][0];
                        if(inter[i][0]==v)
                                inter[i][2]=0;
                        else
                                inter[i][2]=INF;
                }
                for(int i=(m-1)/2;i>=1;i--)
                        if(inter[i][0]==v)
                                if(inter[i][1]==1)
                                        inter[i][2]=min(min(inter[2*i][2],inter[2*i+1][2])+1,inter[2*i][2]+inter[2*i+1][2]);
                                else
                                        inter[i][2]=inter[2*i][2]+inter[2*i+1][2];
                        else
                                inter[i][2]=min(inter[2*i][2],inter[2*i+1][2]);
                cout<<"Case #"<<cn<<": ";
                if(inter[1][2]>=INF)
                        cout<<"IMPOSSIBLE";
                else
                        cout<<inter[1][2];
                cout<<endl;
        }
        return 0;
}
