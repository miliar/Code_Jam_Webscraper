#include <ctime>
#include <cmath>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <iostream>
#include <functional>
#include <map>
#include <set>
#include <fstream>
#include<bitset>


using namespace std;

typedef long long int64;
#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define fornd(i, n) for (int i = (int)(n) - 1; i >= 0; i--)
#define forab(i, a, b) for (int i = (int)(a); i <= (int)(b); i++)
#define forabd(i, a, b) for (int i = (int)(b); i >= (int)(a); i--)
#define sz(x) ((int) (x).size())
#define pb push_back
int numDigits(int number)
{
    int digits = 0;
    if (number < 0) digits = 1; // remove this line if '-' counts as a digit
    while (number) {
        number /= 10;
        digits++;
    }
    return digits;
}
int main(){

ifstream fin("a.txt");
ofstream fout("out.txt");
int a,b,T;
fin>>T;
map<int,bool> check;
int ten[8]={1,10,100,1000,10000,100000,1000000,10000000};
forn(tt,T){

fin>>a>>b;
int temp;
int sum=0;
forab(i,a,b){
    int digit=numDigits(i);
    forab(j,1,digit-1){
        temp=(i%ten[j])*ten[digit-j]+i/ten[j];
       // cout<<temp<<endl;
      //  if(check[temp]==true) continue;
        if(check[temp]==false && temp<=b && temp>i)
            {
                sum++;
                check[temp]=true;
                }
    }
    check.clear();
}
fout<<"Case #"<<tt+1<<": "<<sum<<endl;
}
}






