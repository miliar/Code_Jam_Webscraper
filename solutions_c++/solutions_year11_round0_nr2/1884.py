#include<iostream>
#include<cstdio>
#include<fstream>
#include<algorithm>
#include<cmath>
#include<vector>
#include<map>
#include<cstring>

using namespace std;

int nc,nd,n;
char c[100][5],d[100][5],st[105],ans[105];
bool u[105];

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int cs,i,j,t;
    cin>>cs;
    for (int k=1;k<=cs;k++){
        cin>>nc;
        for (i=1;i<=nc;i++) cin>>c[i];
        cin>>nd;
        for (i=1;i<=nd;i++) cin>>d[i];
        cin>>n>>st;
        int l=0;
        ans[0]=st[0];
        memset(u,0,sizeof(u));
        for (i=1;i<n;i++){
            if (!u[i-1]){
               for (j=1;j<=nc;j++)
                   if ((st[i]==c[j][0] && st[i-1]==c[j][1]) || (st[i]==c[j][1] && st[i-1]==c[j][0])){
                      ans[l]=c[j][2];
                      u[i]=true;
                      break;
                      }
               }
            for (j=1;j<=nd;j++)
                if (!u[i])
                for (t=l;t>=0;t--)
                    if ((st[i]==d[j][0] && ans[t]==d[j][1]) || (st[i]==d[j][1] && ans[t]==d[j][0])){
                       l=-1;
                       u[i]=true;
                       break;
                       }
            if (!u[i]){
               l++;
               ans[l]=st[i];
               }
            }
        cout<<"Case #"<<k<<": [";
        bool flag=true;
        for (i=0;i<=l;i++)
            if (flag) { cout<<ans[i]; flag=false; }
               else cout<<", "<<ans[i];
        cout<<"]"<<endl;
        }
}
                     
