#include <stdio.h>
#include <iostream>
#include <string>
#include <stdlib.h>
#include <fstream>

using namespace std;

int gcd(int a,int b){
    if (b % a == 0) return a;
    else return gcd((b % a),a);
}
int main(){
    
    int a,b,ans[1000],t,pd,pg;
    long long n;
    
    ans[0] = 0;
    ans[100] = 1;
    
    ifstream in("1.in");
    ofstream out("1.out");
    
    for (int i = 1;i<100;i++){
        ans[i] = 100 / gcd(i,100);
    }
    
    in >> t;
    
    for (int i = 0;i<t;i++){
        in >> n >> pd >> pg;
        if ((pg == 100 && pd != 100 ) || (pg == 0 && pd > 0)) out << "Case #" << i+1 <<": Broken"<<endl;
        else{
             if (ans[pd] <= n) 
                out << "Case #" << i+1 <<": Possible"<<endl;
             else 
                out << "Case #" << i+1 <<": Broken"<<endl;
        }
    }
    
    system("pause");
}
