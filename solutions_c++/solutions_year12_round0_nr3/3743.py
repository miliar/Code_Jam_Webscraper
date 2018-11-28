#include<iostream>
#include<map>
#include<cstring>
using namespace std;
int bas(int x){
    int a=1;
    while(x/=10)a++;
    return a;
}
int main(){
    int ba10[9];
    ba10[0]=1;
    for(int i=1;i<9;i++){
        ba10[i]=ba10[i-1]*10;
    }
    int t;
    cin>>t;
    for(int z=1;z<=t;z++){
        int a,b;
        cin>>a>>b;
        int ans=0;
        //cout<<bas(a)<<" "<<bas(b)<<endl;
        for(int i=a;i<b;i++){
            int max=0;
            int arr[20];
            int len=bas(i);
            for(int j=1;j<len;j++){
                int ba=i%ba10[j];
                int fo=i/ba10[j];
                int tmp=ba*ba10[len-j]+fo;
                if(tmp<=i)continue;
                else if(bas(tmp)!=len)continue;
                else if(tmp<=b){
                    bool t=true;
                    for(int x=0;x<max;x++){
                        if(arr[x]==tmp){
                            t=false;
                            break;
                        }
                    }
                    if(t){
                        ans++;
                        arr[max++]=tmp;
                    }
                }
            }
        }
        cout<<"Case #"<<z<<": "<<ans<<endl;
    }
}
