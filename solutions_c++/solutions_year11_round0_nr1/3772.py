#include<iostream>
using namespace std;

class robot{
    public:
        robot():pos(1),time(0){}
        void go(int n){
            time+=(n>pos?n-pos:pos-n);
            pos=n;
        }
        void press(){
            ++time;
        }
        void wait(const robot& b){
            if(time<b.time)
                time=b.time;
        }
        int pos;
        int time;
};

int main(){
    int N;
    cin>>N;
    for(int i=1;i<=N;++i){
        robot O,B;
        int num;
        cin>>num;
        for(int j=0;j<num;++j){
            int n;
            char c;
            cin>>c>>n;
            if(c=='O'){
                O.go(n);
                O.wait(B);
                O.press();
            }else{
                B.go(n);
                B.wait(O);
                B.press();
            }
        }
        cout<<"Case #"<<i<<": "<<max(B.time,O.time)<<endl;
    }
    return 0;
}
