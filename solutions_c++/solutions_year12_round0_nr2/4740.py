#include<sstream>
#include <cstdlib>
#include<cstdio>
#include<iostream>
using namespace std;
int nofbestresult();
/*
 * 
 */
int main() {
freopen("a.in", "r", stdin); 
freopen("a.out", "w", stdout); 
int T,i=1;
cin>>T;
while(T>0){
    cout<<"Case #"<<i<<": "<<nofbestresult()<<endl;
    T--;i++;
}
//int x,y,z;
//cin>>x;
//cout<<"no. stored in file : "<<x;
//cin>>y>>z;
//cout<<"\n values of other variable is :"<<y<<z;
return 0;
}

int nofbestresult(){
    int N,S,P,j,ti,count=0;
    cin>>N>>S>>P;
    while(N--){
        cin>>ti;
        if((ti+2)>=(P*3)){
            count++;
        }
        else if((ti+4)>=(P*3)){
            if(S && 2<=ti && ti<=28){
                count++;
                S--;
            }
        }
    }
    return count;
    
}