#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <fstream>

#define fir(i,j,n) for(int (i)=(j);(i)<(n);(i)++)
#define forn(i,j,n)  for(int (i)=(j);(i)<=(n);(i)++)
#define Sort(a) sort(a.begin(),a.end())
#define PB push_back
#define MP make_pair

using namespace std;

long long gcd(long long a,long long b){
    long long t;
    while(a%b!=0){
        t=a%b;
        a=b;
        b=t;
    }
    return b;
}

int main()
{
    fstream fin,fout;
    fin.open("inp.txt",ios::in);
    fout.open("out.txt",ios::out);
    
    int t,cnt=1;
    long long n,pd,pg,q,x,y;
    bool f=0;
    
    double d1,d2;
    fin>>t;
    
    while(t--){
        fin>>n>>pd>>pg;
        fout<<"Case #"<<cnt++<<": ";
        if(pd==0 && pg==0){
           fout<<"Possible\n";
           continue;
        }

        if((pg==100 && pd<100) || (pg==0 && pd>0)){
           fout<<"Broken\n";        
           continue;
        }
        
        x=gcd(100,pd);
        y=gcd(100,pg);
        q=100/x;
        
        f=0;
        for(long i=1;(i*q)<=n;i++){
             f=1; 
             break;
        }
        
        if(f==0) {
           fout<<"Broken\n";
           continue;
        }
        
        if(pg!=100 || (pg==100 && pd==100))
        fout<<"Possible\n";
        
        else
           fout<<"Broken\n";
    }
    
    system("pause");
    return 0;
}
