#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int main(){
    int T,i;
    long long n;
    int pd,pg;
    freopen ("A-large.in","r",stdin);
    freopen ("Al.out","w",stdout);
    cin>>T;
    for( int cas=1;cas<=T;cas++){
        cin>>n>>pd>>pg;
    //    cout<<n<<" "<<pd<<" "<<pg<<endl;
        int flag=0;
        if(n>=100||pd==0)flag=1;
        else {
            for(i=1;i<=n;i++){
                if((i*pd)%100==0){
                    flag=1;
                    break;
                }
            }
        }
        if(flag==1){
            if(pd!=100&&pg==100)flag=0;
            if(pd!=0&&pg==0)flag=0;
        }
        
        if(flag)
        cout<<"Case #"<<cas<<": "<<"Possible"<<endl;
        else cout<<"Case #"<<cas<<": "<<"Broken"<<endl;
    }
}
