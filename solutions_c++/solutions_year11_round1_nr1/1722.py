#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <string>
#include <set>
#include <math.h>

using namespace std;
int gcd(int m, int n)     	
{                         	
   int  r;                	
   while (n != 0) {       	
      r = m % n;          	
      m = n;              	
      n = r;
   }                      	
   return m;              	
}

string retT(int n, int n2, int pg, int pd) {
    string ret;
    if(pg == 0 && pd != 0) {
        return " Broken";
    }
    if(pg == 100 && pd != 100) {
        return " Broken"; 
    }
    if(n2 <= n) {
        ret = " Possible";
    } else {
        ret = " Broken";
    }
    return ret;
}

int main() {
    int T;
    int n, pd, pg;
    double fract, intpart;
    cin >> T;
    for(int i=0; i < T; i++) {
        printf("Case #%d:", i+1);
        cin >> n >> pd >> pg;
        int C = gcd(pd,100);
        int n1 = pd / C;
        int n2 = 100 / C;
        string ret = retT(n,n2,pg,pd);
        cout << ret << endl;
    }
    return 0;
}