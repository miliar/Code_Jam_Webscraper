#include<iostream>
#include<cstdio>
#include<vector>
using namespace std;


int main(){
    long long sum,aux,temp,sumX;
    vector<long long> candys;
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int ic=1,casos,c,i;
    cin>>casos;
    while(casos--){
        cin>>c;
        for(i=0;i<c;i++){
            cin>>temp;
            candys.push_back(temp);
        }
        sum=0;
        sumX=0;
        aux=-1;
        for(i=0;i<candys.size();i++){
            sum+=candys[i];
            if(aux==-1) aux=candys[i];
            else{
                if(aux>candys[i]) aux=candys[i];
            }
            sumX=sumX^candys[i];
        }
        if(sumX>0)
            cout<<"Case #"<<ic<<": NO"<<endl;
        else
            cout<<"Case #"<<ic<<": "<<sum-aux<<endl;

        ic++;
        candys.clear();
    }
    return 0;
}
