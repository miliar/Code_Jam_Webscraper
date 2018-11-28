#include <iostream>
#include <map>
using namespace std;
map <int,bool> ck;
int mu[10]={1,10,100,1000,10000,10000,1000000,10000000},cnt;
int a,b;
void dit(int now){
    int q = now;
    int digit=0;
    while(q>0)q/=10,digit++;
    for(int i=1;i<=digit;i++)
       if(now%mu[i]>=mu[i-1]){
          int tmp = now%mu[i]*mu[digit-i]+now/mu[i];
         if(tmp>now && tmp <=b)cnt++;
    //cout << now%mu[i]*mu[digit-i]+now/mu[i] << endl;
    }
}
bool ans[2000001]={0};
int main(){
    int ntc;
    cin >> ntc;
   
    ck.clear();
    for(int tc=1;tc<=ntc;tc++){
    

            cin >> a >> b;
            cnt=0;
            for(int i=a;i<=b;i++){
                  dit(i);

            }
           cout << "Case #"<<tc << ": " << cnt << endl;
    }
  //  while(cin >> ntc){dit(ntc);
   // }
}
