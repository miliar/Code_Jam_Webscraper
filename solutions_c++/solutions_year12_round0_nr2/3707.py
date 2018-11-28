#include <iostream>
#include <cstdio>
#include <vector>
#include <list>
#include <string>
#include <numeric>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
using namespace std;

int T,N,S,p;
int t[101];

void getResult(){
    int count = 0;
    for(int i=0;i<N;i++){
        if(t[i]/3>=p){
            count++;
            //cout<<t[i]<<endl;
        }
        else if(t[i]/3+t[i]%3>=p){
            if(p-t[i]/3==2){
                if(S!=0){
                    count++;
                    //cout<<t[i]<<endl;
                    S--;
                }
            }
            else{
                count++;
                //cout<<t[i]<<endl;
            }
        }
        else if(t[i]/3==p-1&&S!=0&&t[i]!=0){
            count++;
            //cout<<t[i]<<endl;
            S--;
        }
    }
    cout<<count<<endl;
}


int main(){
    freopen("B.in","r",stdin);
    //freopen("test.out","w",stdout);
    cin>>T;
    for(int Case=1;Case<T+1;Case++){
        cin>>N>>S>>p;
        for(int i=0;i<N;i++){
            cin>>t[i];
        }
        cout<<"Case #"<<Case<<": ";
        getResult();
    }
    return 0;
}
