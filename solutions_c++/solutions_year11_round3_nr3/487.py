#include<iostream>

using namespace std;

int d[100];

int main(){
    freopen("C-small-attempt0.in","r",stdin);
    freopen("x.out","w",stdout);
    int tc,n,l,h;
    cin>>tc;
    for(int t=1;t<=tc;t++){
        cin>>n>>l>>h;
        for(int i=0;i<n;i++)
            cin>>d[i];
        printf("Case #%d: ",t);
        bool no=true;
        for(int i=l;i<=h&&no;i++){
            bool is_possible=true;
            for(int j=0;j<n&&is_possible;j++)
                if(!(d[j]>i&&d[j]%i==0||d[j]<=i&&i%d[j]==0))
                    is_possible=false;
            if(is_possible){
                cout<<i<<endl;
                no=false;
            }    
        }
        if(no)cout<<"NO"<<endl;
    }
    return 0;
}    
