#include<iostream>
using namespace std;
long long n;
int pd,pg;
void f(){
    int nd=pd/__gcd(pd,100),dd=100/__gcd(pd,100);
    int nx=dd-nd;
    if(((long long)dd)>n){
        cout<<"Broken"<<endl;
        return;
    }
    if(pg==100&&nx>0){
        cout<<"Broken"<<endl;
        return;    
    }
    if(pg==0&&nd>0){
        cout<<"Broken"<<endl;
        return;    
    }
    cout<<"Possible"<<endl;      
}
int main(){
    int nc;
    cin>>nc;
    for(int i=0;i<nc;i++){
        cin>>n>>pd>>pg;
        cout<<"Case #"<<i+1<<": ";
        f();
    }    
}
