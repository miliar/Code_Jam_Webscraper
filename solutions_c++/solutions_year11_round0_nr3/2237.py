#include <iostream>
using namespace std;
int main(){
    int ntc,n;
    cin >> ntc;
    for(int tc = 1;tc<=ntc;tc++){
           cin >> n;
           int num,i,mi=999999999;
           long long total=0,ck=0;
           for(i=1;i<=n;i++){
              cin >> num;
              mi= min(mi,num);
              total+=num;
              ck=ck xor num;
           }
           if(ck==0)
              cout << "Case #"<<tc<<": " << total-mi << endl;
           else
              cout << "Case #"<<tc<<": NO" << endl;
    }
}
