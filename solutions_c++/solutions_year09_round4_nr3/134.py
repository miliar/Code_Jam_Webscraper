#include<iostream>
using namespace std;
int ans;
int map[200][200];
int a[200][200];
int used[200];
int link[200];
int n,k;
int cross(int i,int j){
    int big=0,small=0;
    for(int q=0;q<k;q++){
        if(a[i][q]>a[j][q])big=1;
        if(a[i][q]<a[j][q])small=1;
        if(a[i][q]==a[j][q])big=small=1;
    }
    if(big==1&&small==0)return(1); else return(0);
}
int find(int now){
    if(used[now])return(0);
    used[now]=1;
    for(int i=1;i<=n;i++)
        if(map[now][i]&&(link[i]==0||find(link[i]))){
            link[i]=now;
            return(1);
        }
    return(0);
}

int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int tt,i,j;
    cin>>tt;
    for(int ii=1;ii<=tt;ii++){
        cin>>n>>k;
        for(i=1;i<=n;i++)
            for(j=0;j<k;j++)
                cin>>a[i][j];
        memset(map,0,sizeof(map));
        for(i=1;i<=n;i++)
            for(j=1;j<=n;j++)
                if(i!=j&&cross(i,j)){
                    map[i][j]=1;
                    //cout<<i<<" "<<j<<endl;
                }
        ans=n;
        memset(link,0,sizeof(link));
        for(i=1;i<=n;i++){
            memset(used,0,sizeof(used));
            if(find(i))ans--;
        }
        cout<<"Case #"<<ii<<": "<<ans<<endl;
    }
    return(0);
}

