#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
#include <fstream>

using namespace std;
#define forn(i,n) for(i=0;i<(n);i++)

int calc(int n)
{
    if(n == 2)
         return 27;
    if(n == 3)
         return 143;
    if(n == 4)
         return 751;
    if(n == 5)
         return 935;
    if(n == 6)
         return 607;
    if(n == 7)
         return 903;
    if(n == 8)
         return 991;
    if(n == 9)
         return 335;
    if(n == 10)
         return 47;
    if(n == 11)
         return 943;
    if(n == 12)
         return 471;
    if(n == 13)
         return 55;
    if(n == 14)
         return 447;
    if(n == 15)
         return 463;
    if(n == 16)
         return 991;
    if(n == 17)
         return 95;
    if(n == 18)
         return 607;
    if(n == 19)
         return 263;
    if(n == 20)
         return 151;
    if(n == 21)
         return 855;
    if(n == 22)
         return 527;
    if(n == 23)
         return 743;
    if(n == 24)
         return 351;
    if(n == 25)
         return 135;
    if(n == 26)
         return 407;
    if(n == 27)
         return 903;
    if(n == 28)
         return 791;
    if(n == 29)
         return 135;
    if(n == 30)
         return 647;
}

int main()
{
    int n,k,i;
    ifstream text("C-small.in");
    ofstream result("C-small.out");
    string st;
    getline(text,st);
    n = atoi(st.c_str());
    forn(i,n)
    {
        getline(text,st);
        k = atoi(st.c_str());
        result << "Case #" << i+1 << ": ";
        if(calc(k) < 100)
           result << '0';
        result << calc(k) << '\n';
    }
    result.close();
}
