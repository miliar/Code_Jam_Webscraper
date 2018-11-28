//gcj-2011-1a-a

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define FOR(i, a, b) for (int i(a), _b(b); i <= _b; ++i)
#define REP(i, n) for (int i(0), _n(n); i < _n; ++i)
ifstream fin("I://fin.txt");
ofstream fout("I://out.txt");

string solve(){
    string ret;
    int pd,pg,Pd,d,wd;
    long long n;
    
    fin >> n >> pd >> pg;
    
    Pd=pd;
    d=1;
    if(pd%4){
        if(pd%2)d=4; else d=2;
    }
    if(pd%25){
        if(pd%5)d*=25; else d*=5;
    }
    
    wd = pd*d/100;
    
    if(d>n)return "Broken";
    
    if((pg==100) && (pd<100))return "Broken";
    if((pg==0) && (pd>0))return "Broken";
    
    return "Possible";
}

int main(int argc, char *argv[])
{
    int n;
    
    fin >> n;
    
    REP(i,n){
        fout << "Case #" << i+1 << ": " << solve() << endl;
    }

    fin.close();    
    fout.close();
    system("PAUSE");
    return EXIT_SUCCESS;
}
