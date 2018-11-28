#include <iostream>
#include <cstdio>
#include <queue>
using namespace std;
int resuelva(queue<int> q,int r,int k){
    int cc=1,suma=0,dato,sumatotal=0,n;
    n=0;
    while(cc<=r){
        while((true)&&(q.size()>n)){
            dato=q.front();
            if(suma+dato>k){
            break;
            }
            else{
            suma+=dato;
            q.pop(); q.push(dato);
            }
            n++;
        }
        n=0;
        //suma-=dato;
        cc++;
        sumatotal+=suma;
        suma=0;
    }
    return sumatotal;
}
int main(){
    int t,cont=0,suma=0;
    int r,k,n,dato;
    scanf("%d",&t);
    for(int i=1;i<=t;i++){
        cin>>r>>k>>n;
        queue<int> q;
        for(int j=1;j<=n;j++){
            cin>>dato;
            q.push(dato);
        }
        suma=resuelva(q,r,k);
        cout<<"Case #"<<i<<": "<<suma<<endl;
    }
}
/*
3
100 10 1
1
4 6 4
1 4 2 1
5 5 10
2 4 2 3 4 2 1 2 1 3
*/
