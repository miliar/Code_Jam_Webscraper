#include <iostream>
#include <cmath>
#include <math.h>
#include <fstream>
#include <string>
#include <cstring>
#include <map>
#include <vector>
#include <utility>
using namespace std;

int main(){
    ifstream myf;
    myf.open("input3.txt");
    
    int T;
    myf>>T;
    
    ofstream myfile;
    myfile.open("result3.txt");
    
    for (int it = 0; it < T; it++){
    
    int n;
    myf>>n;
    int A;
    myf>>A;
    int res = A;
    int tot = A;
    int min = A;
    
    
    for (int i = 1; i < n; i++){
        myf>>A;
        tot+=A;
        res = res ^ A;
        if (A < min) min = A;    
    }
    
    if (res != 0)  myfile<<"Case #"<<it+1<<": NO"<<endl;
    else  myfile<<"Case #"<<it+1<<": "<<tot-min<<endl;
    
    
    
    
    }
    
    myfile.close();
    return 0;
}
