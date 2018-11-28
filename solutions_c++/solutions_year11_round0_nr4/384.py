#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <queue>
#include <cmath>

using namespace std;

int main(){
    int T,N,a;
    int tot=0,correct=0;
    cin>>T;
    for (int i=0;i<T;i++){
        cin>>N;
        correct=0;
        for (int j=0;j<N;j++){
            cin>>a;
            if (a==j+1) correct++;
        }
        cout<<"Case #"<<i+1<<": "<<N-correct<<endl;
    }
    return 0;
}
