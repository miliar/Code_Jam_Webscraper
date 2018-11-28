#include <iostream>
#include <string.h>
#include <vector>
#include <set>
#include <queue>
#include <cmath>
#include <algorithm>

using namespace std;

int t,k,n;

int status(int N,int K){
    return K%(1<<N)==(1<<N)-1;
}

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    cin>>t;
    for(int i=0; i<t; i++){
        cin>>n>>k;
        if(status(n,k)){
            cout<<"Case #"<<i+1<<": ON"<<endl;
        }
        else{
            cout<<"Case #"<<i+1<<": OFF"<<endl;
        }
    }
	return 0;
}
