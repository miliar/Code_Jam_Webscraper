#include<iostream>
#include<fstream>
#include<algorithm>
#include<queue>
using namespace std;
int main(){
    ifstream in ("C-large.in");
    ofstream out("C-large.out");
    int T;
    int N;
    in>>T;
    int mymin;
    int i=1;
    while(T--){
               in>>N;
               int realsum=0, xorsum=0,C; 
               mymin=999999999;
               while(N--){
                          in>>C;
                          realsum +=C; 
                          xorsum^=C;
                          mymin = min(C,mymin);
               }
               cout<<"Case #"<<i<<": ";
               out<<"Case #"<<i<<": ";
               if(xorsum) {cout<<"NO\n";out<<"NO\n";}
               else {cout<<realsum-mymin<<'\n';out<<realsum-mymin<<'\n';}
               ++i;
    }
    system("pause");
    return 0;
}
