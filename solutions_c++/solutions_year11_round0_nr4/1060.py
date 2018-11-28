#include<iostream>
#include<fstream>
#include <iomanip>
using namespace std;
int main(){
    ifstream in("D-large.in");
    ofstream out("D-large.out");
    int T,N,arr[1010],i,cas=1, ans;
    in>>T;
    while(T--){
             i=1;
             in>>N;
             while(N--){
                        in>>arr[i];
                        i++;
             }
             N=i-1;
             ans=0;
             for(int i=1;i<=N;i++){
                     if(arr[i]!=i)ans++;
             }
             cout<<"Case #"<<cas<<": "<<ans<<".000000\n";
             out<<"Case #"<<cas<<": "<<ans<<".000000\n";
             ++cas; 
    }
    system("pause");
    return 0;
}
                                                       
                           
                           
