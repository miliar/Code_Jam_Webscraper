#include<cstdio>
#include<cstring>
#include<fstream>
#include<queue>
#include<cmath>
#include<algorithm>
using namespace std;
ifstream cin("1.in");
ofstream cout("2.out");
struct Node{
    char robot;
    int button;
}node,d;
queue<Node> q;
int n,m,T,t,ans,oi,bi,t1,t2,w1=1,w2=1;
int o[1000],b[1000];
char c;
int main()
{
    int i,j,k,l;
    cin>>T;
    for(l=0;l<T;l++){
        ans=0;oi=0;bi=0;t1=t2=ans=0,w1=w2=1;
        memset(o,0,sizeof(o));
        memset(b,0,sizeof(b));
        cin>>n;
        for(i=0;i<n;i++){
            cin>>node.robot>>node.button;
            if(node.robot=='O') o[oi++]=node.button;
            else b[bi++]=node.button;
            q.push(node);
        }
        while(!q.empty()){
            d=q.front();
            q.pop();
            if(d.robot=='O'){
                t=abs(d.button-w1)+1;
                w1=d.button;
                if(ans-t1<t)
                    ans=t1+t;
                else ans+=1;
                t1=ans;
            }
            else{
                t=abs(d.button-w2)+1;
                w2=d.button;
                if(ans-t2<t)
                    ans=t2+t;
                else ans+=1;
                t2=ans;
            }
        }
        cout<<"Case #"<<l+1<<": "<<ans<<endl;
    }
    return 0;
}
