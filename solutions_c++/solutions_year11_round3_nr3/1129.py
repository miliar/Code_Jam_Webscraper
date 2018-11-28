#include <iostream>
#include <stdio.h>

using namespace std;


int main(){

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int M[200];
    int T;
    cin>>T;
    for(int ts=1;ts<=T;ts++){
        int N, L , H;
        int counter=0;
        cin >> N >> L >> H;
        int var;
        for(int i=1;i<=N;i++){
            cin >> var;
            M[++counter]=var;
        }

        int ans=0;
        for(int i=L;i<=H;i++){
            int p=1;
            for(int j=1;j<=counter;j++){
                if(i%M[j]!=0&&M[j]%i!=0) {p=0;break;}
            }
            if(p==1) {ans=i;break;}
        }

        if(ans==0)
        cout<<"Case #"<<ts<<": NO\n";
        else
        printf("Case #%d: %d\n",ts,ans);

    }

    return 0;
}
