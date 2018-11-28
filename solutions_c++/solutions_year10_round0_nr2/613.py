#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <bitset>
#include <string>
#include <functional>
#include <algorithm>
#include <iomanip>


using namespace std;

long long gcd(long long a,long long b)
{
    if (a % b == 0){
        return b;
    }else{
        return gcd(b,a%b);
    }
}
int main()
{
    freopen("B-small-attempt1.in","r",stdin);
    freopen("out_b.txt","w",stdout);
    long long a[128];
    int ca;
    cin >> ca;
    int num;
    for (int i = 1 ;i <= ca ;i++){
        cin >> num;
//        cout << num <<endl;
        for (int i = 0 ; i < num ;i++){
            cin >> a[i];
        }
        int nnum = 1;
        for (int j = 1 ;j < num ;j++){
            if (a[j] != a[0]){
                a[nnum++] = (a[j] > a[0])?(a[j]-a[0]):(a[0]-a[j]);
            }
        }
        int temp = a[1];
        for (int i = 2 ;i < nnum ;i++){
            if (a[i] > temp){
                temp = gcd(a[i],temp);
            }else{
                temp = gcd(temp,a[i]);
            }
        }
        int xx = (temp - a[0]%temp) % temp;
        cout << "Case #" << i << ": " << xx << endl;
        
    }
}



