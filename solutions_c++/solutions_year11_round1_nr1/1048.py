#include <iostream>
#include <fstream>
using namespace std;

#define INPUT "A-large.in"
#define OUTPUT "a.out"

long long ucln(long long a, long long b){
    while ( b){
        long long r = a % b;
        a = b;
        b = r;
    }
    return a;
}

bool solve(long long pd,long long pg, long long n){
    if (pg == 0)
        return (pd ==0);
    if (pg == 100)
        return (pd == 100);

    return (100 / ucln(pd,100) <= n);
}

int main(){

    freopen(INPUT,"r",stdin);
    freopen(OUTPUT,"w",stdout);

    long long test;
    cin >> test;
    for (long long task =1;task<=test;task++)
    {
        long long n,pd,pg;
        cin >> n >> pd >> pg;
        if (solve(pd,pg,n))
            cout << "Case #"<<task<<": Possible"<<endl;
        else
            cout << "Case #"<<task<<": Broken"<<endl;
    }
}
