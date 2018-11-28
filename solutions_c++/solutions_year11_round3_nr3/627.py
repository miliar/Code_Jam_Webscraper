#include <stdio.h>
#include <iostream>
#include <string>
#include <cstdlib>
#include <fstream>

using namespace std;


int main(){
    ifstream in("c.in");
    ofstream out("c.out");  
    
    int t,n,min,max,a[1000];
    
    in >> t;
    
    for(int i=0;i<t;i++){
            in >> n >> min >> max;
            for (int j=0;j<n;j++ ){
                in >> a[j];
            }
            bool ok = true;
            for (int k=min;k<=max;k++){
                bool flag = true;
                for (int j=0;j<n;j++ ){
                    if (!((k % a[j] == 0) || (a[j] % k == 0))){
                       flag = false;
                       break;
                    }
                } 
                if (flag){
                   out << "Case #"<<i+1<<": "<<k<<endl;
                   ok = false;
                   break;
                }
            }
            if (ok)
               out << "Case #"<<i+1<<": NO"<<endl;
    }
    
}
