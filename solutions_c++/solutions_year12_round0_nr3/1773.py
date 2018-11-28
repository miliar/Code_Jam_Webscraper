#include<iostream>
#include<sstream>
#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<cmath>
#include<vector>
#include<map>
#include<set>
#include<string>
using namespace std;


int main(int argc, char *argv[]){
    int N;
    cin>>N;
    for(int i=1;i<=N;++i){
        int num=0;
        int A,B;
        string sB,m,sn;
        cin>>A;
        cin>>B;
        stringstream ss(stringstream::in | stringstream::out);;
        ss << B<<endl;
        ss >> sB;

        for(int n=A;n<=B;++n){
            ss << n<<endl;
            ss >> sn;

            //cerr<<"n "<<sn<<endl;
            set <string> visited;
            for(int i=sn.length()-1;i>0;--i){
                string m;
                m=sn.substr(i);
                m+=sn.substr(0,i);

                if( !visited.count(m) && m > sn && m <= sB){
                    ++num;
                    //cerr<<"n "<<sn<<" m "<<m<<" num "<<num<<endl;
                    visited.insert(m);
                }
            }
        }
        cout<<"Case #"<<i<<": "<<num<<endl;           
    }
    return EXIT_SUCCESS;    
}
