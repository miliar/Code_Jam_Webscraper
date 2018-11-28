#include<iostream>
#include<queue>

using namespace std;

queue<int> q;

int main(){
    int cases,rep,cap,ng,groups[12];
    cin>>cases;
    for(int cc=0;cc<cases;cc++){
        cin>>rep>>cap>>ng;
        while(!q.empty()) q.pop();
        for(int cc1=0;cc1<ng;cc1++){
            cin>>groups[cc1];
            q.push(groups[cc1]);
        }
        int cost=0;
        for(int i=0;i<rep;i++){
            int onboard=0;
            for(int j=0;j<ng;j++){
                int front=q.front();
                onboard+=front;
                if(onboard>cap) break;
                q.push(front);
                q.pop();
                cost+=front;
            }
        }
        cout<<"Case #"<<cc+1<<": "<<cost<<endl; 
    }
    return 0;
}
