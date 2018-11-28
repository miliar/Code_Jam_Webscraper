#include<iostream>
using namespace std;

int main(){
    int N;
    cin>>N;
    for(int i=1;i<=N;++i){
        int num,sum,xsum,mini,tmp;
        cin>>num;
        cin>>tmp;
        sum=xsum=mini=tmp;
        for(int j=1;j<num;++j){
            cin>>tmp;
            sum+=tmp;
            xsum^=tmp;
            mini=min(mini,tmp);
        }
        cout<<"Case #"<<i<<": ";
        if(xsum!=0)
            cout<<"NO"<<endl;
        else
            cout<<sum-mini<<endl;
    }
    return 0;
}
